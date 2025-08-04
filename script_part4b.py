#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import route_nyc 

### Given contour plot ###
n_fine = 100
t_fine = np.linspace(0, 24, n_fine)
x_fine = np.linspace(0, 60, n_fine)
tt_fine, xx_fine = np.meshgrid(t_fine, x_fine)
zz_fine = route_nyc.route_nyc(tt_fine,xx_fine)
w, h = plt.figaspect(0.4)
fig = plt.figure(figsize=(w, h))
plt.axes().set_aspect(0.2, adjustable='box')
cs = plt.contourf(tt_fine,xx_fine,zz_fine, 50, cmap=cm.get_cmap('jet'))
plt.xlabel('Time [hour of day]',fontsize=18)
plt.ylabel('Distance [km]',fontsize=18)
plt.title('Speed [km/h]',fontsize=18)
fig.colorbar(cs)
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')

#rutter med start 4.5, och 9. 

t_1, d_1, s_1 = route_nyc.nyc_route_traveler_euler(4, 0.01)
t_2, d_2, s_2 = route_nyc.nyc_route_traveler_euler(9.5, 0.01)

plt.plot(t_1, d_1, color="silver", linestyle="--", label="Route start 04:00h")
plt.plot(t_2, d_2, color="darkmagenta", linestyle="--", label="Route start 09:30h")

# Add a legend in the upper right corner with a white background
plt.legend(loc="upper right", fontsize=14, facecolor="white", edgecolor="black", framealpha=0.8)

plt.show()