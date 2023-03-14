import pandas as pd
import numpy as np
import os

class GetDataClass:
    def __init__(self):
        self.data = None

    def read_data(self):
        file_path = input("Please enter the file path which one you want : ")
        if os.path.exists(file_path):
            self.data = np.genfromtxt(file_path, delimiter=',')
            print(self.data)
        else:
            print("Invalid file path and please enter the path carefully")


    def data_load_from_directory(self):
        directory_path = input("Enter the same directory path: ")

        if not os.path.isdir(directory_path):
            raise ValueError(f"{directory_path} is not a wrong  directory path what you enter")

        
        files = [file for file in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, file))]

        
        for i, file in enumerate(files):
            print(f"{i+1}. {file}")

        
        file_index = int(input("Enter the file number you want : "))

        
        if file_index < 1 or file_index > len(files):
            raise ValueError("Invalid file number you choose")

        
        file_name = files[file_index-1]

        file_path = os.path.join(directory_path,file_name)

       
        data = pd.read_csv(file_path, delimiter=',', header=None, dtype=float)

        
        data_array = data.to_numpy()
        print(data_array)
        return data_array
    
    def validate_data(self):
        directory_path = input("Enter the path of the directory containing the CSV files: ")
        csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

        
        print("The following CSV files were found in the directory:")
        for i, f in enumerate(csv_files):
            print(f"{i + 1}. {f}")

        
        file_index = int(input("Enter the number of the file you would like to open and validate: ")) - 1

        
        file_path = os.path.join(directory_path, csv_files[file_index])
        df = pd.read_csv(file_path)

        
        if df.isnull().values.any():
            print("There are NaN values in your data.")
            return False

        
        if not all(df.dtypes == 'float64'):
            print("There are Decimal values in your data.")
            return True

        
        print("Your data is perfect.")
        return True
    
    