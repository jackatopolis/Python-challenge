#!/usr/bin/env python
# coding: utf-8

# In[129]:


# Import Dependencies
import os
import csv


# In[135]:


# Read and open the budget data csv file
file_path = 'Resources/election_data.csv'
election_csv = os.path.join(file_path)
votes = []
winner_votes = 0

# Creating dictionary class
class voter_information(dict):
    def __init__(self):
        self = dict()
    def add(self, key, value):
        self[key]=value
        
# Open election data
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")    
    csv_header = next(csv_reader)
    
    # Initialize variables
    num_vote = 0
    votes_list = []
    candidates = []
    
    # Loop trought all rows in the election data
    for row in csv_reader:
        num_vote = num_vote+1 # counting votes
        candidate = row[2] # extract candidate
        votes.append(candidate)
        
        # Collect candidate names
        if candidate not in candidates:
            candidates.append(candidate)

# Start voter function from class
vote_func = voter_information()

print("ELECTION RESULTS\n"
      "By: Jack Cohen\n"
     "------------------------\n"
     f"Total Votes: {num_vote}\n"
     "------------------------")

# Loop through all votes to tally candidate totals and percents
for x in candidates:
    vote_func.add(x,{"Votes":votes.count(x),"Percent":round(100*(votes.count(x)/num_vote),3)})

# Loop through candidates to print results and find winner
for key in list(vote_func.keys()):
    print(f"{key}: {vote_func[key]['Percent']}% ({vote_func[key]['Votes']})")
    if vote_func[key]["Votes"] > winner_votes:
        winner_votes = vote_func[key]["Votes"]
        winner = key
print("------------------------\n"
      f"Winner: {winner}\n"
     "------------------------")


# In[136]:


# Output results and analysis to .txt file
file1 = open("Analysis/Election_Results.txt","w")
file1.write(("ELECTION RESULTS\n"
      "By: Jack Cohen\n"
     "------------------------\n"
     f"Total Votes: {num_vote}\n"
     "------------------------\n"))
for key in list(vote_func.keys()):
    file1.write(f"{key}: {vote_func[key]['Percent']}% ({vote_func[key]['Votes']})\n")
file1.write("------------------------\n"
      f"Winner: {winner}\n"
        "------------------------\n")
file1.close()


# In[ ]:




