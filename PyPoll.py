# Add our dependencies.
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total votes count by setting an accumulator
total_votes = 0

candidate_options = []

#Create Dictionary for votes
candidate_votes = {}


#Open the election results and read the file.
with open(file_to_load) as election_data:


    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)
    
    #Print each row in the CSV file.
    for row in file_reader:

        #Add to the total vote count
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #check if candidate name matches any existing candidates
        if candidate_name not in candidate_options:

        #add candidate name to the candidate list
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Iterate through the candidate list.
for candidate_name in candidate_votes:

    #Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

    #Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    print(f'{candidate_name}: recieved {vote_percentage:.1f}% of the vote.')





# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.