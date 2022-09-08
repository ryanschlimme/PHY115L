import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

frequencies = [0.801, 1.456, 2.725]
wavelengths = [3.96, 1.98, 1.32]
inverse_waves = [0.2525, 0.5051, 0.7576]

def func(f, a, b):
    l = a*f + b
    return l


popt, pcov = curve_fit(func, frequencies, inverse_waves)
a = round(popt[0], 2)
b = round(popt[1], 2)
print("The best fit parameters are")
print("a = ", a)
print("b = ", b)

xvalues = np.linspace(0.75, 2.75, 100)
plt.figure(1)
plt.plot(frequencies, inverse_waves, 'o', color="black", markersize=4)
plt.xlabel('$f$', fontsize=14)
plt.ylabel('$inverse$', fontsize=14)
plt.plot(xvalues, func(xvalues, a, b), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

perr = np.sqrt(np.diag(pcov))
delta_a = round(perr[0], 2)
delta_b = round(perr[1], 2)
print("The error of parameter a is", delta_a)
print("The error of parameter b is", delta_b)
