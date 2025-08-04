import numpy as np
import roadster
import matplotlib.pyplot as plt


# vill ha sträckan som array till argumentet i total consumption 
distance_anna_km_test, speed_anna_kmph = roadster.load_route('roadster/speed_anna.npz')

#referensvärde, n=640000 st intervall
I = roadster.total_consumption(distance_anna_km_test[-1], 'roadster/speed_anna.npz', 640000)

# totalkonsumptions integralen för olika steglängder, n tillräckligt stort. 
n_values = np.array([1, 2, 4, 8, 16, 32]) * 10000
Con_values = np.array([roadster.total_consumption(distance_anna_km_test[-1], 'roadster/speed_anna.npz', n) for n in n_values])

# felen realtiv ref.värde
Con_errors = np.abs(I - Con_values)

# plottar
plt.loglog(n_values, Con_errors, label = '$E_T(n)$')     #error mot steglängd
plt.loglog(n_values, 1e7*n_values**-2.,  label = "p=2")  #loglog för n^-2 
plt.loglog(n_values, 1000*n_values**-1., label = "p=1")  #loglog för n^-1
plt.ylabel('Error')
plt.xlabel('Intervall [n]')
plt.legend()
plt.grid(which='both', linestyle=':')
plt.show()