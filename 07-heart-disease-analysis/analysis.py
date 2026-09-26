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



#print(df.head())

#print(df.isnull().sum())

sns.boxplot(data = df, x = 'sex', y = 'chol')
plt.show()