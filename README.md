# AshsProjects

A collection of university, personal, and upcoming projects focused on data science, artificial intelligence, machine learning, and software development.

## AI Database Analyst

An AI-powered database assistant built with Python, SQLite, Streamlit, and Ollama.

The application allows users to ask questions about a database using normal English. The system reads the database structure, converts the user's question into SQL, checks that the generated query is safe, executes it, and then explains the results in plain English.

### Features

- Ask database questions using natural language
- Automatically reads database tables and column structure
- Converts user questions into SQLite queries
- Restricts generated SQL to read-only operations
- Blocks commands such as `DELETE`, `DROP`, `UPDATE`, `INSERT`, and `ALTER`
- Executes valid SQL queries against the database
- Displays results in a pandas DataFrame
- Shows the generated SQL query
- Uses Llama 3.2 locally through Ollama
- Generates a simple explanation of the returned results

### Tech Stack

- Python
- SQLite
- SQL
- Streamlit
- pandas
- LangChain
- Ollama
- Llama 3.2

### How It Works

```text
User Question
    ↓
Read Database Schema
    ↓
Llama 3.2
    ↓
Generate SQL Query
    ↓
SQL Safety Check
    ↓
Execute Query
    ↓
Return Database Results
    ↓
Llama 3.2
    ↓
Natural Language Explanation
```
### Demo

Below is an example of the application analysing the Northwind SQLite database using a natural-language question.

![AI Database Analyst Demo](assets/sql-database-analyst.png)

The application converts the user's question into SQL, executes the query against the database, displays the returned data, and generates a natural-language explanation of the results.

### Database Schema Detection

Before generating a query, the application reads the SQLite database structure.

It retrieves:

- Table names
- Column names
- Column data types

This information is passed to the language model so that it can generate SQL based on the actual structure of the database.

### Natural Language to SQL

The user's question is passed to Llama 3.2 along with the database schema.

For example:

```text
Which customers have placed the most orders?
```

The model generates an appropriate SQLite query based on the available tables and columns.

### SQL Safety

Before a generated query is executed, it passes through a validation step.

The application blocks SQL containing operations such as:

```text
DELETE
DROP
UPDATE
INSERT
ALTER
CREATE
REPLACE
```

Only queries beginning with:

```sql
SELECT
```

or:

```sql
WITH
```

are allowed to run.

This prevents the AI from intentionally or accidentally modifying the database.

### Query Results

After the SQL query is executed, the application retrieves:

- Column names
- Returned rows

The results are then displayed in a pandas DataFrame through the Streamlit interface.

### Result Explanation

The generated SQL and database results are passed back to Llama 3.2.

The model then converts the raw database output into a short, readable answer to the user's original question.

To avoid sending unnecessarily large amounts of data to the model, the explanation step uses a maximum of the first 20 returned rows.

### Project Files

```text
AI-Database-Analyst/
├── sqlapp.py
└── sql_agent.py
```

#### `sqlapp.py`

Handles the Streamlit interface, including:

- User questions
- Database location
- Displaying generated answers
- Displaying query results
- Showing generated SQL

#### `sql_agent.py`

Contains the main database and AI logic, including:

- SQLite connection
- Database schema detection
- Natural-language-to-SQL generation
- SQL validation
- Query execution
- Result explanation

### Example Questions

Examples of questions the application could handle include:

```text
Which products are the most expensive?
```

```text
How many customers are in each country?
```

```text
Which employees have processed the most orders?
```

```text
What are the top five products by price?
```

The generated SQL depends on the structure and contents of the connected database.

### Current Limitations

- Currently designed for SQLite databases
- Uses a fixed database location in the Streamlit application
- SQL validation is based on query text and allowed starting commands
- Generated SQL accuracy depends on the language model understanding the database schema
- The result explanation only sends the first 20 rows to the model
- Llama 3.2 must be running locally through Ollama

### Future Improvements

Possible improvements include:

- Allow users to upload their own SQLite databases
- Improve SQL validation using SQL parsing
- Add support for additional database systems
- Add charts and automatic data visualisations
- Add conversation history
- Add example question suggestions
- Improve error handling for invalid generated SQL
- Add automated tests
- Deploy the Streamlit interface

### What It Demonstrates

This project demonstrates experience with:

- SQL and relational databases
- Natural language to SQL
- Database schema inspection
- LLM integration
- Query validation and safety
- Data processing with pandas
- Streamlit application development
- Building AI tools around structured data




---

## AI Study Assistant (RAG)

