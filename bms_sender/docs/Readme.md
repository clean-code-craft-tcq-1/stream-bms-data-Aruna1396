#BMS Sender Usage Manual

BSM Sender program will get the BSM parameter values from the desired source to send to desired output.
Currently, BMS values are obtained from inbuilt random number generator and output is printed to the console

##Structure

bms_sender/generic_libs:
        bms_generator.py        -> random bms readings generator
        bms_input_handler.py    -> Functions to verify input parameters for BMS Sender
        bms_output_handler.py   -> Functions to send BMS Data
bms_sender
    bms_sender.py       -> streams the bms readings for the given inputs
    bms_sender_test.py  -> Test application for bms_sender

##Program Usage
Function call:

stream_bms_readings(bms_input, bms_output, bms_parameters, stream_speed, num_of_readings)

bms_input:- Select from which source bsm values to be obtained (Supported:local_database)
bms_output:- Select where BSM data needs to be sent/output(Supported: console)
stream_speed:- The speed at which bms data needs to be output
num_of_readings:- Number of required bsm readings

Example:-

stream_bms_readings("local_database", "console", bms_parameters_with_range, 1, 15)

##Sample Output 1

bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                            'charge_rate': {'min': 0, 'max': 0.8}}

charging_temperature: 35  	  charge_rate: 0.19 	
charging_temperature: 4  	  charge_rate: 0.27 	
charging_temperature: 3 	  charge_rate: 0.19 	
charging_temperature: 14 	  charge_rate: 0.58 	
charging_temperature: 8 	  charge_rate: 0.55 	


##Sample Output 2

bms_parameters_with_range = {'charging_temperature': {'min': 0, 'max': 45},
                            'charge_rate': {'min': 0, 'max': 0.8},
                            'SOC': {'min': 20, 'max': 80}}

charging_temperature: 31  	  charge_rate: 0.68  	  SOC: 51  	  
charging_temperature: 42  	  charge_rate: 0.5  	  SOC: 68  	  
charging_temperature: 4  	  charge_rate: 0.05  	  SOC: 78  	  
charging_temperature: 20  	  charge_rate: 0.7  	  SOC: 39  	  
charging_temperature: 35  	  charge_rate: 0.52  	  SOC: 72 
