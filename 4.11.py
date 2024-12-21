# Define the file name for saving the result
file_name = 'powers.txt'

def calculate_powers():
    
    # Open the file in write mode
    with open(file_name, 'w') as file:
        # Loop through numbers from 1 to 100
        for i in range(1, 101):
            second_power = i ** 2
            third_power = i ** 3
            # Create the result line
            result_line = f"{i},{second_power},{third_power}\n"
            # Print the result to the console
            print(result_line.strip())
            # Write the result to the file
            file.write(result_line)
    

# Call the function
calculate_powers()
