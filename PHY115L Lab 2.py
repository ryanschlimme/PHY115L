import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.optimize import curve_fit

frequencies = [0.801, 1.456, 2.725]
wavelengths = [3.96, 1.98, 1.32]

plt.figure(1)
plt.plot(frequencies, wavelengths, 'o', color="black", markersize=4)
plt.xlabel('$f (Hz)$', fontsize=14)
plt.ylabel('$lambda (m)$', fontsize=14)
plt.show()
