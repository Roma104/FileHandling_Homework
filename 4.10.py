###
#The clothing.csv contains a list of clothing in stock. 
# Write a program that prints those products whose price 
# is less than 60 and whose stock is less than 40.

import re

# Define the file name
file_name = 'clothing.csv'

def filter_clothing(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            print("Products with Price < 60 and Stock < 40")
            print("=======================================")
            
            # Skip the header and process each line
            for line in content[1:]:
                # Use regex to extract relevant fields
                match = re.match(r'^(\d+),([^,]+),[^,]+,[^,]+,[^,]+,(\d+\.\d+),(\d+)$', line.strip())
                if match:
                    _, product_name, price, stock_quantity = match.groups()
                    price = float(price)
                    stock_quantity = int(stock_quantity)
                    
                    # Apply conditions: Price < 60 and Stock < 40
                    if price < 60 and stock_quantity < 40:
                        print(f"{product_name} - Price: {price}, Stock: {stock_quantity}")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
filter_clothing(file_name)
