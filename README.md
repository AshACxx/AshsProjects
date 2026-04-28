# AshsProjects
Clean new repo for adding previous and upcoming projects 
# NBA Scoreboard Analyzer

This is a Python project where I use an NBA API to get live game data and analyse it.

## What it does

- Fetches real-time NBA game data using an API
- Extracts data from nested JSON
- Prints all games played today
- Finds the highest scoring game
- Detects if any games went to overtime
- Converts the data into a pandas DataFrame for easier analysis

## Tech used

- Python
- requests (for API calls)
- pandas (for data handling)

## How to run

1. Install dependencies:


## Example output

- List of games played today
- Highest scoring game
- Overtime games (if any)
- DataFrame of all games

## Project type

This is an API integration + data analysis project.

## Notes

- Data comes from the official NBA public API
- JSON data is saved locally for debugging and reuse

## Future improvements

- Add more stats (lowest score, biggest margin, averages)
- Add visualisations (charts)
- Improve structure and reduce repetition in code


# Ammonia Sensor Data Analysis Project

This project simulates ammonia (NH₃) sensor readings and performs data analysis using NumPy and pandas. It also exports the data into a JSON file for reuse.

---

## Overview

The program generates random ammonia readings between 0 and 20 ppm for multiple sensors. Each sensor contains 1800 samples, creating a realistic dataset.

The data is then analysed using statistical methods and structured into useful formats.

---

## Features

- Generates random sensor data using NumPy  
- Calculates:
  - Mean (average)
  - Standard deviation (spread)
  - Min and Max values
  - Median
- Computes z-scores to measure deviation from the mean  
- Detects outliers using:


- Identifies which sensor has the most outliers  
- Exports all readings to a JSON file  
- Uses pandas to group and summarise sensor data  

---

## JSON Output

Each reading is stored as:

```json
{
  "sensor_id": "NH3_1",
  "sample_number": 1,
  "value": 12.34,
  "unit": "ppm"
}