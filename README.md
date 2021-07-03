# Python-challenge
### By: Jack Cohen

## PyBank

#### Purpose
The purpose of this python script (main.py) is to analyze the financial records for a company. The code loops through a bank's profit loss data (Resources/budget_data.csv) to extract, analyze, and document the meaningful insights. The script runs through each line of the .csv file and outputs to a .txt file the following:
1. Total number of months in the dataset
2. Net profit/loss over all months
3. Average profit/loss for each month
4. Greatest increase in profits and its corresponding date
5. Greatest decrease in profits and its corresponding date

#### Assumptions
1. Imported file has date in the first column and profit/loss value in dollars in the second column
2. Dates do not have to be chronological; the code will work in any order

## PyPoll

#### Purpose
The purpose of this python script (main.py) is to help a small, rural town modernize its vote counting process. The code loops through election data (Resources/election_data.csv) to extract, analyze, and document the meaningful insights. The script runs through each line of the .csv file and outputs to a .txt file the following:
1. Total number of votes cast
2. Complete list of candidates who received votes
3. Percentage of votes each candidate won
4. Total number of votes each candidate won
5. Winner of the election based on popular vote

#### Assumptions
1. Imported file has data in the first two columns (data not used in this analysis, but still needs to have two columns) and then candidate name in the third column
2. Data does not have to be ordered; the code will work in any order