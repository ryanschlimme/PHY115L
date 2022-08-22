import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

xdata = [0.000, 0.100, 0.200, 0.300, 0.400, 0.500, 0.600, 0.700, 0.800, 0.900, 1.000, 1.100]
ydata = [1.055, 2.952, 3.911, 6.338, 8.973, 10.630, 12.671, 15.126, 16.547, 19.482, 22.704, 24.354]

def func(x,a,b,c):
    y = a*x**2 + b*x + c
    return y

popt, pcov = curve_fit(func, xdata, ydata)
a = popt[0]
b = popt[1]
c = popt[2]
print("The best fit parameters are")
print("a =", round(a, 3))
print("b =", round(b, 3))
print("c =", round(c, 3))

xvalues = np.linspace(0, 1.2, 100)
plt.figure(2)
plt.plot(xdata, ydata, 'o', color = "black", markersize=4, label="data")
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$y$', fontsize=14)
plt.plot(xvalues, func(xvalues,a,b,c), color = 'black', linewidth = 1.2, label="best-fit model")
plt.legend()
plt.show()

perr = np.sqrt(np.diag(pcov))
delta_a = round(perr[0], 3)
delta_b = round(perr[1], 3)
delta_c = round(perr[2], 3)
print("The error of parameter a is ", delta_a)
print("The error of parameter b is ", delta_b)
print("The error of parameter c is ", delta_c)