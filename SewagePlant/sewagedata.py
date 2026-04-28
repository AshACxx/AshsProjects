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






    
    