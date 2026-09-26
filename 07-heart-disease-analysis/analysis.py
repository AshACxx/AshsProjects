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

print("\n")

print(df.head())

print("\n")
sns.histplot(data = df, x = 'ca', bins = 4)
plt.show()
sns.boxplot(data = df, x = 'sex', y = 'chol')
plt.show()
#printing how many rows equal or exceed 500
condition = (df['sex'] == 0) & (df['chol'] >= 500)
print(f"The index of cholestrol equal or above 500 are: {df[condition].index}")
print(df['chol'].describe())

#print(df.isnull().sum())

#checking chol from asc
print(df['chol'].sort_values(ascending= False).head(10))

print("\n")

targetCounts = df['target'].value_counts()
print(targetCounts)

#getting rid of 4 since its not a real value

df.loc[df['ca'] == 4, 'ca'] = np.nan
print(df['ca'].value_counts())
sns.histplot(data = df, x = 'ca')
plt.show()

for col in ['sex', 'age', 'ca', 'thal']:
    sns.countplot(data = df, x = col, hue = 'target')
    plt.show()