import csv
import requests

# open the CSV file
with open("Task 2 - Intern.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "urls":   # skip header
            continue

        url = row[0]

        try:
            response = requests.get(url, timeout=5)   # added timeout
            status = response.status_code

            print(f"({status}) {url}")

        except requests.exceptions.RequestException:
            print(f"(ERROR) {url}")
