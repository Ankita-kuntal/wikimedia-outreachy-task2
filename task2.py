import csv
import requests

with open("Task 2 - Intern.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "urls":
            continue

        url = row[0]

        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            print(f"({response.status_code}) {url}")

        except requests.exceptions.RequestException:
            print(f"(ERROR) {url}")
