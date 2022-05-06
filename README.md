# Election_Analysis
Analyzing the elections results for a local congressional election in Colorado.

## Project Overview
A Colorado Board of Elections employee has given you the following task to complete the elecetion audit of a recent local congressional election:

1. Calculate the total number of votes cast.
2. Get a list of the counties in which votes were cast.
7. Calculate the total number of votes cast in each county.
8. Calculate the percentage of the total votes that came from each county.
9. Determine which county had the most votes.
3. Get a complete list of candidates who received votes.
4. Calculate the total number of votes each candidate received.
5. Calculate the percentage of votes each candidate won.
6. Determine the winner of the election based on popular vote.


# Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 votes cast

- The counties where votes were cast were:
    - Jefferson
    - Denver
    - Arapahoe

- The breakdown of votes in the counties were:
    - Jefferson County accounted for 38,855 votes which was 10.5% of the vote.
    - Denver County accounted for 306,055 vote which was 82.8% of the vote.
    - Arapahoe County accounted for 24,801 votes which was 6.7% of the vote.

- Denver had the largest voter turnout. 

- The candidates were:
    -  Charles Casper Stockham
    -  Diana DeGette
    -  Raymon Anthony Doane

- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
    - Diana DeGette received 73.8% of the vote and 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.

- The winner of the election was **Diana Degette** with 272,892 total votes (73.8% of the vote).

## Election Audit Summary
This script can be easily refactored in order to use it for any size or type of election with any number of candidates. You can also use this script in order to retreive other information on cities, voter's political parties, or where/how the vote was cast. If you wanted to get information on how votes were cast(mail in, in person, ect.), you would just need to collect that data, add it into the csv and add in new variables for the options as a list and votes cast using each option as a dictionary and modify/add the same formatted code to get the total number and percentages of votes casted using each method. 

