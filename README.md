# Election_Analysis

## Overview of Project

We were tasked with auditing the results of an election in the US Congressional Precinct in Colorado and reporting the results.  While this task is usually done in Excel, the goal of our project was to write a Python script that would automate the process for future elections.

## Election Audit Results

- How many votes were cast in this congressional election?
    * The election data was given to us in a CSV file where each row was a record of a vote.  To count the total number of votes cast, we created a `for loop` that incremented a variable set to zero by one for each row in the file.  The code block looked like this:
    ~~~
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
    ~~~
    The total number of votes cast were 369,711
    
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   * To determine the number and percentage of votes for each county, we had to include an `if statement` that would first compile all instances of a unique county name into our `county_options` list and then increment the total votes tally for each county in the  `county_votes` dictionary by one for each row.  This was accomplished by adding the following `if statement` inside our `for loop`:
   ~~~
   # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
   ~~~
   Once we had the number of votes for each county, we calculated the share of the total vote by each county:  `cvotes_percentage = float(cvotes) / float(total_votes) * 100`.
   The percentage (and number) of votes by county were as follows: Jefferson: 10.5% (38,855); Denver: 82.8% (306,055); Arapahoe: 6.7% (24,801).

- Which county had the largest number of votes?
   * Denver had the largest number of votes.

- Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
   * To calculate the number of votes and percentage of total votes for each candidate, the process was quite similar to the one above.  We first had to use an `if statement` within a `for loop` to get the unique instances of a candidate's name and then add a count of each row for a particular candidate.  The following block of code accomplished this:
   ~~~
   # If the candidate does not match any existing candidate add it to
           # the candidate list
           if candidate_name not in candidate_options:

               # Add the candidate name to the candidate list.
               candidate_options.append(candidate_name)

               # And begin tracking that candidate's voter count.
               candidate_votes[candidate_name] = 0

           # Add a vote to that candidate's count
           candidate_votes[candidate_name] += 1
   ~~~
   We could then calculate the percentage of the total vote each candidate had with the following: `vote_percentage = float(votes) / float(total_votes) * 100`.  These were the results: Charles Casper Stockham: 23.0% (85,213); Diana DeGette: 73.8% (272,892); Raymon Anthony Doane: 3.1% (11,606).

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   * The winner was Diana DeGette.  Her vote count was 272,892 and her percentage of the vote was 73.8%.

## Election Audit Summary

As long as the CSV files that hold the data for future elections retains the same format, each row is a single vote, the second column (index 1) is the county, and the third column (index 2) is the candidate, then this script will be able to perform the same analysis in future elections.  The user will only need to modify the `file_to_load` variable to represent the file with the election data and add a repository within their working directory to hold an election analysis text file.
