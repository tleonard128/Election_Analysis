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

#Winning Candidate and Winning Count Tracker
winning_candidate = ""

winning_count = 0

winning_percentage = 0

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

#Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    election_results = (

        f"\nElectionResults\n"

        f"---------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"---------------------\n")

    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Iterate through the candidate list.
    for candidate_name in candidate_votes:

        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]

        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print out each candidate's name, vote count and percentage of votes
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")
        
        #Print the candidate_results
        print(candidate_results)

        #Write the candidate results to the txt file
        txt_file.write(candidate_results)

        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # 2. If true then set winning_count = votes and winning_percentage = 
            #vote_percentage.
            winning_count = votes

            winning_percentage = vote_percentage

            winning_candidate = candidate_name


        # Print out the winning candidate, vote count, and percentage
    winning_candidate_summary = (
        f"------------------------\n"

        f"Winner: {winning_candidate}\n"

        f"Winning Vote Count: {winning_count:,}\n"

        f"Winning Percentage: {winning_percentage: .1f}%\n"

        f"--------------------------\n")

    print(winning_candidate_summary)

    #Save the winning candidates name to the text fil
    txt_file.write(winning_candidate_summary)
            



