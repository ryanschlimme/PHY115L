import numpy as np
import statistics
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

length_n = [1, 3, 3, 5, 5, 7, 7, 9]
lengths = [0.228, 0.392, 0.407, 0.555, 0.577, 0.711, 0.755, 0.922]


def linreg(x, a, b):
    y = a * x + b
    return y


popt, pcov = curve_fit(linreg, length_n, lengths)
a = popt[0]
b = popt[1]

print("Best Fit Wavelength and End Correction")
print("The best fit parameters are:")
print("Lambda =", round(a * 4, 3), "m")
print("End Correction =", round(b, 3), "m")
print("Therefore the speed of sound as measured is", round(a * 4 * 1026, 3), "m/s")

corrected = a * 4 * 1026 * np.sqrt(293.15 / (273.15 + 22.2))
theoretical = np.sqrt(1.4 * 1 / 1.225)

print("The corrected speed of sound at standard temperature is", round(corrected, 3), "m/s")
print("The theoretical speed of sound at standard temperature is", round(theoretical, 3), "m/s")


def speed(f, L, n):
    c = 2 * L / n * f
    return c


def frequencies(c, h, L, n):
    f = 0.113 * h / (L ** 2) * c * ((2 * n + 1) ** 2)
    return f


width = 0.0635
thickness = 0.0125
length = 0.76
c = np.sqrt(83.5E9 / 8770)

print()
print("Speed of Longitudinal Sound in Bulk Metal")
print("The longitudinal wave speed for 1669.156 Hz is", round(speed(1669.156, length, 1), 3))
print("The longitudinal wave speed for 2180.906 Hz is", round(speed(2180.906, length, 2), 3))
print("The longitudinal wave speed for 2675.781 Hz is", round(speed(2675.781, length, 3), 3))

print()
print("Expected Frequencies of Transverse Sound in Bulk Metal")
print("The expected frequency for mode 1 is", round(frequencies(c, thickness, length, 1), 3))
print("The expected frequency for mode 2 is", round(frequencies(c, thickness, length, 2), 3))
print("The expected frequency for mode 3 is", round(frequencies(c, thickness, length, 3), 3))
print("The expected frequency for mode 4 is", round(frequencies(c, thickness, length, 4), 3))
print("The expected frequency for mode 5 is", round(frequencies(c, thickness, length, 5), 3))
print("The expected frequency for mode 6 is", round(frequencies(c, thickness, length, 6), 3))

predicted_frequencies = (67.912, 188.645, 369.744, 611.209)
sound_results = (68.6, 115.1, 158.9, 213.9)


def sqrt(x, a):
    y = a * np.sqrt(x)
    return y


popt, pcov = curve_fit(sqrt, predicted_frequencies, sound_results)
m = popt[0]
perr = np.sqrt(np.diag(pcov))
delta_m = perr[0]

print()
print("Functional Dependence of Sound Propagation vs Transverse Frequency")
print("The best fit parameters are:")
print("m =", round(m, 3))
print("The error in m is", round(delta_m, 3))

fvalues = np.linspace(0, 700, 1000)
plt.figure(0, dpi=300)
plt.plot(predicted_frequencies, sound_results, 'o', color="black", markersize=4, label="raw data")
plt.plot(fvalues, sqrt(fvalues, m), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.xlim(0, 700)
plt.ylim(0, 300)
plt.xlabel('$f$ (Hz)', fontsize=14)
plt.ylabel('Speed of Sound $m/s$', fontsize=14)
plt.show()
