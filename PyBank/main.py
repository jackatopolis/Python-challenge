
# Dependencies
import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    print(csv_reader)