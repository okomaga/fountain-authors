# Fountain Authors

This project extracts and aggregates the number of articles per author from [Fountain Magazine Archives](https://fountainmagazine.com/archives). The script scrapes multiple archive pages, extracts author names (with entries containing "Fountain" re-labeled as "Fountain Editors"), and then aggregates the results to show how many articles each author has contributed.

## How It Works

1. **Scraping Archive Pages:**  
   The script gathers all archive URLs from the main archives page using a regular expression to match the `/archives/YYYY/MM` pattern.

2. **Extracting Authors:**  
   For each archive page, it uses BeautifulSoup to parse the HTML and extract author names from specific `<div>` elements. If an author name contains "Fountain", it is changed to "Fountain Editors".

3. **Aggregating Results:**  
   The script then counts the number of articles per author using Python's `Counter` and prints a table.

## How to Run

Make sure you have Python installed along with the required libraries (`requests`, `beautifulsoup4`). Then run:

```bash
python3 extract_authors.py
