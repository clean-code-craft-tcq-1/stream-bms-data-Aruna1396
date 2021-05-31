# BMS Sender Usage Manual

BSM Sender program will get the BSM parameter values from the desired source & sends to desired output medium.  
Currently, BMS values are obtained from an inbuilt random number generator and output is printed to the console.

## Structure

bms_sender/generic_libs  
        `bms_generator.py`        -> random bms readings generator  
        `bms_input_handler.py`    -> Functions to verify input parameters for BMS Sender  
        `bms_output_handler.py`   -> Functions to send BMS Data  

bms_sender  
    `bms_sender.py`       -> streams the bms readings for the given inputs  
    `bms_sender_test.py`  -> Test application for bms_sender  

## Program Usage
Function call:

`stream_bms_readings(bms_input, bms_output, bms_parameters, stream_speed, num_of_readings)`

`bms_input`:- Select from which source bsm values to be obtained (Supported:local_database)  
`bms_output`:- Select where BSM data needs to be sent/output(Supported: console)  
`stream_speed`:- The speed at which bms data needs to be output  
`num_of_readings`:- Number of required bsm readings  

Example:-

`stream_bms_readings("local_database", "console", bms_parameters_with_range, 1, 15)`

### Sample Output 1

bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                            'charge_rate': {'min': 0, 'max': 0.8}}  

![output 1](https://github.com/clean-code-craft-tcq-1/stream-bms-data-Aruna1396/blob/8112cf769763bf57bd3fec4cccda81dc04880233/bms_sender/docs/BMSSenderOuput_2Parameters.png)  


### Sample Output 2

bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                            'charge_rate': {'min': 0, 'max': 0.8},
                            'SOC': {'min': 20, 'max': 80}}  

![output 2](https://github.com/clean-code-craft-tcq-1/stream-bms-data-Aruna1396/blob/8112cf769763bf57bd3fec4cccda81dc04880233/bms_sender/docs/BMSSenderOuput_3Parameters.png)  


