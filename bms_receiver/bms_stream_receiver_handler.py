import threading

import Constant


def create_stream_reader(source):
    return Constant.STREAM_READERS_MAP[source]()


def create_data_parser(stream_type):
    return Constant.DATA_PARSERS_MAP[stream_type]()


def create_analyzer(param, analyzer_map, analytical_parameters, analyzer=Constant.DEFAULT_ANALYZER,
                    window_size=Constant.WINDOW_SIZE):
    if param not in list(analyzer_map.keys()):
        analyzer_map[param] = analyzer(analytical_parameters=analytical_parameters, window_size=window_size)
    return analyzer_map


def perform_analysis(data, analyzer_map, analytical_parameters):
    analysis_output = {}
    for param in data:
        analyzer_map = create_analyzer(param, analyzer_map, analytical_parameters)
        analyzer_map[param].update_data(data[param])
        analysis_output[param] = analyzer_map[param].get()
    return analysis_output


def is_valid(data, quit_event):
    data = data.strip()
    if data == 'BMS_STREAMING_COMPLETE':
        quit_event.set()
        return 'Task Completed'
    elif ':' not in data:
        return 'Format Error'
    return True


def process_stream_until_quit(stream_reader, data_parser, analytical_parameters):
    analyzer_map = {}
    quit_event = threading.Event()
    while not quit_event.is_set():
        raw_input_data = stream_reader.read_input()
        data_validity = is_valid(raw_input_data, quit_event)
        if data_validity == True:
            input_data = data_parser.parse_data(raw_input_data)
            analytics_results = perform_analysis(input_data, analyzer_map, analytical_parameters)
            print(analytics_results)
        else:
            print(data_validity)


def start(input_stream_source, input_stream_type, analytical_parameters):
    stream_reader = create_stream_reader(input_stream_source)
    data_parser = create_data_parser(input_stream_type)
    process_stream_until_quit(stream_reader, data_parser, analytical_parameters)
