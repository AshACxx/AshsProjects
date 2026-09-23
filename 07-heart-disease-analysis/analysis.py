import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('07-heart-disease-analysis/data/heart.csv')

print(df.head())

print(df.isnull().sum())

sns.boxplot(data = df, x = 'sex', y = 'chol')
plt.show()