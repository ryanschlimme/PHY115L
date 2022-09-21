import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.optimize import curve_fit

# Free Decay of Driven Damped Harmonic Oscillator Statistics
free_omega = [77.231, 77.244, 77.253, 77.261]
free_B = [0.204, 0.209, 0.211, 0.192]


def half(m):
    u = m / 2
    return u


def resonant_omega(w, y):
    r = np.sqrt(w ** 2 + (y / 2) ** 2)
    return r


def div(w, y):
    Q = w / y
    return Q

def sub(a, b):
    c = a - b
    return c


free_gamma = list(map(half, free_B))
free_Q = list(map(div, free_omega, free_gamma))
free_resonant_omega = list(map(resonant_omega, free_omega, free_gamma))

mean_free_res_omega = round(statistics.mean(free_resonant_omega), 2)
sd_free_res_omega = round(statistics.stdev(free_resonant_omega) / np.sqrt(len(free_resonant_omega)), 2)
mean_free_omega = round(statistics.mean(free_omega), 2)
sd_free_omega = round(statistics.stdev(free_omega) / np.sqrt(len(free_omega)), 2)
mean_free_B = round(statistics.mean(free_B), 3)
sd_free_B = round(statistics.stdev(free_B) / np.sqrt(len(free_B)), 3)
mean_free_gamma = round(statistics.mean(free_gamma), 3)
sd_free_gamma = round(statistics.stdev(free_gamma) / np.sqrt(len(free_gamma)), 3)
mean_free_Q = round(statistics.mean(free_Q), 2)
sd_free_Q = round(statistics.stdev(free_Q) / np.sqrt(len(free_Q)), 2)

print("Free Decay of Driven Damped Harmonic Oscillator Statistics")
print("The average value of omega is", mean_free_omega)
print("The standard error of omega is", sd_free_omega)
print()
print("The average value of the resonant frequency is", mean_free_res_omega)
print("The standard error of the resonant frequency is", sd_free_res_omega)
print()
print("The average value of B is", mean_free_B)
print("The standard error of B is", sd_free_B)
print()
print("The average value of gamma is", mean_free_gamma)
print("The standard error of gamma is", sd_free_gamma)
print()
print("The average value of Q is", mean_free_Q)
print("The standard error of Q is", sd_free_Q)

# Measurement of the Driven Oscillation of a Damped Cantilever
f_data = [2, 4, 6, 10, 20]
driven_V = [0.838036, 0.837460, 0.837098, 0.836974, 0.834571]
driven_A = [0.203719, 0.220444, 0.257813, 0.583482, 0.124076]
phi_V = [5.534568, 4.369257, 0.977612, 1.261262, 0.513714]
phi_A = [5.528414, 4.362403, 0.960685, 1.293395, 2.660390]

phi = list(map(sub, phi_A, phi_V))
R = list(map(div, driven_V, driven_A))


def R_func(f, a, b, c):
    R_val = a / np.sqrt((f**2 - b**2)**2 + f**2 * c**2)
    return R_val


popt, pcov = curve_fit(R_func, f_data, R, p0 = [1.0, 55.0, 1])
a = popt[0]
b = np.abs(popt[1])
c = np.abs(popt[2])

print()
print("Measurement of the Driven Oscillation of a Damped Cantilever")
print("The best fit parameters are")
print("a =", round(a, 3))
print("b =", round(b, 3))
print("c =", round(c, 3))

perr = np.sqrt(np.diag(pcov))
delta_a = perr[0]
delta_b = perr[1]
delta_c = perr[2]

print("The error of parameter a is", round(delta_a, 3))
print("The error of parameter b is", round(delta_b, 3))
print("The error of parameter c is", round(delta_c, 3))

fvalues = np.linspace(0, 600, 1000)
plt.figure(1, dpi=300)
plt.plot(f_data, R, 'o', color = "black", markersize = 4, label = "raw data")
plt.xlim(0, 120)
plt.xlabel('$f$ (Hz)', fontsize = 14)
plt.ylabel('Amplitude Ratio $R$', fontsize = 14)
plt.plot(fvalues, R_func(fvalues, a, b, c), color = "black", linewidth = 1.2, label = "best-fit model")
plt.legend()
plt.show()
plt.figure(2, dpi=300)
plt.plot(f_data, R, 'o', color = "black", markersize = 4, label = "raw data")
plt.xlim(100, 600)
plt.ylim(0, 0.05)
plt.xlabel('$f$ (Hz)', fontsize = 14)
plt.ylabel('Amplitude Ratio $R$', fontsize = 14)
plt.plot(fvalues, R_func(fvalues, a, b, c), color = "black", linewidth = 1.2, label = "best-fit model")
plt.legend()
plt.show()


def dphi(f, a, b, c):
    dphi = np.arctan2(c*f, b**2 - f**2)
    return dphi


plt.figure(3, dpi = 300)
plt.plot(f_data, phi, 'o', color = "black", markersize = 4, label = "data")
plt.xlim(0, 100)
plt.xlabel('$f$ (Hz)', fontsize = 14)
plt.ylabel('$\Delta\phi$', fontsize = 14)
plt.plot(fvalues, dphi(fvalues, a, b, c), color = 'black', linewidth = 1.2, label = "best-fit model")
plt.legend()
plt.show()

plt.figure(4, dpi = 300)
plt.plot(f_data, phi, 'o', color = "black", markersize = 4, label = "best-fit model")
plt.xlim(0, 20)
plt.xlabel('$f$ (Hz)', fontsize = 14)
plt.ylabel('$\Delta\phi$', fontsize = 14)
plt.plot(fvalues, dphi(fvalues, a, b, c), color = 'black', linewidth = 1.2, label = "best-fit model")
plt.legend()
plt.show()