A Retrieval-Augmented Generation (RAG) study assistant built with Python and Streamlit. Users can upload a PDF, ask questions about its contents, and receive answers based on the most relevant sections of the document.

The application also displays the page numbers used as sources for each response.

### Features

- Upload and process PDF documents
- Split documents into overlapping text chunks
- Generate embeddings using Hugging Face
- Store document chunks in a Chroma vector database
- Retrieve relevant information using similarity search
- Generate answers locally using Llama 3.2 through Ollama
- Restrict responses to information found in the uploaded document
- Display source page numbers
- Simple Streamlit interface

### Tech Stack

- Python
- Streamlit
- LangChain
- Chroma
- Hugging Face Embeddings
- Ollama
- Llama 3.2
- PyPDFLoader

### How It Works

```text
PDF Upload
    ↓
PDF Text Extraction
    ↓
Text Chunking
    ↓
Hugging Face Embeddings
    ↓
Chroma Vector Database
    ↓
Similarity Search
    ↓
Relevant Document Context
    ↓
Llama 3.2
    ↓
Answer + Source Pages
```
### Demo

Below is an example of the application answering a question about an uploaded CV.

![AI Study Assistant Demo](assets/rag-study-assistant.png)

The application retrieves information from the uploaded PDF, generates an answer based on the relevant document content, and displays the page used as the source.

The PDF is split into smaller chunks and converted into embeddings. These embeddings are stored in Chroma and searched when the user asks a question. The most relevant sections are then passed to Llama 3.2, which generates an answer based only on the retrieved document content.

---

## NBA Scoreboard Analyzer

A Python project that retrieves live NBA game data through an API and performs basic analysis on the results.

### Features

- Fetches real-time NBA game data
- Extracts information from nested JSON
- Displays games played on the current day
- Finds the highest-scoring game
- Detects overtime games
- Converts game data into a pandas DataFrame for further analysis

### Tech Stack

- Python
- Requests
- pandas
- REST APIs
- JSON

### Example Analysis

The program can return:

- Games played today
- Highest-scoring game
- Overtime games
- Structured game data in a pandas DataFrame

### Project Type

API integration and data analysis project.

### Notes

- Data is retrieved from the NBA API
- JSON responses can be saved locally for debugging and reuse

### Future Improvements

- Add average scores and scoring statistics
- Calculate winning margins
- Add team-level analysis
- Add charts and visualisations
- Improve code structure and reduce repetition

---

## Ammonia Sensor Data Analysis

A data analysis project that simulates ammonia (NH₃) sensor readings using NumPy and analyses the generated data using pandas.

### Overview

The program generates ammonia readings between 0 and 20 ppm across multiple sensors.

Each sensor contains 1,800 samples, creating a dataset that can be used for statistical analysis and outlier detection.

### Features

- Generates simulated sensor readings using NumPy
- Calculates descriptive statistics including:
  - Mean
  - Standard deviation
  - Minimum
  - Maximum
  - Median
- Calculates z-scores
- Detects statistical outliers
- Identifies which sensor contains the most outliers
- Converts the data into structured pandas DataFrames
- Exports sensor readings to JSON

### JSON Structure

Each sensor reading is stored in the following format:

```json
{
  "sensor_id": "NH3_1",
  "sample_number": 1,
  "value": 12.34,
  "unit": "ppm"
}
```

### Tech Stack

- Python
- NumPy
- pandas
- JSON

### What It Demonstrates

- Data simulation
- Statistical analysis
- Outlier detection
- Data transformation
- JSON data handling
- pandas DataFrame operations

---

## Titanic Data Cleaning and Analysis

A data cleaning and exploratory analysis project using the Titanic dataset.

The project focuses on handling missing values, creating new features, and analysing patterns that may have influenced passenger survival.

### Data Cleaning

#### Cabin

The `Cabin` column contains a large number of missing values.

A new feature called `HasCabin` is created:

- `1` = passenger had recorded cabin information
- `0` = no recorded cabin information

The original `Cabin` column is then removed.

#### Age

Missing `Age` values are filled using the median age grouped by:

- Passenger class (`Pclass`)
- Sex

Any remaining missing values are filled using the overall median age.

#### Embarked

Missing values in `Embarked` are filled using the mode, representing the most common embarkation location.

### Feature Engineering

#### Age Groups

Passengers are grouped into age categories:

- Child: 0–13
- Teen: 13–18
- Adult: 18–35
- Middle-aged: 35–60
- Senior: 60+

