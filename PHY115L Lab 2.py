import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.optimize import curve_fit

frequencies = [0.801, 1.456, 2.725]
lmda = [3.96, 1.98, 1.32]
li = [0.2525, 0.5051, 0.7576]
velocities = [3.17, 2.88, 3.60]
transverse_pulse = [0.77, 0.90, 0.61, 0.75, 0.66]
longitudinal_pulse = [0.62, 0.60, 0.68, 0.65, 0.68, 0.72]

fvf_frequencies = [424.102, 370.235, 317.383, 278.320, 249.023, 219.995, 198.532, 187.800, 166.338]
fvf_lengths = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65]

vwt_frequencies = [219.995, 262.921, 305.846, 338.041, 370.235, 396.153, 433.004, 451.430]
vwt_tensions = [9.8, 14.7, 19.6, 24.5, 29.4, 34.3, 39.2, 44.1]

general_velocity = statistics.mean(velocities)
velocity_error = statistics.stdev(frequencies)
print("The velocity of the spring's transverse wave is", round(general_velocity, 2),
      "with error", round(velocity_error, 2))

transverse_velocity = 3.96 / statistics.mean(transverse_pulse)
transverse_error = statistics.stdev(transverse_pulse)
longitudinal_velocity = 3.96 / statistics.mean(longitudinal_pulse)
longitudinal_error = statistics.stdev(longitudinal_pulse)

print("The transverse pulse velocity is", round(transverse_velocity, 3),
      "with error", round(transverse_error, 3))
print("The longitudinal pulse velocity is", round(longitudinal_velocity, 3),
      "with error", round(longitudinal_error, 3))


def func_l(f, a):
    lmda = a / f
    return lmda


def func_li(f, a, b):
    lmda_inv = a * f + b
    return lmda_inv


def func_fvf(l, a, b):
    f = a / l + b
    return f


def func_vwt(T, a, b):
    f = a * T + b
    return f


# Plot for Modal Frequencies vs Wavelength
lmda_popt, lmda_pcov = curve_fit(func_l, frequencies, lmda)
a_lmda = round(lmda_popt[0], 2)
print()
print("Modal Frequencies vs Wavelength")
print("The best fit parameters are:")
print("a_lmda = ", a_lmda)

lmda_x = np.linspace(0.75, 2.75, 100)
plt.figure()
plt.plot(frequencies, lmda, 'o', color="black", markersize=4)
plt.xlabel('$frequencies$', fontsize=14)
plt.ylabel('$lambda$', fontsize=14)
plt.plot(lmda_x, func_l(lmda_x, a_lmda), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

lmda_perr = np.sqrt(np.diag(lmda_pcov))
lmda_delta_a = round(lmda_perr[0], 2)
print("The error of parameter a_lmda is", lmda_delta_a)


# Plot for Modal Frequencies vs Inverse Wavelength
li_popt, li_pcov = curve_fit(func_li, frequencies, li)
a_li = round(li_popt[0], 2)
b_li = round(li_popt[1], 2)
print()
print("Modal Frequencies vs Inverse Wavelength")
print("The best fit parameters are:")
print("a_li = ", a_li)
print("b_li = ", b_li)

li_x = np.linspace(0.75, 2.75, 100)
plt.figure()
plt.plot(frequencies, li, 'o', color="black", markersize=4)
plt.xlabel('$frequencies$', fontsize=14)
plt.ylabel('$lambda$ $inverse$', fontsize=14)
plt.plot(li_x, func_li(li_x, a_li, b_li), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

li_perr = np.sqrt(np.diag(li_pcov))
li_delta_a = round(li_perr[0], 2)
li_delta_b = round(li_perr[1], 2)
print("The error of parameter a_li is", li_delta_a)
print("The error of parameter b_li is", li_delta_b)


# Plot for Fundamental Vibrating Frequency vs Vibrating Wire Length
fvf_popt, fvf_pcov = curve_fit(func_fvf, fvf_lengths, fvf_frequencies)
a_fvf = round(fvf_popt[0], 2)
b_fvf = round(fvf_popt[1], 2)
print()
print("Fundamental Vibrating Frequency vs Vibrating Wire Length")
print("The best fit parameters are:")
print("a_fvf = ", a_fvf)
print("b_fvf = ", b_fvf)

fvf_x = np.linspace(0.2, 0.7, 100)
plt.figure()
plt.plot(fvf_lengths, fvf_frequencies, 'o', color="black", markersize=4)
plt.xlabel('$lengths$', fontsize=14)
plt.ylabel('$fundamental$ $frequencies$', fontsize=14)
plt.plot(fvf_x, func_fvf(fvf_x, a_fvf, b_fvf), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

fvf_perr = np.sqrt(np.diag(fvf_pcov))
fvf_delta_a = round(fvf_perr[0], 2)
fvf_delta_b = round(fvf_perr[1], 2)
print("The error of parameter a_fvf is", fvf_delta_a)
print("The error of parameter b_fvf is", fvf_delta_b)


# Plot for Fundamental Vibrating Frequency vs Vibrating Wire Tension
vwt_popt, vwt_pcov = curve_fit(func_vwt, vwt_tensions, vwt_frequencies)
a_vwt = round(vwt_popt[0], 2)
b_vwt = round(vwt_popt[1], 2)
print()
print("Fundamental Vibrational Frequency vs Vibrating Wire Tension")
print("The best fit parameters are:")
print("a_vwt = ", a_vwt)
print("b_vwt = ", b_vwt)

vwt_x = np.linspace(9.5, 45, 100)
plt.figure()
plt.plot(vwt_tensions, vwt_frequencies, 'o', color="black", markersize=4)
plt.xlabel('$tensions$', fontsize=14)
plt.ylabel('$fundamental$ $frequencies$', fontsize=14)
plt.plot(vwt_x, func_vwt(vwt_x, a_vwt, b_vwt), color="black", linewidth=1.2, label="best-fit model")
plt.legend()
plt.show()

vwt_perr = np.sqrt(np.diag(vwt_pcov))
vwt_delta_a = round(vwt_perr[0], 2)
vwt_delta_b = round(vwt_perr[1], 2)
print("The error of parameter a_vwt is", vwt_delta_a)
print("The error of parameter b_vwt is", vwt_delta_b)
