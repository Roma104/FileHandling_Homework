###
# Reads the entire contents of a file
#

def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

#splits words into array parts
file_content = read_from_file('pets.txt')
file_lines = file_content.split()

#print(file_lines)

#counts words
counter = 0

for line in file_lines:
   counter += 1


print('Total words:', counter)