This makes it easier to compare survival rates between different age groups.

#### Family Features

Two additional features are created:

```text
FamilySize = Parch + SibSp + 1
```

`IsAlone` is used to identify whether a passenger travelled alone or with family.

### Analysis Performed

- Survival rate based on cabin availability
- Passenger age distribution
- Survival rate by age group
- Survival comparison between solo travellers and passengers travelling with family

### Visualisation

A histogram is used to examine the distribution of passenger ages and understand which age ranges were most common.

### Tech Stack

- Python
- pandas
- NumPy
- seaborn
- matplotlib

### Key Insights

The analysis explores relationships between:

- Cabin availability and survival
- Passenger age and survival
- Family size and survival
- Travelling alone compared with travelling with family

### What It Demonstrates

- Data cleaning and preprocessing
- Missing-value handling
- Feature engineering
- Exploratory data analysis
- Statistical analysis
- Data visualisation

---

## Technologies Used Across Projects

### Programming

- Python
- SQL
- C
- R
- PHP
- HTML

### Data & Machine Learning

- pandas
- NumPy
- TensorFlow
- Hugging Face
- Chroma
- Tableau
- Orange

### AI & Development

- LangChain
- Ollama
- Streamlit
- Git
- GitHub

---

## About

These projects were created while studying Data Science and Artificial Intelligence at Technological University Dublin.

The repository will continue to be updated with new projects covering data science, machine learning, AI, and software development.

---

# Data Centric Programming Assignment 2025 (OPTIMISED SEPTEMBER 2026)


# Description of the project
Program designed to read 2 folders containing ABC files representing different books
The program parses and stores the tunes in a dictionary which is saved in a list
A database is used to store a table that takes the contents of each tunes.
Pandas is used for analysis of the data and 
We can access this data using a GUI

# Instructions for use
Run the program
A window will be opened with the 3 boxes that will let u search by:
Book number
Title
Jig
Input into the search bar which books youd like to look up 
# How it works:
First we import our libraries

1. Establish connection to our database tunes2.db that will be used to store our table
if the already exists, it gets dropped


2. #### Reading the File
- File is opened, all the inesa are read using readlines()

#### Parsing tunes 
- As the for loop iterates, the inforation is being tracked using current_tune via dictionary and all completed tunes are stored inside a list called "tunes"

#### Identifying tune informatiom
- X: Tune number
- T: Title
- K: Key signature
- R: Rhythm/type (e.g., jig)
- When the loop detects one of these keys it stores the information in current_tune

#### Detecting a new tune
- When a newe x appears
- The previous tune in current_tunes is then saved in the list tunes
- The next current_tune dictionary is created to take in the information of the next tune

#### Storing the Body
- Any other line that does not contain the main keys (x,t,k,r) is considered the body, which is the remainder of the information of the tunes and stored in "body"
- Finally when the loop ends and the last tune is added to the list "tunes" the parsed list is then returned 



```Python
def process_file(file):
    
    tunes = [] #1
    current_tune = {}
    
    with open(file, 'r') as f:
        lines = f.readlines()
    # list comprehension to strip the \n's
    lines = [line.strip() for line in lines]

    # just print the files for now
    for line in lines:
        
        
        #if the line starts with X, we are on a tune
        if line.startswith("X:"):
            #saving previous tune 
            if current_tune:
                tunes.append(current_tune)
                
            #new tune present 
            current_tune = {"X": line[2:].strip(),"body":""}
            print(line)  
                
        elif line.startswith("T:"):
            current_tune["title"] = line[2:].strip()
            
        elif line.startswith("K:"):
            current_tune["key"] = line[2:].strip()
            
        elif line.startswith("R:"):
            current_tune["type"] = line[2:].strip()
            
        #current_tune["body"] taking "body from the dictionary and adding the lines that dont have x t k or r
        else:
            
            
            if "body" not in current_tune:
                #making body a key
                current_tune["body"] = ""
                #adding on body to a new line
            current_tune["body"] += line + "\n"
                
                
    if current_tune:
        tunes.append(current_tune)
        
    return tunes #returns to #1
```

3. 
#### Function inserting()
- Takes the parsed data and stores them into the rows of the sql database. We can later retrieve this information for searching and analysis

#### Establishing a DB connection
- The function creates a sql db called tunes2.db
- Cursor is used to execute sql commands

#### Table
- We dont know if a table exists before hand so the function makes sure to specify that "IF NOT EXIST" and creates the table with the rows
- id — auto-incrementing primary key
- book_number — identifies the source book the tune came from
- title — tune title
- key — key signature
- type — tune type (e.g. jig, reel)
- body — remaining ABC notation

