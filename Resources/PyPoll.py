# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Declare candidate list
candidate_options = []

# Create Candidate Dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add total vote count
        total_votes += 1
        
        # Print candidate name for each row
        candidate_name = row[2]
        
        # If Candidate name does not match existing options...
        if candidate_name not in candidate_options:
            # Add to candidate options
            candidate_options.append(candidate_name)

            # Begin tracking candidate's votes
            candidate_votes[candidate_name] = 0

        # Add Candidate's total votes
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping through the counts
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    # Calculate Percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # Print out each candidate's name, vote count, and percentage of total votes to terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes are greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # And set candidate_name = winning_candidate
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage}\n"
    f"-----------------------\n")
print(winning_candidate_summary)