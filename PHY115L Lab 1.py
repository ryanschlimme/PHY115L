import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.optimize import curve_fit

volt_list = [4.821, 5.493, 5.626, 4.951, 5.248, 5.588, 4.585, 4.677, 5.494, 4.665, 5.390, 5.294, 4.490, 4.796,
             5.219, 4.763, 5.074, 4.949, 5.514, 4.891, 4.571, 5.269, 5.210, 5.165, 5.403, 5.042, 5.081, 5.143,
             5.642, 5.689]

mean_V = round(statistics.mean(volt_list), 3)
print("The mean of V is", mean_V)

std_V = round(statistics.stdev(volt_list), 3)
print("The statistical error of V is", std_V)

length = len(volt_list)
std_mean = round(std_V / length, 3)
print("The statistical error in the mean is", std_mean)

length_list = [0.400, 0.600, 0.800, 1.000, 1.200, 1.400, 1.600]
frequency_list = [391.77, 261.73, 197.91, 157.17, 129.21, 110.97, 102.13]

plt.figure(1)
plt.plot(length_list, frequency_list, 'o', color="black", markersize=4)
plt.xlabel('$L$', fontsize=14)
plt.ylabel('$f$', fontsize=14)
plt.show()


def func(L, a):
    f = a / L
    return f


popt, pcov = curve_fit(func, length_list, frequency_list)
a = round(popt[0], 2)
print("The best fit parameters are")
print("a = ", a)

xvalues = np.linspace(0.2, 1.8, 100)
plt.figure(2)
plt.plot(length_list, frequency_list, 'o', color="black", markersize=4, label="data")
plt.xlabel('$L$', fontsize=14)
plt.ylabel('$f$', fontsize=14)
plt.plot(xvalues, func(xvalues, a), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

perr = np.sqrt(np.diag(pcov))
delta_a = round(perr[0], 2)
print("The error of parameter a is", delta_a)
