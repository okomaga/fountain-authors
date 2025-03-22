# Fountain Authors

This project extracts and aggregates the number of articles per author from Fountain Magazine and visualizes the results. The process is divided into three steps:

1. **Extraction**  
   The `extract_authors.py` script scrapes archive pages, extracts author names, and saves a raw list of authors to `authors_raw.csv`.

2. **Count and CSV**  
   The `count_authors.py` script reads `authors_raw.csv`, aggregates the number of articles per author using Python's `Counter`, and outputs the results to `author_counts.csv`.

3. **Plots: Bar Chart & Pie Chart**  
   The `plots_authors.py` script loads `author_counts.csv`, creates:
   - A bar chart for authors with 15 to 350 articles.
   - A pie chart comparing the total articles from top authors (15–350 articles) against authors with fewer than 15 articles.

## How It Works

### Extraction: `extract_authors.py`
- **Scraping Archive Pages:**  
  It collects archive URLs using a regular expression that matches `/archives/YYYY/MM` from the main archives page.
- **Extracting Authors:**  
  For each archive page, it parses the HTML with BeautifulSoup to extract author names from designated `<div>` elements.
- **Saving Data:**  
  The script writes the list of authors to `authors_raw.csv`.

### Counting: `count_authors.py`
- **Reading and Aggregating Data:**  
  This script reads the raw authors from `authors_raw.csv` and uses Python's `Counter` to compute the article counts per author.
- **Output:**  
  The aggregated data is saved to `author_counts.csv` for further processing.

### Plotting: `plots_authors.py`
- **Bar Chart:**  
  Filters authors with article counts between 15 and 350, then generates a bar chart with count labels on each bar.
- **Pie Chart:**  
  Creates a pie chart showing the percentage of articles from top authors (15–350 articles) vs. those with less than 15 articles.
- **Additional Information:**  
  The plot includes a summary text detailing total authors, total articles, and a breakdown of authors with less than 15 articles.

## How to Run

1. **Extraction:**  
   Run the extraction script:
   ```bash
   python extract_authors.py

	2.	Counting:
Run the counting script:

python count_authors.py


	3.	Plotting:
Run the plotting script:

python plots_authors.py


Ensure you have Python installed along with the required libraries: requests, beautifulsoup4, pandas, and matplotlib.

