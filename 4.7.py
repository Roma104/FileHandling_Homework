import re
### Write a program that calculates the number of vowels in the text entered from the keyboard. 
# Use regular expressions.

#!!! vovels -> SAMOGŁOSKI !!!
def count_vowels(text):
   #Calculate the number of vowels in the given text.
  
    # Define the pattern to match vowels (case-insensitive)
    pattern = r'[aeiouAEIOU]'
    
    # Find all matches for vowels
    vowels = re.findall(pattern, text)
    
    # Return the count of vowels
    return len(vowels)

def main():
    # Prompt the user to enter text
    text = input("Enter text: ")
    
    # Calculate the number of vowels
    num_vowels = count_vowels(text)
    
    # Display the result
    print(f"The text contains {num_vowels} vowels.")

if __name__ == "__main__":
    main()
