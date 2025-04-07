# 📚 Fountain Authors

A 3-part Python project that extracts, analyzes, and visualizes author activity from [The Fountain Magazine](https://fountainmagazine.com).

This tool scrapes author names from the magazine archive, counts the number of published articles per author, and generates simple visual summaries. The project is designed to demonstrate data pipeline construction (scraping → cleaning → aggregation → visualization) using real-world data.

---

## 🧠 Summary

- 🔎 **Extracts** author data from magazine archives using web scraping (BeautifulSoup + regex)  
- 📊 **Counts** the number of articles per author using Python's built-in `Counter`  
- 📈 **Visualizes** the results with:
  - A bar chart of authors with 15–350 articles  
  - A pie chart showing the proportion of articles from frequent vs. infrequent contributors  

---

## 🛠️ Required Packages

Install all required packages with:

```bash
pip install pandas matplotlib requests bs4
```
---

## 🔧 The Process (3 Steps)

### 1. Extraction — `extract_authors.py`
- Scrapes archive URLs from the magazine’s archive page (regex-based)
- Extracts author names from each monthly archive page using BeautifulSoup
- Saves raw author data to `authors_raw.csv`

### 2. Counting — `count_authors.py`
- Reads the raw author list from `authors_raw.csv`
- Aggregates article counts per author using Python’s `Counter`
- Saves result to `author_counts.csv`

### 3. Visualization — `plots_authors.py`
- Loads `author_counts.csv`
- Filters authors with 15–350 articles
- Generates:
  - 📊 Bar chart with article counts  
  - 🥧 Pie chart comparing top contributors (15–350) to those with <15 articles
- Adds summary stats to the plot (total authors, article breakdown)

---

## 🧪 Sample Use Case

This project is useful for:

- Practicing data pipeline creation  
- Exploring real publishing data from a media source  
- Building visualizations for reporting or exploratory analysis  
- Gaining hands-on experience in web scraping, aggregation, and matplotlib plotting

---

## 📁 Output Files

- `authors_raw.csv` — list of all extracted authors  
- `author_counts.csv` — article counts per author  
- `bar_chart.png`, `pie_chart.png` — visual summaries

---

## 📬 Contact

If you’re hiring for roles in data analysis, research, or media analytics — or want to chat about Fountain-format scripting, I’m open to collaboration.
