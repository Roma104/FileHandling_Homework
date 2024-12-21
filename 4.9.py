import re

# Define the file name
file_name = 'it_company.csv'

def extract_graphic_designers(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            
            # Extract the header to find column indices
            header = content[0].strip()
            columns = header.split(',')
            
            # Find indices of required columns
            first_name_idx = columns.index('First Name')
            last_name_idx = columns.index('Last Name')
            job_title_idx = columns.index('Job Title')
            email_idx = columns.index('Email')
            
            print("GRAPHIC DESIGNERS")
            print("=================")
            
            # Process the remaining lines
            for line in content[1:]:
                fields = re.split(r',(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)', line.strip())  # Handles CSV fields with commas inside quotes
                if fields[job_title_idx] == 'Graphic Designer':
                    first_name = fields[first_name_idx]
                    last_name = fields[last_name_idx]
                    email = fields[email_idx]
                    print(f"{first_name} {last_name},{email}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    

# Call the function
extract_graphic_designers(file_name)
