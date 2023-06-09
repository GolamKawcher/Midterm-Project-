import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class PlotAndSimulate:
    def __init__(self):
        pass

    def plot_normal(self, data, mean=0, std=1):
        plt.hist(data, bins=25, density=True, alpha=0.6, color='g')
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = plt.plot(x, norm.pdf(x, mean, std))
        plt.show()

    def plot_scatter(self, x, y):
        plt.scatter(x, y)
        plt.show()

    def simulate_data(self):
        n = int(input("Enter number of data points to generate: "))
        mean = float(input("Enter mean of the data: "))
        std = float(input("Enter standard deviation of the data: "))
        return np.random.normal(mean, std, n)

    def get_data_from_user(self, data_type):
        print("Type some sample data like 1,2,3,4,5")
        data = input(f"Enter {data_type} data (comma separated): ")
        data = list(map(float, data.split(',')))
        return data

