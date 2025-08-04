#!/usr/bin/env python3
import numpy as np
import roadster
import matplotlib.pyplot as plt

speed_kmph = np.linspace(1., 200., 1000)
consumption_Whpkm = roadster.consumption(speed_kmph)

# plotting the consumption as a func. of speed, c(v)

plt.plot(speed_kmph, consumption_Whpkm, label = 'c(v)')

plt.xlabel('Hastighet, v [km/h]')
plt.ylabel('Energiförbrukning, c [Wh/km]')

plt.legend()
plt.grid()

plt.show()