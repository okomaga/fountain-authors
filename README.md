# Fountain Authors

This project extracts and aggregates the number of articles per author from [Fountain Magazine](https://fountainmagazine.com/archives). The script scrapes multiple archive pages, extracts author names (with entries containing "Fountain" re-labeled as "Fountain Editors"), and then aggregates the results to show how many articles each author has contributed.

## How It Works

1. **Scraping Archive Pages:**  
   The script gathers all archive URLs from the main archives page using a regular expression to match the `/archives/YYYY/MM` pattern.

2. **Extracting Authors:**  
   For each archive page, it uses BeautifulSoup to parse the HTML and extract author names from specific `<div>` elements. If an author name contains "Fountain", it is changed to "Fountain Editors".

3. **Aggregating Results:**  
   The script then counts the number of articles per author using Python's `Counter` and prints a table.

## How to Run

Make sure you have Python installed along with the required libraries (`requests`, `beautifulsoup4`). Then run code.py

# Summary of Author Contributions

This summary shows the distribution of how many articles each author contributed. The numbers below were calculated by grouping authors based on the number of articles they wrote and then computing the percentage of the total authors.

**Steps to Compute:**
1. **Group** the aggregated counts by the number of articles per author.
2. **Count** the number of authors in each group (e.g., how many authors wrote exactly 1 article, exactly 2 articles, etc.).
3. **Calculate** the percentage for each group relative to the total number of authors.

**Example Summary Table:**

| Articles Written | Number of Authors | Percentage (%) |
|------------------|-------------------|----------------|
| 1                | 150               | 60%            |
| 2                | 50                | 20%            |
| 3                | 25                | 10%            |
| 4                | 10                | 4%             |
| 5 or more        | 15                | 6%             |
| **Total**        | 250               | 100%           |

*Note: The numbers above are for illustration only. Replace them with the actual values calculated from your data.*

# Fountain Authors - Aggregated Article Counts

| Author                         | Articles |
|--------------------------------|----------|
| M. Fethullah Gulen             | 350      |
| Fountain Editors               | 323      |
| Hikmet Isik                    | 72       |
| Irfan Yilmaz                   | 48       |
| Bediuzzaman Said Nursi         | 34       |
| Seth Mette                     | 33       |
| Jay Willoughby                 | 20       |
| Lawrence Brazier               | 19       |
| Alphonse Dougan                | 18       |
| Ali Fethi Toprak               | 16       |
| Mirkena Ozer                   | 15       |
| Hakan Oztunc                   | 13       |
| Mustafa Tabanli                | 13       |
| Ali Unal                       | 13       |
| Naim Yilmaz                    | 12       |
| Numan Erciyes                  | 12       |
| Hamza Aydin                    | 12       |
| Osman Cakmak                   | 12       |
| Ceyda Sablak                   | 10       |
| Dr. Ibrahim B. Syed            | 10       |
| Justin Pahl                    | 10       |
| Safiye Arslan                  | 10       |
| Omer Arifagaoglu               | 10       |
|--------------------------------|----------|
| *... (Additional authors and counts follow)* | |
