import os
import csv

# path to collect data from Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# file to hold the output of the budget analysis
outputfile = os.path.join("budgetAnalysis.txt")

# variables
totalMonths = 0     # initialize total months to 0
totalRevenue = 0    # initialize the total revenue to 0
monthlyChanges = [] # initialize the list of monthly changes
months = []         # initialize the list of months

# Read in the csv file
with open(budget_csv, 'r') as csvFile:
    
    # Split the data on commas
    csvreader = csv.reader(csvFile, delimiter=",")

    # read header row
    csv_header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment the count of the total months
    totalMonths += 1

    # add on to total amount of revenue (in index[1])
    totalRevenue += float(firstRow[1])

    # establish previous revenue for the month (in index[1])
    previousRevenue = float(firstRow[1])

    for row in csvreader:
        # increment the count of the total months
        totalMonths += 1

        # add on to total amount of revenue (in index[1])
        totalRevenue += float(row[1])

        # track the net change
        netChange = float(row[1]) - previousRevenue
        # add on to the list of monthly changes
        monthlyChanges.append(netChange)

        # add the first month (in index[0]) that a change occured
        months.append(row[0])

        # update previousRevenue
        previousRevenue = float(row[1])

# calculate average net change per month
averageNetChange = sum(monthlyChanges) / len(monthlyChanges)

greatestIncrease = [months[0], monthlyChanges[0]]   # holds the month and value of greatest increase
greatestDecrease = [months[0], monthlyChanges[0]]   # holds the month and value of greatest decrease

# use this loop to calculate the index of the greatest and least monthly change
for m in range(len(monthlyChanges)):
    # calculate the greatest increase
    if(monthlyChanges[m] > greatestIncrease[1]):
        # if the value is greater than the greatest increase, that value becomes new greatest increase
        greatestIncrease[1] = monthlyChanges[m]
        # update the month
        greatestIncrease[0] = months[m]
    
    # calculate the greatest decrease
    if(monthlyChanges[m] < greatestDecrease[1]):
        # if the value is greater than the greatest decrease, that value becomes new greatest decrease
        greatestDecrease[1] = monthlyChanges[m]
        # update the month
        greatestDecrease[0] = months[m]

# generating the output
output = (
    f"\nFinancial Analysis \n"
    f"--------------------------------- \n"
    f"Total Months: {totalMonths} \n"
    f"Total: ${totalRevenue:,.0f} \n"
    f"Average Change: ${averageNetChange:,.2f} \n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]:,.0f}) \n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]:,.0f})"
)

# print the output to the terminal
print(output)

# export the output variable to the text file
with open(outputfile, "w") as textfile:
    textfile.write(output)