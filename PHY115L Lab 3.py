import numpy as np
import matplotlib.pyplot as plt
import statistics
from scipy.optimize import curve_fit

# Free Decay of Driven Damped Harmonic Oscillator Statistics
free_omega = [77.231, 77.244, 77.253, 77.261]
free_B = [0.204, 0.209, 0.211, 0.192]


def half(m):
    u = m / 2
    round(u, 3)
    return u


def resonant_omega(w, y):
    r = np.sqrt(w ** 2 + (y / 2) ** 2)
    round(r, 3)
    return r


def quality(w, y):
    Q = w / y
    round(Q, 3)
    return Q


free_gamma = list(map(half, free_B))
free_Q = list(map(quality, free_omega, free_gamma))
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