#### Inserting
- The function loops through the newly parsed tunes and inserts them into the table, it uses .get to retrieve the dictionary values

#### Commiting the changes to the Database
- The database changes are saved with commit() then the connection is closed

```Python
def inserting(book_number,tunes):
    conn = sqlite3.connect("tunes2.db")
    cursor = conn.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS tunes2 (id INTEGER PRIMARY KEY AUTOINCREMENT, book_number INTEGER, title TEXT, key TEXT, type TEXT, body TEXT)')
    
    for tune in tunes: #1 is used to insert the data into a table
        
        cursor.execute('INSERT INTO tunes2(book_number,title,key,type,body) VALUES (?,?,?,?,?)',(book_number,tune.get("title", ""),tune.get("key", ""),tune.get("type", ""),tune.get("body", "")))
    conn.commit()
    conn.close()

```

4. Defining a function that takes file and book_number as parameters
- tunes stores the function process_file(file)
- tunes is then used to insert the tunes in the databasse

```Python
def process(file, book_number):
    tunes = process_file(file)
    inserting(book_number, tunes)
```

5. 
#### DB connection ctdb
- ctdb() is as short function that creates another conenction to the database tunes2.db

#### Loading tunes into the dataframe
- load_tunes_from_database() fetches the stored tunes and returns them as a pandas df for easy viewing, filtering and analysis

```Python
def ctdb():
    conn = sqlite3.connect('tunes2.db')
    return conn

def load_tunes_from_database():
    #variable conn holds the function ctdb
    conn = ctdb()
    #selecting all columns from tunes
    query = "SELECT * FROM tunes2"
    #creating a data from 
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df
```

6. df is used to store the function load_tunes_from_database()

7. 3 pandas functions are created to load the tune ddata from the datatbase into the pandas df and provide filtering

- get_tunes_by_book(df, book_number)
Returns all tunes from a specific book number.

- get_tune(df, tune_type)
Returns all tunes that match a given tune type (e.g., "Single jig").

- search(df, search_terms)
Searches for tunes whose titles contain a given keyword (case-insensitive).

```Python
def get_tunes_by_book(df, book_number):
    """Get all tunes from a specific book"""
    df = df[df["book_number"] ==  book_number]
    return df

#displays all the tunes from 3400 onwards as this is book2 (abc files)

def get_tunes_by_book(df, book_number):
    """Get all tunes from a specific book"""
    df = df[df["book_number"] ==  book_number]
    return df

#printing the title and key
book2_t = get_tunes_by_book(df, 2)
print(book2_t[["title","key"]].head())

#displays all the tunes from 3400 onwards as this is book2 (abc files)

def get_tune(df, tune_type):
    """Get the tune types"""
    df_2 = df[df["type"].str.lower() == tune_type.lower()] # FOR THE FUTURE, case = False wouldnt work fix later
    return df_2

#returning rthe title andd jig of a song
book3_t = get_tune(df, "Single jig")
print(book3_t[["title","type"]].head())


def search(df, search_terms):
    '''function to return the title of a song (used for tkinter)'''
    df_3 = df[df["title"].str.contains(search_terms, case = False)]
    return df_3
```



#### Matplot
- Created 2 graphs for further data analysis
- Graph 1: Shows number of tunes per book
- Graph 2; Shows the distribution of tune type and counts them
- value_counts() returns every row 

```Python
book_counts = df["book_number"].value_counts()

plt.figure(figsize=(8,5))
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

```

#### Tkinter
- Creating the tkinter function
- my_w = tk.Tk() creates the main window for the GUI
- my_w.geometry is used to alter the window size

```Python
#tkinter menu
def launch_gui(df):
    
    #main window
    my_w = tk.Tk()
    my_w.title("ABC Tune Database")
    
    my_w.geometry("750x600")
    #adding a text and scroll widget to the main box (my_W) -> acts as the root
    output = scrolledtext.ScrolledText(my_w, width=90, height=25)
    #pady is padding for the main window, moves it away from the top of the titlebar
    output.pack(pady=10)
```

