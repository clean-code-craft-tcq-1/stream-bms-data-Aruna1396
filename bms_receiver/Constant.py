from DataAnalyzers import SimpleStats
from DataParsers import CustomDataParser
from StreamReaders import ConsoleStreamReader

WINDOW_SIZE = 5
DEFAULT_STAT_FUNCTIONS = ["min", "max", "simple_moving_average"]
DEFAULT_ANALYZER = SimpleStats
STREAM_READERS_MAP = {
    "console": ConsoleStreamReader
}
DATA_PARSERS_MAP = {
    "custom": CustomDataParser
}