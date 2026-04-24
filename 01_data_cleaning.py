import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt




print("="*60)
print("Data Cleaning for Tiatnic.csv")
print("="*60)

df = pd.read_csv("data/titanic.csv")

print(df.head())

print(f"This dataset contains: {df.shape}")

print("="*60)
print("Looking for null values")
print("="*60)
print(f"{df.isnull().sum()} values")

print("="*60)
print("Cabin cleaning")
print("="*60)

df["HasCabin"] = df["Cabin"].notna().astype(int)

print("The survival rate of the cabin is:", df.groupby('HasCabin')["Survived"].mean())

df = df.drop(columns=["Cabin"])

print("="*60)
print("Age Cleaning")
print("="*60)

print("Median age by Pclass and Sex")
print(df.groupby(['Pclass', 'Sex'])['Age'].median())

print(f"The amount of missing values before imputation was:{df['Age'].isnull().sum()}")

# Fill missing Age with group median
df["Age"] = df.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median())) #use tramsform when doing operations on grouped classes
df['Age'] = df['Age'].fillna(df['Age'].median)
print("The amount of missing values in Age after imputation is:", df['Age'].isnull().sum())

plt.figure(figsize=(10, 6))

sns.histplot(df["Age"])

plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

print("The total number of missing values in Embark:", df["Embarked"].isnull().sum())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print("Embarked after imputations is:",df['Embarked'].isnull().sum())

print("="*60)
print("Checking how many missing values for each column")
print("="*60)

print(df.isnull().sum())

print("="*60)
print("Binning age groups")
print("="*60)

df["AgeGroup"] = pd.cut(
    df['Age'],
    bins = [0,13,18,35,60,80],
    labels = ["Child", "Teen", "Adult", "Middle-aged","Senior"]
)
print("Age group distribution table")
print(df['AgeGroup'].value_counts().sort_index())

print("Survival rate by age group")
print(df.groupby('AgeGroup')['Survived'].mean())

print("="*60)
print("Family Survival Rate")
print("="*60)

df['FamilySize'] = df["Parch"] + df["SibSp"] + 1
df['IsAlone'] = (df["FamilySize"] == 1).astype(int)

print(f"The total number of solo travellers was {df['IsAlone'].sum()}")
print(f"The survival rate of a solo traveller is {df[df['IsAlone'] == 1]['Survived'].mean():.2%}")

print(f"The total number of family travellers was {df['IsAlone'].sum()}")
print(f"The survival rate of a solo traveller is {df[df['IsAlone'] == 0]['Survived'].mean():.2%}")