# AshsProjects

A collection of university, personal, and upcoming projects focused on data science, artificial intelligence, machine learning, and software development.

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