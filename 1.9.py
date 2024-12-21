###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

count = 1

with open(file_name, 'r') as file:
   for line in file:
      if job_title in line:
        print(f"{count}. {line.strip()}")  # Print the numbered line
        count += 1