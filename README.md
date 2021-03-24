# Election_Analysis

## Overview of Project

We were tasked with auditting the results of an election in the US Congressional Precint in Colorado and reporting the results.  While this task is usually done in Excel, the goal of our project was to write a Python script that would automate the process for future elections.

## Election Audit Results

- How many votes were cast in this congressional election?
    * The election data was given to us in a CSV file where each row was a record of a vote.  To count the total number of votes cast, we created a `for loop` that added incremented a variable set to zero by one for each row in the file.  The code block looked like this:
    ~~~
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
    ~~~
    The total number of votes cast were 369,711
    
- Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
   * To determine the number and percentage of votes for each county, we had to include an `if statement` that would first compile all intances of a unique county name into our `county_options` list and then increment the the total votes tally for each county in the  `county_votes` dictionary by one for each row.  This was accomplished by adding the following `if statement` inside our `for loop`:
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
   * To calulate the number of votes and percentage of total votes for each candidate, the process was quite similar to the one above.  We first had to use an `if statement` within a `for loop` to get the unique instances of a candidate's name and then add a count of each row for a particular candidate.  The following block of code accomplished this:
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
   We could then calulate the percentage of the total vote each candidate had with the following: `vote_percentage = float(votes) / float(total_votes) * 100`.  These were the results: Charles Casper Stockham: 23.0% (85,213); Diana DeGette: 73.8% (272,892); Raymon Anthony Doane: 3.1% (11,606).

- Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
   * The winner was Diana DeGette.  Her vote count was 272,892 and her percentage of the vote was 73.8%.
