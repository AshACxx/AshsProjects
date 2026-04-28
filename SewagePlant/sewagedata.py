import numpy as np
import pandas as pd


num_sens = 5
num_samples = 1800
np.random.seed(42)

ammonia_samples = np.random.uniform(20,0,(num_sens, num_samples))
for x, y in enumerate(ammonia_samples):
    print(f"Sensor {x}: {y}")

mean = np.mean(ammonia_samples, axis = 1)
std = np.std(ammonia_samples, axis = 1)

zscore = (ammonia_samples - mean[:, np.newaxis]) / std[:, np.newaxis]

print("")
print(zscore)

outlier_mask = np.abs(zscore) > 2
most_outlier = np.sum(outlier_mask, axis =1)
sensor_most_outliers = np.argmax(most_outlier)

print("")

print(most_outlier)
print(sensor_most_outliers)

print("")
difference = mean[0] - mean[2]
print(difference)





    
    