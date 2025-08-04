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

## License

CC BY-NC-SA 4.0 — for educational use.

> Developed as part of the course in Scientific Computing, Uppsala University, 2025.
