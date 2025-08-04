import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def load_route(route):
    """ 
    Get speed data from route .npz-file. Example usage:

      distance_km, speed_kmph = load_route('speed_anna.npz')
    
    The route file should contain two arrays, distance_km and 
    speed_kmph, of equal length with position (in km) and speed 
    (in km/h) along route. Those two arrays are returned by this 
    convenience function.
    """
    # Read data from npz file
    if not route.endswith('.npz'):
        route = f'{route}.npz' 
    data = np.load(route)
    distance_km = data['distance_km']
    speed_kmph = data['speed_kmph']    
    return distance_km, speed_kmph

def save_route(route, distance_km, speed_kmph):
    """ 
    Write speed data to route file. Example usage:

      save_route('speed_olof.npz', distance_km, speed_kmph)
    
    Parameters have same meaning as for load_route
    """ 
    np.savez(route, distance_km=distance_km, speed_kmph=speed_kmph)

### PART 1A ###
def consumption(v):
    '''
    Returns electric consumption c(v) [Wh/km] for a given velocity v [hm/h]
    '''
    a_1 = 546.8                         # coefficients
    a_2 = 50.31                         #
    a_3 = 0.2584                        #
    a_4 = 0.008210                      #
    c = a_1/v + a_2 + a_3*v + a_4*v**2  # electric consumption, c(v)
    return c

### PART 1B ###
def velocity(x, route):
    # ALREADY IMPLEMENTED!
    """
    Interpolates data in given route file, and evaluates the function
    in x
    """
    # Load data
    distance_km, speed_kmph = load_route(route)
    # Check input ok?
    assert np.all(x>=0), 'x must be non-negative'
    assert np.all(x<=distance_km[-1]), 'x must be smaller than route length'
    # Interpolate
    v = interpolate.pchip_interpolate(distance_km, speed_kmph,x)
    return v

### PART 2A ###
def time_to_destination(x, route, n):
    '''
    Returns time T(x) [h] for given covered distance x [km]
    '''
    h = x/n                                                 # delintervall för given sträcka
    s_array = np.linspace(0, x, n+1)                        # sträcka-array från 0 till x
    f_array = 1/velocity(s_array, route)                    # integrand
    T = h*(np.sum(f_array)-0.5*(f_array[0]+f_array[-1]))    # beräknar tiden med trapetsmetoden
    return T

### PART 2B ###
def total_consumption(x, route, n):
    '''
    Returns electric consumption E(x) [Wh] for a given covered distance x [km]
    '''
    h = x/n                                                 # delintervall för given sträcka
    s_array = np.linspace(0, x, n+1)                        # sträcka-array från 0 till x
    f_array = consumption(velocity(s_array, route))         # integrand
    E = h*(np.sum(f_array)-0.5*(f_array[0]+f_array[-1]))    # beräknar elkonsumptionen med trapetsmetoden
    return E

### PART 3A ###
def distance(T, route): 
    '''
    Solves time_to_destination(x) - T = 0 with Newton-Raphsons method
    '''
    # parametrar
    n = int(1e6)
    delta_x = 1

    # f
    def f(x):
        return time_to_destination(x, route, n) - T
    
    # f'
    def df(x):
        return 1/velocity(x, route)
    
    # startgissning
    distance_km, speed_kmph = load_route(route)
    x = np.mean(speed_kmph)*T   # sträcka [km] ≈ medelhastighet [km/h] * tid [h]

    # om T > totala tiden, returnera hela sträckan
    if T >= time_to_destination(distance_km[-1], route, n):
        return distance_km[-1]

    # Newton-Raphson
    E_T = (time_to_destination(x, route, n) - time_to_destination(x, route, 2*n))/3 # tredjedelsregeln
    while abs(delta_x + E_T) >= 1e-4:
        # beräkna nytt x med NR
        delta_x = -f(x)/df(x)
        x += delta_x
        
    return x

### PART 3B ###
def reach(C, route):
    '''
    Solves total_consumption(x) - C = 0 with Newton-Raphsons method
    '''
    # parametrar
    n = int(1e6)
    delta_x = 1

    # f
    def f(x):
        return total_consumption(x, route, n) - C
    
    # f'
    def df(x):
        return consumption(velocity(x, route))
    
    # startgissning
    distance_km, speed_kmph = load_route(route)
    consumption_array = consumption(speed_kmph)
    x = C/np.mean(consumption_array)   # sträcka [km] ≈ laddning [Wh] / medelförbrukning [Wh/km]

    # om C > totala konsumtionen, returnera hela sträckan
    if C >= total_consumption(distance_km[-1], route, n):
        return distance_km[-1]

    # Newton-Raphson
    E_T = (total_consumption(x, route, n) - total_consumption(x, route, 2*n))/3 # tredjedelsregeln
    while abs(delta_x + E_T) >= 1e-4:
        delta_x = -f(x)/df(x)
        x = x + delta_x

    return x