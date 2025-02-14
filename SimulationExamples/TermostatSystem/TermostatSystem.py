import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
T_min = 18  # Lower threshold (°C)
T_max = 22  # Upper threshold (°C)
T_heater = 50  # Heater max temperature (°C)
T_ambient = 10  # Ambient temperature (°C)
k1 = 0.5  # Heating rate coefficient
k2 = 0.1  # Cooling rate coefficient


def heating(t, T):
    return k1 * (T_heater - T)  # Heating equation


def cooling(t, T):
    return -k2 * (T - T_ambient)  # Cooling equation


def simulate_thermostat(T_init, t_end, dt=0.1):
    time = [0]
    temperature = [T_init]
    mode = "heating" if T_init <= T_min else "idle"

    t = 0
    while t < t_end:
        T_current = temperature[-1]

        if mode == "heating":
            sol = solve_ivp(heating, [t, t + dt], [T_current], max_step=dt)
            T_next = sol.y[0][-1]
            if T_next >= T_max:
                mode = "idle"
        else:
            sol = solve_ivp(cooling, [t, t + dt], [T_current], max_step=dt)
            T_next = sol.y[0][-1]
            if T_next <= T_min:
                mode = "heating"

        t += dt
        time.append(t)
        temperature.append(T_next)

    return time, temperature


# Run simulation

time, temperature = simulate_thermostat(T_init=18, t_end=50)


# Plot results
plt.figure(figsize=(8, 5))
plt.plot(time, temperature, label="Temperature")
plt.axhline(T_min, color='r', linestyle='--', label="T_min")
plt.axhline(T_max, color='g', linestyle='--', label="T_max")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.title("Thermostat System Simulation")
plt.legend()
plt.grid()
plt.show()
