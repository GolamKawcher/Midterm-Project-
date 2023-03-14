from data_class import GetDataClass
from calculator_class import CalculatorClass
from plot_class import PlotAndSimulate

data = GetDataClass()
calculator = CalculatorClass()
plot = PlotAndSimulate()

def main():
    while True:
        
        print(" Following functions are available:")
        print(" 1.  This is for load data from file")
        print(" 2.  This is for load data from files in the same directory")
        print(" 3.  This is for Please validates data ")
        print(" 4.  This is for the convert units")
        print(" 5.  This is for find mean")
        print(" 6.  This is for find variance")
        print(" 7.  This is for find minimum value and index")
        print(" 8.  This is for find maximum value and index")
        print(" 9.  This is for simulates a random dataset")
        print("10.  This is for normal Plot data ")
        print("11.  This is for scatter Plot data")
        
        user_choice = input("Please choose and enter the number of the function which one you need : ")

        
        if user_choice == "1":
            data.read_data()
        elif user_choice == "2":
            data.data_load_from_directory()
        elif user_choice == "3":
            data.validate_data()
        elif user_choice == "4":
            result = calculator.convert_units()
            print("Converted value:",result)
        elif user_choice == "5":
            result = calculator.find_mean()
            print("The mean value is: ", result)
        elif user_choice == "6":
            result = calculator.find_variance()
            print("The variance value is: ", result)
        elif user_choice == "7":
            result = calculator.find_min_value_and_index()
            print("The Minimum value and index are: ", result)
        elif user_choice == "8":
            result = calculator.find_max_value_and_index()
            print("The Maximum value and index are: ", result)
        elif user_choice == "9":
            result = plot.simulate_data()
            print("The Simulate Dataset is: ", result)
        elif user_choice == "10":
            result = plot.simulate_data()
            plot.plot_normal(result)
        elif user_choice == "11":
            x = plot.get_data_from_user("x")
            y = plot.get_data_from_user("y")
            plot.plot_scatter(x, y)
            
        else:
            print("Invalid ! Please enter a number between 1 and 8.")

    
        print("Function done.")

        
        repeat = input("Would you want to use this function again ? (y/n): ")
        if repeat.lower() != "y":
            
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
