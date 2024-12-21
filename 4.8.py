###
#The files.txt contains a list of file names. 
# Write a program that prints only those file names whose extensions consist of exactly four characters (e.g. .html).

import re

# File name containing the list of file names
file_name = 'files.txt'

# Regular expression pattern to match file names with extensions of exactly four characters
pattern = r'\.\w{4}'

try:
    # Open and read the file
    with open(file_name, 'r') as file:
        print("Files with extensions of exactly four characters:")
        for line in file:
            line = line.strip()  # Remove whitespace or newline characters
            if re.search(pattern, line):
                print(line)
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
