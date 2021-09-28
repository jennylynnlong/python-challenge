import os
import csv

# path to collect data from Resources folder
budget_csv = os.path.join("..", "Resources", "budget_data.csv")

# variables
totalMonths = 0 # initialize total months to 0

# Define the function
def financial_analysis(budget_csv):

    # month is at index 0, profit/losses at index 1
    month = budget_csv[0]
    profit_loss = int(budget_csv[1])

    # find total months



    # print analysis
    print("Financial Analysis")
    print("------------------------------")
    print(f"")

# Read in the csv file
with open(budget_csv, 'r') as csvFile:
    
    # Split the data on commas
    csvreader = csv.reader(csvFile, delimiter=",")

    # read header row
    csv_header = next(csvreader)

   

