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

# Titanic Data Cleaning and Analysis

This project focuses on cleaning and analysing the Titanic dataset using pandas, NumPy, and data visualisation tools.

The goal is to handle missing data, create meaningful features, and extract insights about survival patterns.

---

## Overview

The dataset is first loaded and inspected for missing values. Key columns such as `Cabin`, `Age`, and `Embarked` are cleaned using different techniques.

New features are then created to improve analysis, such as whether a passenger had a cabin, their age group, and family size.

---

## Data Cleaning Steps

### Cabin
- The `Cabin` column contains many missing values  
- A new feature `HasCabin` is created:
  - `1` = passenger had a cabin  
  - `0` = no cabin  
- The original `Cabin` column is then removed  

---

### Age
- Missing `Age` values are filled using **median grouped by Pclass and Sex**
- This keeps the data more realistic compared to using a single average  
- Any remaining missing values are filled with the overall median  

---

### Embarked
- Missing values are filled using the **mode (most common value)**  

---

## Feature Engineering

### Age Groups
Passengers are grouped into categories:

- Child (0–13)  
- Teen (13–18)  
- Adult (18–35)  
- Middle-aged (35–60)  
- Senior (60+)  

This makes it easier to analyse survival trends.

---

### Family Features
- `FamilySize` = Parch + SibSp + 1  
- `IsAlone` = 1 if passenger travelled alone, else 0  

This helps analyse how travelling alone vs with family affects survival.

---

## Analysis Performed

- Survival rate based on cabin availability  
- Age distribution (visualised using a histogram)  
- Survival rate by age group  
- Survival comparison between solo travellers and families  

---

## Visualisation

A histogram is used to show the distribution of passenger ages:

- Helps understand the spread of ages  
- Shows where most passengers fall  

---

## Technologies Used

- Python  
- pandas  
- NumPy  
- seaborn  
- matplotlib  

---

## How to Run

1. Install dependencies:

2. Run the script:

3. Make sure the dataset is located at:


---

## Key Insights

- Passengers with cabins had higher survival rates  
- Age plays a role in survival probability  
- Travelling alone vs with family affects survival chances  

---

## Summary

This project demonstrates:

- Data cleaning and preprocessing  
- Handling missing values  
- Feature engineering  
- Data visualisation  
- Exploratory data analysis  

It shows how raw data can be transformed into meaningful insights using Python.