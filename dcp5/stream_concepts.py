import csv 
import numpy as np
import seaborn as sns
import json

print("=" * 55)
print("SENSOR DATA STREAM CONCEPTS")
print("=" * 55)

# --- Stream Temporal Nature ---
print("\n--- Temporal Data Structure ---\n")



def sim_data(duration_seconds, sample_rate):
    np.random.seed(42)
    annomalies = np.random.uniform(0,10,(duration_seconds,sample_rate))
    return annomalies

def numpy_opp(annomalies):
    mean = np.mean(annomalies, axis = 1)
    std = np.std(annomalies, axis = 1)

    value, count = np.unique(annomalies, return_counts = True)
    mode = value[np.argmax(count)]

    return mean, std, mode

def zscore(annomalies, mean, std):
    zscore = (annomalies - mean[:, np.newaxis]) / std[:, np.newaxis]
    return zscore

def find_outliers(zscore):
    outliers = np.abs(zscore) > 2
    outliers_counts = np.sum(outliers, axis = 1)
    most_outliers = np.argmax(outliers_counts)
    return outliers, outliers_counts, most_outliers

def create_readings(annomalies):
    readings = []
    for sample_index, sample_value in enumerate(annomalies):
        for sensor_index, value in enumerate(sample_value):
            reading= {
                "sensor_id": f"{sample_index+1}",
                "sensor_number": f"{sensor_index+1}",
                "value": float(value),
                }
            readings.append(reading)
    
    return readings
    



















duration_seconds = 3600 # 1 hour in second
sample_rate = 1 # 1 reading per second




