import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

angle_1 = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360]
power_1 = [0.276, 0.213, 0.071, 0.004, 0.070, 0.201, 0.264, 0.194, 0.071, 0.004, 0.071, 0.204, 0.275]


def malus(x, A):
    y = A * np.cos(x * (np.pi / 180)) ** 2
    return y


popt, pcov = curve_fit(malus, angle_1, power_1)
a = popt[0]
perr = np.sqrt(np.diag(pcov))
delta_a = perr[0]

print("Intensity of Light as a Function of Relative Angle Between Two Polarizers")
print("The best fit parameter are:")
print("a =", round(a, 3), "with error", round(delta_a, 3))

fvalues = np.linspace(0, 360, 1000)
plt.figure(0, dpi=300)
plt.plot(angle_1, power_1, 'o', color="black", markersize=4, label="raw data")
plt.plot(fvalues, malus(fvalues, a), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.xlim(0, 360)
plt.ylim(0, 0.3)
plt.xlabel('Relative Angle', fontsize=14)
plt.ylabel('Intensity of Light', fontsize=14)
plt.show()
