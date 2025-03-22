import pandas as pd
import matplotlib.pyplot as plt

# Data Loading
df = pd.read_csv("author_counts.csv")

# Filter authors with article count between 15 and 350 for the bar chart
df_filtered = df[(df['count'] >= 15) & (df['count'] <= 350)].copy()

# Optional: Sort authors by article count in descending order
df_filtered.sort_values('count', ascending=False, inplace=True)

# Plotting: Create the bar chart with author names on the x-axis
plt.figure(figsize=(12,6))
bars = plt.bar(df_filtered['author'], df_filtered['count'])
plt.xlabel('Authors')
plt.ylabel('Articles')
plt.title('The Fountain Magazine: Articles & Authors (Jan 1993 – Jan 2025)')
plt.xticks(rotation=45, ha='right')

# Add count labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{int(height)}', ha='center', va='bottom')

# Filter authors with less than 15 articles
df_rest = df[df['count'] < 15]

# Group the rest by article count and count number of authors in each group
grouped_rest = df_rest.groupby('count').size().reset_index(name='num_authors')

# Create summary text
summary_lines = []
for _, row in grouped_rest.iterrows():
    count = row['count']
    num_authors = row['num_authors']
    article_str = 'article' if count == 1 else 'articles'
    summary_lines.append(f"{num_authors} authors - {count} {article_str}")

summary_text = " | ".join(summary_lines)

# Compute total authors and total articles
total_authors = len(df)
total_articles = df['count'].sum()

# Adjust layout to allow space for the text below the plot
plt.tight_layout(rect=[0, 0.15, 1, 1])

# Combine summaries
combined_summary = f"Total Authors: {total_authors} | Total Articles: {total_articles}\nAuthors with less than 15 articles: " + summary_text
plt.figtext(0.5, 0.05, combined_summary, wrap=True, horizontalalignment='center', fontsize=10)

plt.savefig("authors_plot.png")
plt.show()

# Plotting: Create a pie chart showing percentage of articles from top authors (15-350) vs. others (<15)
top_authors_articles = df_filtered['count'].sum()
others_articles = df_rest['count'].sum()

labels = ['15 to 350', 'Less than 15']
sizes = [top_authors_articles, others_articles]
explode = (0.1, 0)  # Explode the slice for top authors

plt.figure(figsize=(8,8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, explode=explode)
plt.title('Percentage of Articles: Top 11 Authors (15–350 articles) vs. 1002 authors (<15 articles)')
plt.axis('equal')
plt.savefig("authors_pie_chart.png")
plt.show()