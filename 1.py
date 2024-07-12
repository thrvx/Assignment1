import numpy as np
import matplotlib.pyplot as plt

# Given temperature data
time_points = np.array([0, 2, 4, 6, 8, 10])  # Time in hours
temperatures = np.array([15, 18, 21, 24, 20, 16])  # Temperature in degrees Celsius

# Time point where we want to estimate the temperature
query_time = 5

# Average Interpolation
def average_interpolation(time_points, temperatures, query_time):
    return np.mean(temperatures)

# Linear Interpolation
def linear_interpolation(time_points, temperatures, query_time):
    return np.interp(query_time, time_points, temperatures)

# Calculate interpolated temperatures
avg_temp = average_interpolation(time_points, temperatures, query_time)
linear_temp = linear_interpolation(time_points, temperatures, query_time)

print(f"Average Interpolated Temperature: {avg_temp:.2f}°C")
print(f"Linear Interpolated Temperature: {linear_temp:.2f}°C")

# Plotting the data and interpolations
plt.plot(time_points, temperatures, 'bo-', label='Original Data')
plt.axhline(avg_temp, color='r', linestyle='--', label=f'Average Interpolation: {avg_temp:.2f}°C')
plt.plot(query_time, linear_temp, 'go', label=f'Linear Interpolation: {linear_temp:.2f}°C')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.title('Temperature Interpolation')
plt.grid(True)
plt.show()


