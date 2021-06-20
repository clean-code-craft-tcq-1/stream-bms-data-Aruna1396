import re



class CustomDataParser:
    def __init__(self):
        pass

    def parse_data(self, data):
        parsed_data = {}
        data = re.sub(' +', ' ', data)
        data = data.replace(': ', ':')
        data_split = data.split()
        for each_data in data_split:
            param_name, param_value = each_data.split(':')
            parsed_data[param_name] = round(float(param_value), 2)
        return parsed_data
