from operator import index
import os

import csv


csvpath = os.path.join('Resources', 'election_data.csv')
output = '''Election Results
-------------------------
Total Votes: '''
'''369711
 -------------------------
  Charles Casper Stockham: 23.049% (85213)
  Diana DeGette: 73.812% (272892)
  Raymon Anthony Doane: 3.139% (11606)
 -------------------------
  Winner: Diana DeGette
  -------------------------
  '''
with open(csvpath, encoding= 'utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    next(csvreader)
    
    total_votes = []
    candidates_votes = ()

    
    for line in csvreader:
        total_votes.append(line[2])
total_count = len(total_votes)
output = output + str(total_count) + "\n" + "-------------------------" + "\n"
candidates = list(set(total_votes))
count_votes_candidate_wise = []
percentage = []

for candidate in candidates:
    count_votes_candidate_wise.append(total_votes.count(candidate))
print(candidates)
print(count_votes_candidate_wise)

for i in range (len(candidates)):
    percentage = count_votes_candidate_wise[i]/total_count*100
    output = output + f'{candidates[i]}: {round(percentage,3)}% ({count_votes_candidate_wise[i]}) \n'

index_of_winner = count_votes_candidate_wise.index(max(count_votes_candidate_wise))
output = output + f"-------------------------\nWinner: {candidates[index_of_winner]}\n-------------------------"   
print(output)

print(output)
csvpath = os.path.join('Analysis', 'Polling_Analysis.txt')
with open(csvpath,'w') as textfile:
    textfile.write(output)