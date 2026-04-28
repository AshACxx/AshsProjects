import numpy as np
import pandas as pd
import json


def generate_data(num_sens, num_samples):
    """Generate random ammonia values between 0 and 20."""
    np.random.seed(42)
    ammonia_samples = np.random.uniform(0, 20, (num_sens, num_samples))
    return ammonia_samples


def calculate_stats(ammonia_samples):
    """Calculate mean and standard deviation for each sensor."""
    mean = np.mean(ammonia_samples, axis=1)
    std = np.std(ammonia_samples, axis=1)
    return mean, std


def calculate_zscores(ammonia_samples, mean, std):
    """Calculate z-scores for each sensor reading."""
    zscore = (ammonia_samples - mean[:, np.newaxis]) / std[:, np.newaxis]
    return zscore


def find_outliers(zscore):
    """Find outliers where absolute z-score is greater than 2."""
    outlier_mask = np.abs(zscore) > 2
    outlier_counts = np.sum(outlier_mask, axis=1)
    sensor_most_outliers = np.argmax(outlier_counts)
    return outlier_mask, outlier_counts, sensor_most_outliers


def create_readings(ammonia_samples):
    """Convert sensor data into a list of dictionaries for JSON."""
    readings = []

    for sensor_index, sample_values in enumerate(ammonia_samples):
        for sample_index, value in enumerate(sample_values):
            reading = {
                "sensor_id": f"NH3_{sensor_index + 1}",
                "sample_number": sample_index + 1,
                "value": float(value),
                "unit": "ppm"
            }

            readings.append(reading)

    return readings


def save_to_json(readings, filename):
    """Save readings to a JSON file."""
    with open(filename, "w") as f:
        json.dump(readings, f, indent=4)


def create_pandas_summary(readings):
    """Create pandas DataFrame and summary statistics."""
    df = pd.DataFrame(readings)

    sensor_summary = df.groupby("sensor_id")["value"].agg([
        "mean",
        "std",
        "min",
        "max",
        "count",
        "sum",
        "median"
    ])

    return df, sensor_summary


# ==============================
#          MAIN PROGRAM
# ==============================

num_sens = 5
num_samples = 1800

ammonia_samples = generate_data(num_sens, num_samples)

mean, std = calculate_stats(ammonia_samples)

zscore = calculate_zscores(ammonia_samples, mean, std)

outlier_mask, outlier_counts, sensor_most_outliers = find_outliers(zscore)

readings = create_readings(ammonia_samples)

save_to_json(readings, "SewageReport.json")

df, sensor_summary = create_pandas_summary(readings)

print("Outlier counts per sensor:")
print(outlier_counts)

print("\nSensor with most outliers:")
print(sensor_most_outliers + 1)

print("\nDifference between sensor 1 mean and sensor 3 mean:")
difference = mean[0] - mean[2]
print(difference)

print("\nFirst 5 rows of DataFrame:")
print(df.head())

print("\nSensor Summary:")
print(sensor_summary)