#### Tkinter output
- Function that displays the data in the primary window
- output.delete(1.0, tk.END) clears all text in the box from start to the end 
- if the dataframe is empty/holds no values it outputs No results found
- loop designed to iterate through ever row and insert the string and row value at the end of the widget
```Python
    def show(df):
        #clears text box (1.0 is line1 char 0 tk.END _> to the end)
        output.delete(1.0, tk.END)
        
        if df.empty:
            #if the df has no rows/ data it displays no (#note for future tk.END is used to place no results at the end of widget)
            output.insert(tk.END, "No results found.\n")
            #returning no result to df
            return
        
        for i, row in df.iterrows():
            #outputting (printing) the rows in the main window
            output.insert(tk.END, f"Title: {row['title']}\n")
            
            output.insert(tk.END, f"Type: {row['type']}\n")
            
            output.insert(tk.END, f"Key: {row['key']}\n")
            
            output.insert(tk.END, f"Book: {row['book_number']}\n")
            
            #adding lines to seperate 
            output.insert(tk.END, "-"*50 + "\n")
```

#### Tkinter input/search
- Tk.Label is used to create a heading (like header is html)
- .pack() stacks this on top of the next widget
- book_entry is variable that stores tk.Entry which is a text box, the window is then passed into it as an argument to specify it being in that window
- tk.Button creates a search button that uses a temporary function (lambda) and runs the show function with the specific pandas function in it as an argument
- book_entry is used to retireve the input of the user -> df holds the data on what book numbers are in the data set
- get_tunes_by_book checks if teh booknumbers in the dataframe match the input of the user -> this is then inserted as a parameter into show function
- the show function then inseerts the data into the window according to the specified book number

```Python
    #search by book number
    #.pack is used to horiztonally or vertically place the widgets after another 
    #.pack() lets me stack the name and asearch bar on top of eachother
    
    tk.Label(my_w, text="Search by Book Number:", font=("Arial",10)).pack()
    
    #entry creates an input box 
    book_entry = tk.Entry(my_w)
    book_entry.pack()
    
    #creating a button, using lambda to create a mini function name (tkinter cant take calls) inserting the dataframe and using .get() to return the specified key
    #FOR FUTURE: user types into entry > when u click the button mini funcyion runs > returns number > get_tunes_by_book filters dataframe to book (1)or(2)
    
    tk.Button(my_w, text="Search", command=lambda:show(get_tunes_by_book(df, int(book_entry.get())))).pack()

    #search by tune type
    tk.Label(my_w, text="\nSearch by Type:").pack()
    type_entry = tk.Entry(my_w)
    
    type_entry.pack()
    tk.Button(my_w, text="Search", command=lambda: show(get_tune(df, type_entry.get()))).pack()

    # Search by title
    tk.Label(my_w, text="\nSearch by Title:").pack()
    title_entry = tk.Entry(my_w)
    title_entry.pack()
    tk.Button(my_w, text="Search", command=lambda: show(search(df, title_entry.get()))).pack()

```


# List of files in the project

| Files | Source |
|-----------|-----------|
| ashCode.py | Self written |


# References
* sqllite tutorial #1 [hyperlink](https://youtu.be/girsuXz0yA8?si=Ymqbg4gZFHoALtOB)
* tkinter tutorial #2 [hyperlink](https://youtu.be/w5JhFN0CwOE?si=ioK0tFfDjpQGgBNd)
* tkinter tutorial #3 [hyperlink](https://youtu.be/YXPyB4XeYLA?si=zruo8y0pNl_6rcrF)
* Codecademy #4 [hyperlink](https://www.codecademy.com)
* Lab5 DCP (parsing) 
* parsing tutorial #5 [hyperlink](https://youtu.be/1uA-pLITer0?si=g6Bh0RFy5-N8PrQO)
# What I am most proud of in the assignment

The thing im most proud of in this assignment are the parsing and pandas parts. For the parsing of the contents i looked back on old python files and labs i had used before, on top of this i used the skills i have been getting from codecademys Python 2 course and pandas course available on the website. Im proud that i could apply my knowledge and quickly get past these parts with little use of ai assistance, only to use it for finding errors, bad syntax or reccomendation. Another thing i am proud about is the developement of my tkinter gui. At first it was overwhelming but I was able to get a grasp on it quickly with the help of notes and youtube videos. Some of the commands look complicated but once you understand what they mean its easy to implement it into your code.

# What I learned

What i learned in this assignment is the connection of a database in which i created the table and columns using python. At first i struggled with this part alot as i struggled with this in php. However, after emailing my lecturer i was able to find the resources available to connect my file data to a sql table. I was not familiar with tkinter in the beggining but due to this assignment I was able to improve at my abilities in creating a GUI through the use of lecture notes, our previous lab and the use of youtube tutorials. 
