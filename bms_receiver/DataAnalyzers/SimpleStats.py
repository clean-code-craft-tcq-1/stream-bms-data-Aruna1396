from statistics import mean


class SimpleStats:
    def __init__(self, analytical_parameters, window_size=5):
        self.analytical_parameters = {}
        for param in analytical_parameters:
            self.analytical_parameters[param] = None
        self.data_window = [0] * window_size
        self.function_map = {
            "min": self.calculate_min,
            "max": self.calculate_max,
            "simple_moving_average": self.calculate_simple_moving_average
        }

    def update_data(self, reading):
        self.data_window.append(reading)
        self.data_window.pop(0)
        for param in self.analytical_parameters:
            self.function_map[param]()
        return True

    def calculate_simple_moving_average(self):
        if all(self.data_window) is True:
            self.analytical_parameters["simple_moving_average"] = round(mean(self.data_window), 2)
        else:
            self.analytical_parameters["simple_moving_average"] = f"N.A."

    def calculate_min(self):
        if self.analytical_parameters["min"] is None or self.data_window[-1] < self.analytical_parameters["min"]:
            self.analytical_parameters["min"] = self.data_window[-1]

    def calculate_max(self):
        if self.analytical_parameters["max"] is None or self.data_window[-1] > self.analytical_parameters["max"]:
            self.analytical_parameters["max"] = self.data_window[-1]

    def get(self):
        return self.analytical_parameters
