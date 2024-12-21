###
#Write a program that calculates the number of lines, 
# characters and words for any text file. 
# The user enters the name of the file from the keyboard.
# Use a try-except block to avoid interrupting your 
# program when the user enters a filename that doesn't exist. 
# Print the result of the calculation.

def count_file_stats(filename):
#Calculate the number of lines, words, and characters in the file.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            
            # Counting lines
            num_lines = len(lines)
            
            # Counting characters
            num_characters = sum(len(line) for line in lines)
            
            # Counting words
            num_words = sum(len(line.split()) for line in lines)
            
            return num_lines, num_words, num_characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None, None, None

def main():
    # Get the file name from the user
    filename = input("Enter the name of the file: ")
    
    # Calculate statistics
    num_lines, num_words, num_characters = count_file_stats(filename)
    
    # If the file exists, display the results
    if num_lines is not None:
        print(f"File name: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_characters}")

if __name__ == "__main__":
    main()
