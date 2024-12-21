###
# Reads the entire contents of a file
#The file car_park.txt contains data on the number of parked cars for the last five days.
#Complete the following program to calculate the total number of parked cars.
#

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

# reads the entire file and splits lines into array
file_content = read_from_file('car_park.txt')
file_lines = file_content.splitlines()

# calculates the total number of cars parked
total = 0
for line in file_lines:
   total += int(line)

print('Total cars parked:', line)