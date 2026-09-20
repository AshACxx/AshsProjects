import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('06-customer-churn-analysis/data/Telco-Customer-Churn.csv')
print(df.head())


print("="*60)
print("Looking for null values")
print("="*60)