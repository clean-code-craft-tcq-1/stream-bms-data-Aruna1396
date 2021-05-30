import time


def print_bms_readings_to_console(bms_readings):
    formatted_bms_readings = ""
    for key, value in bms_readings.items():
        formatted_bms_readings += key + ': ' + str(value) + ' \t'
        formatted_bms_readings.strip()
    print(formatted_bms_readings)
    return 'CONSOLE_OUTPUT_SENT'


def set_delay(stream_speed):
    time.sleep(stream_speed)

