import os
import csv

budget_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_csv) as csvFile:
    csvreader = csv.reader(csvFile, delimiter=",")

    csv_header = next(csvFile)

    # initialize total months
    totalMonths = 0

