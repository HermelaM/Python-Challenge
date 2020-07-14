import os
import csv

# variables and store data
count = 0
candidates = []
unique_candidate = []
vote_count = []
vote_percent = []

# Set csv path 
csvpath = os.path.join("Resources","election_data.csv")

# open and read csv file 

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # read each row
    for row in csvreader:

        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidates
        candidates.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
        
    for x in set(candidates):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidates.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
# print analysis
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# open new file  

with open('election_results.txt', 'w') as text:
    # write new dara

    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
