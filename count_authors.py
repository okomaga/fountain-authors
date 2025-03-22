import csv
from collections import Counter

def main():
    # Read authors from authors.csv
    with open("authors.csv", "r", encoding="utf-8") as infile:
        reader = csv.reader(infile)
        authors = [row[0] for row in reader if row]

    # Count frequency of each author
    counts = Counter(authors)

    # Write the counts to author_counts.csv with headers
    with open("author_counts.csv", "w", newline="", encoding="utf-8") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["author", "count"])
        for author, count in counts.items():
            writer.writerow([author, count])

    print("Author counts saved to author_counts.csv")

if __name__ == "__main__":
    main()