import numpy as np
import pandas as pd

# Reads the movies.csv file into a pandas DataFrame called df
df = pd.read_csv('data_practice/movies.csv')

# Prints the first 5 rows of the dataset so you can quickly inspect it
print(df.head())


# Creates an empty list to store movie titles
titles = []

# Loops through the original_title column
for title in df["original_title"]:
    # Adds each movie title into the titles list
    titles.append(title)

# Prints the first 5 movie titles from the list
print(titles[:5])


# Prints all unique values in the status column
# Example: Released, Rumored, Post Production
print(df["status"].unique())


# Creates an empty list to store movies with the status "Rumored"
released_movies = []

# Loops through the status column
for release in df["status"]:

    # Checks if the word "Rumored" is inside the current status value
    if "Released" in release:
        # Adds the matching status value to the released_movies list
        released_movies.append(release)

# Prints the first 5 values from the released_movies list
print(released_movies[:5])


# Replaces missing values in the genres column with "Unknown"
# This stores the fixed column in missing_rating, but does NOT change df itself
df["genre"] = df["genres"].fillna("Unknown")


# Counts how many rows have the genre exactly equal to "Comedy"
comedy_count = (df["genres"] == "Comedy").sum()

# Prints the number of Comedy movies
print(comedy_count)


# Counts missing/null values in every column
null = df.isnull().sum()

# Prints how many missing values each column has
print(null)