# Election_Analysis

## Overview of Project

We were tasked with auditting the results of an election in the US Congressional Precint in Colorado and reporting the results.  While this task is usually done in Excel, the goal of our project was to write a Python script that would automate the process for future elections.

## Election Audit Results

- How many votes were cast in this congressional election?
    * The election data was given to us in a csv file where each row was a record of a vote.  To count the total number of votes cast, we created a `for loop` that added incremented a variable set to zero by one for each row in the file.  The code block looked like this:
    ~~~
    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
    ~~~
