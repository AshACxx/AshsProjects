import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('06-customer-churn-analysis/data/Telco-Customer-Churn.csv')
print(df.head())


print("="*60)
print("Looking for null values")
print("="*60)

print(f"{df.isnull().sum()} values")

print(f"This dataset contains {df.shape}")

print(df.info())


print("="*60)
print("cleaning Total Charges")
print("="*60)

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors = 'coerce')
print(df.isnull().sum())