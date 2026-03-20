import csv
import requests

with open("Task 2 - Intern.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        if row[0] == "urls":   # skip header
            continue
        url = row[0]   # first column has URL

        try:
            response = requests.get(url)
            status = response.status_code

            print("(" + str(status) + ") " + url)

        except:
            print("(ERROR) " + url)