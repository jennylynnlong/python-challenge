import os
import csv

# path to collect data from Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# file to hold the output of the budget analysis
outputfile = os.path.join("electionResults.txt")

# variables
totalVotes = 0  # initialize total votes to 0
candidates = [] # initialize the list of candidates

# Read in the csv file
with open(election_csv, 'r') as csvFile:
    
    # Split the data on commas
    csvreader = csv.reader(csvFile, delimiter=",")

    # read header row
    csv_header = next(csvreader)
    # move to the first row
    firstRow = next(csvreader)

    # increment the count of the total votes
    totalVotes += 1

    for row in csvreader:
        # increment the count of the total months
        totalVotes += 1

# generating the output
output = (
    f"\nElection Results \n"
    f"------------------------- \n"
    f"Total Votes: {totalVotes} \n"
    f"------------------------- \n"
    f"Khan: \n"
    f"Correy: \n"
    f"Li: \n"
    f"O'Tooley: \n"
    f"------------------------- \n"
    f"Winner: \n"
    f"------------------------- \n"
)

# print the output to the terminal
print(output)

# export the output variable to the text file
with open(outputfile, "w") as textfile:
    textfile.write(output)