import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('07-heart-disease-analysis/data/heart.csv')
checkChol = (df['chol'] == 0).sum()
print(f"There are {checkChol} rows that equal to 0")

checkNa = df.isna().sum()
print(checkNa)
#print(df.head())

#printing how many rows equal or exceed 500
condition = (df['sex'] == 0) & (df['chol'] >= 500)

print("\n")
print(df[condition].index)

print(df['chol'].describe())

#print(df.isnull().sum())

sns.boxplot(data = df, x = 'sex', y = 'chol')
plt.show()