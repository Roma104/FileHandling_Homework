# Define genre to filename mapping
GENRE_TO_FILE = {
    'Fantasy': 'books_fantasy.txt',
    'Historical': 'books_historical.txt',
    'Romance': 'books_romance.txt',
    'Classic': 'books_classic.txt'
}

# Function to read books from the CSV file 
def read_books_from_csv(filename):
    books = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Skip the header line
            next(file)
            # Read each line, split by commas, and create a dictionary for each book
            for line in file:
                data = line.strip().split(',')
                book = {
                    'Title': data[0],
                    'Author': data[1],
                    'Genre': data[2],
                    'Year': data[3]
                }
                books.append(book)
    except FileNotFoundError:
        print("The file was not found.")
    return books

# Function to filter books by genre
def filter_books_by_genre(books, genre):
    return [book for book in books if book['Genre'] == genre]

# Function to save filtered books to a file
def save_books_to_file(books, filename):
    
    with open(filename, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['Title']},{book['Author']},{book['Year']}\n")
    

# Main function to execute the program
def process_books():
    books = read_books_from_csv('books.csv')
    if not books:
        return
    
    # Iterate through each genre in the mapping and process accordingly
    for genre, file_name in GENRE_TO_FILE.items():
        filtered_books = filter_books_by_genre(books, genre)
        if filtered_books:
            save_books_to_file(filtered_books, file_name)
            print(f"Books from the genre '{genre}' have been saved to {file_name}.")
        else:
            print(f"No books found for the genre '{genre}'.")

# Execute the program
process_books()
