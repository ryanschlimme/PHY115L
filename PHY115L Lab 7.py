import numpy as np

a = 19.50*np.pi/180
n = np.sin(a)*np.sqrt((4*(4.35**2)*(np.cos(a)**2))/(2.70**2)+1)
print(round(n, 2))

print(round(np.arcsin(1/1.13)*180/np.pi, 2))
print(round(np.arcsin(1/1.515)*180/np.pi, 3))

delta = np.sin(0.5*(60+42.5)*np.pi/180)/np.sin(0.5*60*np.pi/180)
print(round(delta, 2))
