#2025 DCP CODING ASSIGNMENT  

import os
import matplotlib.pyplot as plt

from database import my_sql_database, load_tunes_from_database
from parser import books_dir, process
from analysis import get_tunes_by_book, get_tune
from gui import launch_gui


my_sql_database()


# Iterate over directories in abc_books
for item in os.listdir(books_dir):
    # item is the dir name, this makes it into a path
    item_path = os.path.join(books_dir, item)

    # Check if it's a directory and has a numeric name
    if os.path.isdir(item_path) and item.isdigit():
        book_number = int(item)
        print(f"Found numbered directory: {item}")

        # Iterate over files in the numbered directory
        for file in os.listdir(item_path):
            # Check if file has .abc extension
            if file.endswith('.abc'):
                file_path = os.path.join(item_path, file)
                print(f"  Found abc file: {file}")
                process(file_path,book_number)


#df holds the function above
df = load_tunes_from_database()

#displays the values of each book file
print(df["book_number"].value_counts())


#printing the title and key
book2_t = get_tunes_by_book(df, 2)
print(book2_t[["title","key"]].head())

#displays all the tunes from 3400 onwards as this is book2 (abc files)


#returning rthe title andd jig of a song
book3_t = get_tune(df, "Single jig")
print(book3_t[["title","type"]].head())



#count tunes per book
book_counts = df["book_number"].value_counts()

plt.figure(figsize=(8,5))
#creating the bar plots index = x acis, values = y
plt.bar(book_counts.index, book_counts.values)
plt.xlabel("Book Number")
plt.ylabel("Number of Tunes")
plt.title("Tunes per Book")

plt.show()


type_counts =  df["type"].value_counts()
plt.figure(figsize=(8,5))
plt.bar(type_counts.index, type_counts.values)
plt.xlabel("Tune Type")
plt.ylabel("Count")
plt.title("Distribution of Tune Types")
plt.xticks(rotation=90)
plt.show()



launch_gui(df)
