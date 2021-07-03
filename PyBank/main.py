#!/usr/bin/env python
# coding: utf-8

# In[24]:


# Import dependencies
import os
import csv


# In[28]:


# Read and open the budget data csv file
file_path = 'Resources/budget_data.csv'
budget_csv = os.path.join(file_path)

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")    
    csv_header = next(csv_reader)
    
    # Initialize variables
    num_months = 0
    total = 0
    profit_loss = []
    great_inc_val = 0
    great_inc_date = []
    great_dec_val = 0
    great_dec_date = []
    
    # Loop through all rows in the budget data
    for row in csv_reader:
        num_months = num_months+1 # counting months
        date = row[0]
        PL_val = int(row[1]) # extract profit/loss value
        total = total + PL_val # sum profit/loss
        if PL_val > great_inc_val:
            great_inc_val = PL_val
            great_inc_date = date
        elif PL_val < great_dec_val:
            great_dec_val = PL_val
            great_dec_date = date
        else: continue
    PL_avg = round(total/num_months,2)
                           
    # Print out results
    print("FINANCIAL ANALYSIS")
    print("By: Jack Cohen")
    print("------------------------")
    print(f"Total Months: {num_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${PL_avg}")
    print(f"Greatest Increase in Profits: {great_inc_date} (${great_inc_val})")
    print(f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_val})")


# In[29]:


# Output results and analysis to .txt file
file1 = open("Analysis/Financial_Analysis.txt","w")
L = ["FINANCIAL ANALYSIS \n",
     "By: Jack Cohen \n",
     "------------------------\n",
     f"Total Months: {num_months}\n",
     f"Total: ${total} \n",
     f"Average Change: ${PL_avg} \n",
     f"Greatest Increase in Profits: {great_inc_date} (${great_inc_val}) \n",
     f"Greatest Decrease in Profits: {great_dec_date} (${great_dec_val}) \n"]
file1.writelines(L)
file1.close()


# In[ ]:




