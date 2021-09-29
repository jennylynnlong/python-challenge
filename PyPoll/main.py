import os
import csv

# path to collect data from Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# file to hold the output of the budget analysis
outputfile = os.path.join("electionResults.txt")

# variables
totalVotes = 0  # initialize total votes to 0
candidates = [] # initialize the list of candidates
candidateVotes = {}  # initialize dictionary of candidate votes
winningCount = 0    # initialize winning count to 0
winningCandidate = ""   # to hold winning candidate

# Read in the csv file
with open(election_csv, 'r') as csvFile:
    
    # Split the data on commas
    csvreader = csv.reader(csvFile, delimiter=",")

    # read header row
    csv_header = next(csvreader)
    
    # increment the count of the total votes
    totalVotes += 1

    for row in csvreader:
        # increment the count of the total months
        totalVotes += 1

        # check if candidates (in index[2]) is in candidates list
        if row[2] not in candidates:
            # add candidate to list if not there already
            candidates.append(row[2])

            # add the candidate to the dictionary as well; start the vote counts at 1
            candidateVotes[row[2]] = 1
        
        else:
            # if candidate is in list already, add vote to candidateVotes
            candidateVotes[row[2]] += 1

vote_output = ""

for candidates in candidateVotes:
        #get the vote count and percentage of the votes
        votes = candidateVotes.get(candidates)
        percentageVotes = (float(votes) / float(totalVotes)) *100

        vote_output += f"{candidates}: {percentageVotes:.3f}% ({votes}) \n"

        # compare votes to winning count
        if votes > winningCount:
            # udpate the winning count
            winningCount = votes
            # update winning candidate
            winningCandidate = candidates

# generating the output
output = (
    f"\nElection Results \n"
    f"------------------------- \n"
    f"Total Votes: {totalVotes} \n"
    f"------------------------- \n"
    f"{vote_output}"
    f"------------------------- \n"
    f"Winner: {winningCandidate}\n"
    f"------------------------- \n"
)

# print the output to the terminal
print(output)

# export the output variable to the text file
with open(outputfile, "w") as textfile:
    textfile.write(output)