import roadster
import matplotlib.pyplot as plt

def get_velocity_and_distance(route):
    '''
    Returns velocity [km/h] along a route and the distance [km] of the route
    '''
    distance_route_km, _ = roadster.load_route(route)
    v_route_kmph = roadster.velocity(distance_route_km, route)

    return v_route_kmph, distance_route_km

# data
v_anna_kmph, distance_anna_km = get_velocity_and_distance('roadster/speed_anna.npz')
v_elsa_kmph, distance_elsa_km = get_velocity_and_distance('roadster/speed_elsa.npz')


# för punktdiagrammet
_, speed_anna_kmph = roadster.load_route('roadster/speed_anna.npz')
_, speed_elsa_kmph = roadster.load_route('roadster/speed_elsa.npz')

# plot
plt.scatter(distance_anna_km, speed_anna_kmph, label = 'Anna', s = 5)
plt.scatter(distance_elsa_km, speed_elsa_kmph, label = 'Elsa', s = 5)

plt.plot(distance_anna_km, v_anna_kmph)
plt.plot(distance_elsa_km, v_elsa_kmph)

plt.xlabel('Sträcka [km]')
plt.ylabel('Hastighet [km/h]')

plt.legend()
plt.grid()

plt.show()