#BMS Sender

##Quality Parameters

Cyclomatic Complexity CCN = 4
Duplication = --min-lines 3 --min-tokens 35 --threshold 0 
coverage >= 95%

##Design

During the development of BMS Sender, the following aspects are considered
Note: I have tried to incoporate it to the best of the ability

- Loose couplings between different objects/components
- Open Close Principle: BMS Sender can easily extend different input/output types
  with least modifications in the existing code
- Makes the code reusable: Functions are split & separated to promote reusability
- Flexibility - Plug in and Plug out the components at ease
- Single Responsibility Principle

##Test Specification
