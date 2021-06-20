import time
import argparse

import bms_stream_receiver_handler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Runs the receiver mechanism for the TCQ project. See -h for more'
                                                 'information')
    parser.add_argument("-s", "--stream", help="Source of stream from sender. Ex: -s console", type=str,
                        default="console", choices=["console"])
    parser.add_argument("-t", "--type", help="Format type of stream from sender. Ex: -t custom", type=str,
                        default="custom", choices=["custom"])
    parser.add_argument("-a", "--analytics",
                        help="Comma separated list of analytical parameters. Ex: -a min,max,simple_moving_average",
                        type=str, default="min,max,simple_moving_average",
                        choices=["min", "max", "simple_moving_average", "min,max", "min,simple_moving_average",
                                 "max,simple_moving_average", "min,max,simple_moving_average"])

    args = parser.parse_args()
    input_stream_source = args.stream
    input_stream_type = args.type
    analytical_parameters = args.analytics.split(',')

    bms_stream_receiver_handler.start(
        input_stream_source,
        input_stream_type,
        analytical_parameters
    )