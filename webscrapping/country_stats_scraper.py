import numpy as np
from bs4 import BeautifulSoup
import requests

# url = https://www.scrapethissite.com/pages/simple/
print("=" * 65)
print("COUNTRY STATISTICS SCRAPER")
print("=" * 65)

url = 'https://www.scrapethissite.com/pages/simple/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Educational Scraper - DATA2005 Lab)'
}
response = requests.get(url, headers = headers, timeout= 15)


if response.ok:
    print(f"URL: {response.url}")
    print(f"Status {response.status_code}")
    print(f"Content Length: {len(response.text):,} characters")
else:
    print(f"Failed to connect: {response.status_code} exit (1)")
    
    
soup = BeautifulSoup(response.text, "lxml")
title = print(f"Title: {soup.title.text.strip()}")

"""
===============================================================================
TASK 1: Explore the Page Structure (5 minutes)
===============================================================================
Before extracting data, you need to understand the HTML structure.

Instructions:
1. Find all country containers on the page
2. Print how many countries are listed
3. Examine the structure of one country entry

Hints:
- Use browser DevTools or soup.prettify() to see structure
- Look for repeating div elements with class names
- The data includes: name, capital, population, area
"""

print("\n--- TASK 1: Explore Page Structure ---\n")

# YOUR CODE HERE

countries = soup.find(id ="countries")
each_country = countries.find_all('h3', class_ = 'country-name')

print(f"The number of countries are: {len(each_country)}")
print("")
#print(countries.prettify())

# Find the container with country data
# Hint: Look for divs with class 'country'
"""
===============================================================================
TASK 2: Extract Country Data (15 minutes)
===============================================================================
Extract all country information into a structured format.

Instructions:
1. Loop through all country elements
2. Extract: name, capital, population, area
3. Store in a list of dictionaries
4. Handle missing data gracefully

Expected output format:
{
    'name': 'Ireland',
    'capital': 'Dublin',
    'population': 4622917,
    'area': 70273.0
}
"""
country_info = soup.find_all("div", class_ = "country")
country_data = []
for country in country_info:
    country_data.append({
        'name': country.find("h3", class_ = "country-name").text.strip(),
        'capital': country.find("span", class_ = "country-capital").text.strip(),
        'population': int(country.find("span", class_ = "country-population").text.strip()),
        'area': float(country.find("span", class_ = "country-area").text.strip())
        
        
        
    })


print("\n--- TASK 2: Extract Country Data ---\n")


print(f"Extracted data for {len(country_data)} countries")
print("\nSample entries:")
for entry in country_data[:5]:
    print(f"  {entry['name']}: Pop={entry['population']:,}, Area={entry['area']:,.0f} km²")


"""
===============================================================================
TASK 3: NumPy Analysis (10 minutes)
===============================================================================
Perform statistical analysis on the extracted data using NumPy.

Instructions:
1. Convert population and area to NumPy arrays
2. Calculate: mean, median, std, min, max for each
3. Calculate population density (pop/area) for each country
4. Find top 5 most populous countries
5. Find top 5 largest countries by area
"""

print("\n--- TASK 3: NumPy Analysis ---\n")

# YOUR CODE HERE

npPop = np.array([r['population']for r in country_data])
npArea = np.array([r['area']for r in country_data])
npName= np.array([r['name']for r in country_data])

populationMean = np.mean(npPop)
populationMax = np.max(npPop)
populationMin = np.min(npPop)
populationSTD = np.std(npPop)

areaMean = np.mean(npArea)
areaMax = np.max(npArea)
areaMin = np.min(npArea)
areaSTD = np.std(npArea)

for country in country_data:
    area = float(country['area'])
    population = int(country['population'])
    
    if area != 0:
        country['density'] = population/area
        
    else:
        country['density'] = None
    
print(country_data[:5])
        
top5 = sorted(country_data, key = lambda country: int(country['population']), reverse = True)[:5]
top5area = sorted(country_data, key = lambda country: float(country['area']), reverse = True)[:5]


print("\nTop 5 Most Populous Countries:")
for country in top5:
    print(f"{country['name']}: {country['population']:,}")
    
print("\nTop 5 Largest Countries by Area:")
for country in top5area:
    print(f"{country['name']}: {country['area']:,.0f} km²")
print("\n" + "=" * 65)
print("CHALLENGE COMPLETE!")
print("=" * 65)


print("\n--- Skills Demonstrated ---")
print("  ✓ HTTP requests with error handling")
print("  ✓ HTML parsing with Beautiful Soup")
print("  ✓ Data extraction from structured elements")
print("  ✓ NumPy statistical analysis")
