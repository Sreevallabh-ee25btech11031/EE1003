import numpy as np
import matplotlib.pyplot as plt

Vin = 5.0
R = 1000.0
L = 0.01

T = L/R #time constant

t = np.linspace(0, 5*T, 1000)

Vr = Vin*(1 - np.exp(-t/T)) #Voltage across resistor: channel 1
Vl = Vin*np.exp(-t/T) #voltage across inductor: negative of channel 2

plt.plot(t, Vr, color = 'red', label = "Ch-1")
plt.plot(t, -Vl, color = 'blue', label = "Ch-2")
plt.axhline(y=5.0, color='gray', linestyle='--')

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.legend(loc='best')

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.6', color='gray')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='gray')


plt.savefig("Figs/plot.png")
plt.show()

