import matplotlib.pyplot as plt

def plot_data_and_fit(x_data, y_data, popt, nonlinear_function):
    plt.scatter(x_data, y_data, label='Data')
    plt.plot(x_data, nonlinear_function(x_data, *popt), label='Fitted curve')
    plt.legend()
    plt.savefig("xy.png")
    