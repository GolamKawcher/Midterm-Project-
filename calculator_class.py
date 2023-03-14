import numpy as np
class CalculatorClass:
    def __init__(self):
        pass

    def convert_units(self):
        value = float(input(" Please type the value you want to convert: "))
        from_unit = input("Please type the unit of the value (gm, kg, F, C, cm, m): ")
        to_unit = input("Please type the unit to convert to (gm, kg, F, C, cm, m): ")
        if from_unit == 'gm' and to_unit == 'kg':
            return value * 0.001
        elif from_unit == 'F' and to_unit == 'C':
            return (value - 32) * (5/9)
        elif from_unit == 'cm' and to_unit == 'm':
            return value * 0.01
        else:
            print("Wrong type units")
            return None

    def find_mean(self):
        data_array = list(map(int,input("Please type " , " for separated  data array: ").split(',')))
        return np.mean(data_array)

    def find_variance(self):
        data_array = list(map(int,input("Please type  " , " for separated data array: ").split(',')))
        return np.var(data_array)

    def find_max_value_and_index(self):
        data_array = list(map(int,input("Please type  " , " for separated data array: ").split(',')))
        max_value = np.amax(data_array)
        max_index = np.argmax(data_array)
        return max_value, max_index

    def find_min_value_and_index(self):
        data_array = list(map(int,input("Please type  " , " for separated data array: ").split(',')))
        min_value = np.amin(data_array)
        min_index = np.argmin(data_array)
        return min_value, min_index
