
import numpy as np
import pandas as pd

df = pd.read_csv("data/titanic_cleaned.csv")

#Average ticket price

ticket = df["Fare"].to_numpy()
pclass = df["Pclass"].to_numpy()


values, count = np.unique(pclass, return_counts = True)

mode_pclass = values[np.argmax(count)]

print(f"The most frequent class is : {mode_pclass}")
#print(df.value_counts())


gender, gender_counts = np.unique(df['Sex'], return_counts = True)
mode_gender = gender[np.argmax(gender_counts)]
print(f"The most frequent gender is : {mode_gender}")