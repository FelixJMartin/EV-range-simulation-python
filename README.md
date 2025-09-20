# EV Range Estimation — Tesla Roadster Simulation

This project estimates the remaining driving range of an electric vehicle along a given route, based on speed and energy consumption data. It was developed as part of a course in scientific computing at Uppsala University.

The program uses real-world data from a Tesla Roadster and GPS-tracked speed profiles to simulate energy usage and travel time using numerical methods.

## Features

- ⚡ Consumption model fitted to Tesla Roadster data  
- 📈 Speed interpolation from GPS route data  
- 🧮 Numerical integration using the trapezoidal rule  
- 🔁 Convergence studies and error analysis  
- 🧠 Newton's method to compute time, distance, and range  
- 🚗 Route simulation with time-dependent speed functions (Euler’s method)

## Technologies

- Python 3  
- NumPy  
- Matplotlib

## Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ev-range-estimation.git
   cd ev-range-estimation
   ```

2. Unpack the provided `roadster.zip` (contains data and base code).

3. Run the scripts in order:
   ```bash
   python script_part1a.py  # Plot consumption curve
   python script_part1b.py  # Route and speed visualization
   python script_part2a.py  # Travel time estimation
   ...
   ```

## Data Sources

- **Consumption Data**: Tesla Roadster energy consumption modeled as  
  \( c(v) = \frac{a_1}{v} + a_2 + a_3v + a_4v^2 \)

- **Route Data**: GPS-based speed profiles from two routes (`speed_anna.npz` and `speed_elsa.npz`)

- **NYC Traffic Model**: Based on historical average speeds from NYC road segments



# EV Range Estimation — Tesla Roadster Simulation

The project involves developing a navigation app and onboard computer for electric vehicles, extended with functionality to estimate the remaining driving range along a given route based on the vehicle’s current battery charge. Since energy consumption depends strongly on speed, range can vary significantly between different routes.

In this project, we estimate range using data on energy consumption at different speeds together with expected speed along a chosen route. For development, we use consumption data from the Tesla Roadster combined with GPS-derived speed data for a test route. The functionality is designed to be generalizable to other vehicle models and adaptable to expected speeds derived from speed limits, historical driving data, or real-time traffic information.

### Part 1a) Energy Consumption Model

To estimate the driving range of the Tesla Roadster, the energy consumption as a function of speed is modeled by:

\[
c(v) = a_1 v^{-1} + a_2 + a_3 v + a_4 v^2
\]

with coefficients:

- \(a_1 = 546.8\)  
- \(a_2 = 50.31\)  
- \(a_3 = 0.2584\)  
- \(a_4 = 0.008210\)

Here \(v\) is the speed in km/h and \(c(v)\) is the consumption in Wh/km.

**Task A:**  
Implement the function `consumption(v)` in `roadster.py` so that it computes \(c(v)\) for any positive input speed. The function must support both scalar inputs and NumPy arrays, returning the corresponding scalar or array of consumption values.

In addition, update the script `script_part1a.py` to plot the energy consumption as a function of speed over the interval \(v \in [1,200]\) km/h.


