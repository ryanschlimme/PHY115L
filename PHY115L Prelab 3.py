import numpy as np

x = [3.0, -3.0, -3.0, 3.0]
y = [4.0, 4.0, -4.0, -4.0]


def divide(m, n):
    u = n / m
    return u


yx = list(map(divide, x, y))

atan = np.arctan(yx) * 180 / np.pi
atan2 = np.arctan2(y, x) * 180 / np.pi

print(atan)
print(atan2)
