###
# Reads a non-existent file
#

# there is no file with this name on the disk
file_name = 'xyz.txt'

try:
    with open(file_name) as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print(f'The file {file_name} does not exist')
