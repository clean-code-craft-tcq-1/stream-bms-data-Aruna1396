import time
import unittest
from generic_libs import bms_input_handler as bms_input
from generic_libs import bms_generator
from generic_libs import bms_output_handler
import bms_sender
from mock import patch


class BMSSenderTest(unittest.TestCase):

    """"
    *********************************
        BMS Sender Test
    *********************************
    """
    def test_if_bms_sender_successfully_streams_data(self):
        bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                                     'charge_rate': {'min': 0, 'max': 0.8},
                                     'SOC': {'min': 20, 'max': 80}}
        self.assertEqual(bms_sender.stream_bms_readings("local_database", "console", bms_parameters_with_range, 0.2, 3),
                         'BMS_STREAMING_COMPLETE')

    def test_if_bms_sender_reports_error_for_invalid_inputs(self):
        bms_parameters_with_range = {}
        self.assertEqual(bms_sender.stream_bms_readings("local_database", "console", bms_parameters_with_range, 1, None)
                         , 'INVALID_INPUT_STREAM_FAILED')

    """"
    *********************************
        File: bms_input_handler
    *********************************
    """

    def test_if_bms_io_type_supported_for_valid_data(self):
        self.assertTrue(bms_input.is_within_supported_types('local_database', 'console'))

    def test_if_bms_io_type_unsupported_for_invalid_data(self):
        invalid_input_list = [(None, None), ('cloud', 'console'), ('local_database', 'logger')]
        for invalid_input in invalid_input_list:
            self.assertFalse(bms_input.is_within_supported_types(invalid_input[0], invalid_input[1]))

    def test_checks_if_bms_parameters_are_valid(self):
        bms_parameters = [{'SOC': {'min': 20, 'max': 80}, 'charge_rate': {'min': 0, 'max': 0.8}},
                          {'charging_temperature': {'min': 0, 'max': 45}, 'charge_rate': {'min': 0, 'max': 0.8},
                           'SOC': {'min': 20, 'max': 80}}]
        for bms_parameter in bms_parameters:
            self.assertTrue(bms_input.is_bms_parameters_valid(bms_parameter))

    def test_checks_if_bms_parameters_are_invalid(self):
        invalid_bms_parameters = [{}, {'battery_load': {'min': 10, 'max': 50}},
                                  {'SOC': {'min': 20, 'max': 80}, 'SOH': {'min': 0, 'max': 0.8}},
                                  {'SOC': {'min': 20, 'max': 80}, 'SOH': {'min': 0, 'max': 0.8},
                                   'charge_rate': {'min': 0, 'max': 0.8}}]
        for bms_parameter in invalid_bms_parameters:
            self.assertFalse(bms_input.is_bms_parameters_valid(bms_parameter))

    def test_checks_is_stream_parameters_are_valid(self):
        self.assertTrue(bms_input.is_stream_parameters_valid(2, 40))

    def test_checks_is_stream_parameters_are_invalid(self):
        invalid_stream_parameters = [(None, None), (0, None), (None, 0), (0, 0)]
        for stream_parameter in invalid_stream_parameters:
            self.assertFalse(bms_input.is_stream_parameters_valid(stream_parameter[0], stream_parameter[1]))

    def test_checks_if_input_is_valid(self):
        bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                                     'charge_rate': {'min': 0, 'max': 0.8}}
        self.assertEqual(bms_input.is_input_valid("local_database", "console", bms_parameters_with_range, 1, 15),
                         'VALID_INPUT')
        self.assertEqual(bms_input.is_input_valid("local_database", "console", bms_parameters_with_range, None, 0),
                         'INVALID_INPUT')

    """"
    *********************************
        File: bms_generator
    *********************************
    """
    def test_yields_decimal_place_for_rounding_off_bms_data(self):
        bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                                     'charge_rate': {'min': 0, 'max': 0.8},
                                     'SOC': {'min': 20, 'max': 80}}
        expected_output = [bms_generator.INTEGER_DECIMAL_PLACE, bms_generator.FLOAT_DECIMAL_PLACE,
                           bms_generator.INTEGER_DECIMAL_PLACE]
        input_values = ['charging_temperature', 'charge_rate', 'SOC']
        for i in range(2):
            self.assertEqual(bms_generator.set_bms_parameter_decimal_place(input_values[i], bms_parameters_with_range),
                             expected_output[i])

    """"
    *********************************
        File: bms_sender
    *********************************
    """

    @patch('generic_libs.bms_generator.generate_bms_readings')
    def test_get_bms_readings_from_mock_bms_generator(self, mock_bms_generator):
        bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                                     'charge_rate': {'min': 0, 'max': 0.8}}
        mock_bms_generator.return_value = {'charging_temperature': 30, 'charge_rate': 0.49}
        self.assertEqual(bms_sender.get_bms_readings_from_bms_generator(bms_parameters_with_range),
                         {'charging_temperature': 30, 'charge_rate': 0.49})


if __name__ == '__main__':
    unittest.main()
