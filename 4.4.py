import re

#file name
file_name = 'it_company.csv'

#function to read and write 5 next lines from the file
def display_5_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()#read the whole file
            #use regex to match each line
            lines = re.findall(r'.+', content)

            for i in range(0,len(lines), 5):
                for line in lines[i:i+5]:
                    print(line)
                    
                #wait until user presses enter
                if i + 5 < len(lines):
                    input("Press Enter to continue:")
                else:
                    print("End of file reached.")
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")

display_5_lines(file_name)
