from io import StringIO
import threading
import unittest.mock
import bms_stream_receiver_handler
from StreamReaders import ConsoleStreamReader
from DataParsers import CustomDataParser
from DataAnalyzers import SimpleStats


class BMSStreamReceiverTest(unittest.TestCase):
    @unittest.mock.patch("builtins.input", side_effect=["Test Raw Input"])
    def test_raw_input(self, mock_stdin):
        test_stream_reader = ConsoleStreamReader()
        test_output = "Test Raw Input"
        received_output = test_stream_reader.read_input()
        self.assertEqual(received_output, test_output)

    def test_invalid_input(self):
        test_input_data = "Invalid test input"
        test_event = threading.Event()
        test_output = bms_stream_receiver_handler.is_valid(test_input_data, test_event)
        self.assertEqual(test_output, "Format Error")

    def test_parse_input(self):
        test_input_data = "charging_temperature: 50        charge_rate: 0.5"
        test_parser = CustomDataParser()
        test_output = {
            "charging_temperature": 50,
            "charge_rate": 0.5
        }
        received_output = test_parser.parse_data(test_input_data)
        self.assertEqual(received_output, test_output)

    def test_max_min(self):
        test_analytical_parameters = ["max", "min"]
        test_input_data = [50, 45, 30.5, 75, 22.22]
        test_analyzer = SimpleStats(test_analytical_parameters)
        test_output = {
            "max": 75,
            "min": 22.22
        }
        for test_input in test_input_data:
            test_analyzer.update_data(test_input)
        received_output = test_analyzer.get()
        self.assertEqual(received_output, test_output)

    def test_simple_moving_average(self):
        test_analytical_parameters = ["simple_moving_average"]
        test_input_data = [0.2, 0.4, 0.6, 0.8, 1]
        test_analyzer = SimpleStats(test_analytical_parameters)
        test_output = {
            "simple_moving_average": 0.6
        }
        for test_input in test_input_data:
            test_analyzer.update_data(test_input)
        received_output = test_analyzer.get()
        self.assertEqual(received_output, test_output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    @unittest.mock.patch("builtins.input", side_effect=["charging_temperature: 3         charge_rate: 0.59",
                                                        "charging_temperature: 33        charge_rate: 0.71",
                                                        "charging_temperature: 40        charge_rate: 0.16",
                                                        "charging_temperature: 37        charge_rate: 0.19",
                                                        "charging_temperature: 11        charge_rate: 0.18",
                                                        "BMS_STREAMING_COMPLETE"])
    def test_output(self, mock_stdin, mock_stdout):
        test_input_stream_source = "console"
        test_input_stream_type = "custom"
        test_analytical_parameters = ["min", "max", "simple_moving_average"]
        test_output = "{'charging_temperature': {'min': 3.0, 'max': 3.0, 'simple_moving_average': 'N.A.'}, " \
                      "'charge_rate': {'min': 0.59, 'max': 0.59, 'simple_moving_average': 'N.A.'}}\n" \
                      "{'charging_temperature': {'min': 3.0, 'max': 33.0, 'simple_moving_average': 'N.A.'}, " \
                      "'charge_rate': {'min': 0.59, 'max': 0.71, 'simple_moving_average': 'N.A.'}}\n" \
                      "{'charging_temperature': {'min': 3.0, 'max': 40.0, 'simple_moving_average': 'N.A.'}, " \
                      "'charge_rate': {'min': 0.16, 'max': 0.71, 'simple_moving_average': 'N.A.'}}\n" \
                      "{'charging_temperature': {'min': 3.0, 'max': 40.0, 'simple_moving_average': 'N.A.'}, " \
                      "'charge_rate': {'min': 0.16, 'max': 0.71, 'simple_moving_average': 'N.A.'}}\n" \
                      "{'charging_temperature': {'min': 3.0, 'max': 40.0, 'simple_moving_average': 24.8}, " \
                      "'charge_rate': {'min': 0.16, 'max': 0.71, 'simple_moving_average': 0.37}}\n" \
                      "Task Completed"
        bms_stream_receiver_handler.start(test_input_stream_source, test_input_stream_type, test_analytical_parameters)
        self.assertEqual(mock_stdout.getvalue().strip(), test_output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    @unittest.mock.patch("builtins.input", side_effect=["BMS_STREAMING_COMPLETE"])
    def test_quit(self, mock_stdin, mock_stdout):
        test_input_stream_source = "console"
        test_input_stream_type = "custom"
        test_analytical_parameters = ["min"]
        bms_stream_receiver_handler.start(test_input_stream_source, test_input_stream_type, test_analytical_parameters)
        self.assertEqual(mock_stdout.getvalue().strip(), "Task Completed")

unittest.main()
