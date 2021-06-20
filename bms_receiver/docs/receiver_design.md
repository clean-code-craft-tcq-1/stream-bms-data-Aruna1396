## Tasks

### System boundaries

| Item                              | Included?     | Reasoning / Assumption
|-----------------------------------|---------------|---
Read and parse Console Input        | Yes           | Part of the software requirements
Calculate maximum and minimum       | Yes           | Part of the software requirements
Calculate simple moving average     | Yes           | Part of the software requirements
Quit Calculation on receiving input | Yes           | To ensure graceful exit and no miscalculated values
Verify reception frequency          | No            | Not part of software requirements
BMS param validation                | No            | Params received as in. Assume validation elsewhere
Param reception acknowledgement     | No            | Leads to assumptions on sender and stream capabilities

### Test cases

1. Generate "Format error" output when the input format cannot be recognized
1. Validate raw stream input converted to internal data structure when available on stream
1. Validate internal data structure created with appropriate keys from input stream
1. Validate calculated maximum and minimum values detection from the stream for each new input
1. Validate calculated simple moving average of the last 5 parameter values for each new input
1. Validate printed output of calculated values for each parameter
1. Generate "Task Completed" output when "BMS_STREAMING_COMPLETE" is received on stream

### Fakes and Reality

| Functionality                | Input                            | Output                     | Faked/mocked part
|------------------------------|----------------------------------|----------------------------|-----------------------------
Read param from input          | sensor data stream               | input stream string        | Mocked the console std input
Validate input                 | internal data-structure          | valid / invalid / no data  | Faked the input data
Parse input                    | input stream string              | internal data-structure    | Faked the input string
Calculate max/min              | sensor values                    | calculated values          | Faked the sensor values
Calculate simple moving average| sensor values                    | calculated value           | Faked the sensor values
Validate analytics output      | sensor data stream               | analytics output stream    | Mocked the console std input and output
Ensure graceful quit           | text in input stream             | program close              | Mocked the console std input and output