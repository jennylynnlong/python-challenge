import os
import csv

# path to collect data from Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# file to hold the output of the budget analysis
outputfile = os.path.join("budgetAnalysis.txt")

# variables
totalMonths = 0 # initialize total months to 0

# Read in the csv file
with open(budget_csv, 'r') as csvFile:
    
    # Split the data on commas
    csvreader = csv.reader(csvFile, delimiter=",")

    # read header row
    csv_header = next(csvreader)

    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1

# start generating the output
output = (
    f"\nFinancial Analysis \n"
    f"--------------------------------- \n"
    f"Total Months: {totalMonths}"
)

# print the output to the terminal
print(output)

# export the output variable to the text file
with open(outputfile, "w") as textfile:
    textfile.write(output)