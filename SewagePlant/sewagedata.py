import numpy as np
import pandas as pd
import json

# Number of sensors and samples
num_sens = 5
num_samples = 1800

# Makes the random values the same every time the code runs
np.random.seed(42)

# Generate random ammonia values between 0 and 20
ammonia_samples = np.random.uniform(20, 0, (num_sens, num_samples))

# Print each sensor number and its readings
for x, y in enumerate(ammonia_samples):
    print(f"Sensor {x + 1}: {y}")

# Calculate mean for each sensor
mean = np.mean(ammonia_samples, axis=1)

# Calculate standard deviation for each sensor
std = np.std(ammonia_samples, axis=1)

# Calculate z-scores for each sensor reading
zscore = (ammonia_samples - mean[:, np.newaxis]) / std[:, np.newaxis]

print("")
print(zscore)

# Create a mask where True means the value is an outlier
outlier_mask = np.abs(zscore) > 2

# Count how many outliers each sensor has
most_outlier = np.sum(outlier_mask, axis=1)

# Find the index of the sensor with the most outliers
sensor_most_outliers = np.argmax(most_outlier)

print("")

# Print number of outliers for each sensor
print(most_outlier)

# Print sensor with most outliers
print(sensor_most_outliers + 1)

print("")

# Find difference between mean of sensor 1 and sensor 3
difference = mean[0] - mean[2]
print(difference)


readings = []

for sensor_index, sample_value in enumerate(ammonia_samples):
    for sample_index, values in enumerate(sample_value):
        reading = {
            "sensor_id": f"NH3_{sensor_index+1}",
            "sample_number": sample_index+1,
            "value":float(values),
            "unit": "ppm"

            
        }
        readings.append(reading)

with open("SewageReport.json", 'w') as f:
    json.dump(readings, f, indent = 4)
        
