# PollPy.py

# Add our dependencies.

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join('resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)





# Using the with statement open the file to save as a text file.
# with open(file_to_save, 'w') as txt_file:

    # Write some data to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")


# 1. The total number of votes cast

# 2. A list of condidates who recieved votes

# 3. The percentage of votes each candidate won

# 4. The total number of votes each cadidate won

# 5. The winner of the election based on popular vote