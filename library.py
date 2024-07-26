# Library Module
# Responsible for managing the user's library, including adding new books, viewing the book shelf, and changing book statuses
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 

class LibraryModule:
    def __init__(self, root, return_callback):
        self.root = root # Main application window
        self.return_callback = return_callback # Callback to return to the home screen
        self.create_library_screen() # Display the library screen

    # Displays the main screen for the library module
    def create_library_screen(self):
        self.clear_screen() # Clear any existing widgets

        # Displaying the title of the Library module
        tk.Label(self.root, text="Library", bg="black", fg="khaki", font=("Arial", 20)).pack(pady=10)
        
        # Adding buttons to navigate to different functionalities within the library module
        tk.Button(self.root, text="Add New Book", bg="midnightblue", fg="khaki", command=self.add_new_book).pack(pady=5)
        tk.Button(self.root, text="BookShelf", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=5)
        tk.Button(self.root, text="Change Book Status", bg="midnightblue", fg="khaki", command=self.change_book_status).pack(pady=5)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.return_callback).pack(pady=10)

        # Display image at the bottom of the screen
        self.image = ImageTk.PhotoImage(Image.open("shelf.jpg"))
        self.image_label = tk.Label(self.root, image=self.image, bg="black")
        self.image_label.pack(side="bottom", pady=10)

    # Displays the screen to add a new book to the library
    def add_new_book(self):
        self.clear_screen() # Clear any existing widgets
        tk.Label(self.root, text="Add New Book", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
        # Creating entry fields for book details
        tk.Label(self.root, text="Title:", bg="black", fg="khaki").pack()
        self.title_entry = tk.Entry(self.root) # Entry field for book title
        self.title_entry.pack()

        tk.Label(self.root, text="Author:", bg="black", fg="khaki").pack()
        self.author_entry = tk.Entry(self.root) # Entry field for book author
        self.author_entry.pack()

        tk.Label(self.root, text="Genre:", bg="black", fg="khaki").pack()
        self.genre_var = tk.StringVar(self.root) # Variable to hold selected genre
        self.genre_var.set("Select Genre")  # Default option for genre dropdown
        genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Biography", "History", "Horror", "Romance", "Thriller", "Young Adult"]
        self.genre_menu = tk.OptionMenu(self.root, self.genre_var, *genres) # Dropdown menu for genres
        self.genre_menu.pack()

        tk.Label(self.root, text="Series:", bg="black", fg="khaki").pack()
        self.series_entry = tk.Entry(self.root) # Entry field for series name
        self.series_entry.pack()

        tk.Label(self.root, text="Status:", bg="black", fg="khaki").pack()
        self.status_var = tk.StringVar(self.root) # Variable to hold selected status
        self.status_var.set("Select Status")  # Default option for status dropdown
        statuses = ["To Be Read", "Reading", "Read"]
        self.status_menu = tk.OptionMenu(self.root, self.status_var, *statuses) # Dropdown menu for status
        self.status_menu.pack()

        # Adding buttons to save the book and go back to the library screen
        tk.Button(self.root, text="Add Book", bg="midnightblue", fg="khaki", command=self.save_book).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_library_screen).pack(pady=10)

    # Saves a new book to the library
    def save_book(self):

        # Retrieving input values
        title = self.title_entry.get()  # Getting the book title
        author = self.author_entry.get()  # Getting the book author
        genre = self.genre_var.get()  # Getting the selected genre
        series = self.series_entry.get()  # Getting the series name
        status = self.status_var.get()  # Getting the selected status

        # Validating input fields
        if not title or not author or genre == "Select Genre" or status == "Select Status":
            messagebox.showerror("Error", "All fields except series are required!")
            return

        book_details = f"{title},{author},{genre},{series},{status}\n" # Formatting book details
        
        # Saving book details to file
        try:
            with open("library_books.txt", "a") as file:
                file.write(book_details)
            messagebox.showinfo("Success", "Book added successfully!")
            self.create_library_screen()
        # Error handling for file operation failures
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save book: {e}")

    # Displays the library bookshelf and allows filtering by various criteria
    def view_library(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="BookShelf", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Adding buttons for different filtering options
        tk.Button(self.root, text="All Books", bg="midnightblue", fg="khaki", command=self.display_all_books).pack(pady=5)
        tk.Button(self.root, text="Search by Title", bg="midnightblue", fg="khaki", command=self.filter_by_title).pack(pady=5)
        tk.Button(self.root, text="Search by Author", bg="midnightblue", fg="khaki", command=self.filter_by_author).pack(pady=5)
        tk.Button(self.root, text="Search by Series", bg="midnightblue", fg="khaki", command=self.filter_by_series).pack(pady=5)
        tk.Button(self.root, text="Search by Genre", bg="midnightblue", fg="khaki", command=self.filter_by_genre).pack(pady=5)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_library_screen).pack(pady=10)

        # Adding the image at the bottom of the screen
        self.image = ImageTk.PhotoImage(Image.open("shelf.jpg"))
        self.image_label = tk.Label(self.root, image=self.image, bg="black")
        self.image_label.pack(side="bottom", pady=10)

    # Displays all books in the library
    def display_all_books(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="BookShelf - All Books", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Reading and displaying all books from the file
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                    tk.Label(self.root, text=book_info, bg="black", fg="khaki").pack()
        # # Error handling for missing file
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=10)

    # Filter books by title
    def filter_by_title(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Search by Title", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Book Title:", bg="black", fg="khaki").pack()
        self.title_entry = tk.Entry(self.root) # Entry field for book title
        self.title_entry.pack()

        # Adding buttons to search and go back to the library screen
        tk.Button(self.root, text="Search", bg="midnightblue", fg="khaki", command=self.display_filtered_books_by_title).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=10)

    # Displays books filtered by the entered title
    def display_filtered_books_by_title(self):
        book_title = self.title_entry.get().strip().lower() # Getting the entered book title
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text=f"BookShelf - Title: {book_title.title()}", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Reading and displaying books matching the entered title
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                found_books = False # Flag to check if any book is found
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if book_details[0].strip().lower() == book_title:
                        found_books = True
                        book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                        tk.Label(self.root, text=book_info, bg="black", fg="khaki").pack()
                if not found_books:
                    tk.Label(self.root, text="No books found with this title.", bg="black", fg="khaki").pack()
        # # Error handling for missing file
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.filter_by_title).pack(pady=10)

    # Filters books by author
    def filter_by_author(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Search by Author", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Author Name:", bg="black", fg="khaki").pack()
        self.author_entry = tk.Entry(self.root) # Entry field for author name
        self.author_entry.pack()

        # Adding buttons to search and go back to the library screen
        tk.Button(self.root, text="Search", bg="midnightblue", fg="khaki", command=self.display_filtered_books_by_author).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=10)

    # Displays books filtered by the entered author
    def display_filtered_books_by_author(self):
        author_name = self.author_entry.get().strip().lower() # Getting the entered author name
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text=f"BookShelf - Author: {author_name.title()}", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Reading and displaying books matching the entered author
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                found_books = False # Flag to check if any book is found
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if book_details[1].strip().lower() == author_name:
                        found_books = True
                        book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                        tk.Label(self.root, text=book_info, bg="black", fg="khaki").pack()
                if not found_books:
                    tk.Label(self.root, text="No books found by this author.", bg="black", fg="khaki").pack()
        # Error handling for missing file
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.filter_by_author).pack(pady=10)

    #  Filters books by series
    def filter_by_series(self):
        self.clear_screen() # Clear any existing widgets
        
        tk.Label(self.root, text="Search by Series", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Series Name:", bg="black", fg="khaki").pack() 
        self.series_entry = tk.Entry(self.root) # Entry field for series name
        self.series_entry.pack()

        # Adding buttons to search and go back to the library screen
        tk.Button(self.root, text="Search", bg="midnightblue", fg="khaki", command=self.display_filtered_books_by_series).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=10)

    # Displays books filtered by the entered series
    def display_filtered_books_by_series(self):
        series_name = self.series_entry.get().strip().lower()  # Getting the entered series name
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text=f"BookShelf - Series: {series_name.title()}", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Reading and displaying books matching the entered series
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                found_books = False # Flag to check if any book is found
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if book_details[3].strip().lower() == series_name:
                        found_books = True
                        book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                        tk.Label(self.root, text=book_info, bg="black", fg="khaki").pack()
                if not found_books:
                    tk.Label(self.root, text="No books found in this series.", bg="black", fg="khaki").pack()
        # Error handling for missing file
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.filter_by_series).pack(pady=10)

    # Filters books by genre
    def filter_by_genre(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Search by Genre", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Genre:", bg="black", fg="khaki").pack()
        self.genre_var = tk.StringVar(self.root) # Variable to hold selected genre
        self.genre_var.set("Select Genre")  # Default option for genre dropdown
        genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Biography", "History", "Horror", "Romance", "Thriller", "Young Adult"]
        self.genre_menu = tk.OptionMenu(self.root, self.genre_var, *genres) # Dropdown menu for genres
        self.genre_menu.pack()

        # Adding buttons to search and go back to the library screen
        tk.Button(self.root, text="Search", bg="midnightblue", fg="khaki", command=self.display_filtered_books_by_genre).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.view_library).pack(pady=10)

    # Displays books filtered by the selected genre
    def display_filtered_books_by_genre(self):
        genre = self.genre_var.get().strip().lower() # Getting the selected genre
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text=f"BookShelf - Genre: {genre.title()}", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Reading and displaying books matching the selected genre
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                found_books = False # Flag to check if any book is found
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if book_details[2].strip().lower() == genre:
                        found_books = True
                        book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                        tk.Label(self.root, text=book_info, bg="black", fg="khaki").pack()
                if not found_books:
                    tk.Label(self.root, text="No books found in this genre.", bg="black", fg="khaki").pack()
        # Error handling for missing file
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.filter_by_genre).pack(pady=10)

    # Displays the screen to change the status of a book
    def change_book_status(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Change Book Status", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)

        # Creating entry fields for book title and new status
        tk.Label(self.root, text="Book Title:", bg="black", fg="khaki").pack()
        self.book_title_entry = tk.Entry(self.root) # Entry field for book title
        self.book_title_entry.pack()

        tk.Label(self.root, text="New Status:", bg="black", fg="khaki").pack()
        self.new_status_var = tk.StringVar(self.root) # Variable to hold selected status
        self.new_status_var.set("Select Status") # Default option for status dropdown 
        statuses = ["To Be Read", "Reading", "Read"]
        self.new_status_menu = tk.OptionMenu(self.root, self.new_status_var, *statuses) # Dropdown menu for status
        self.new_status_menu.pack()

        # Adding buttons to update the status and go back to the library screen
        tk.Button(self.root, text="Update Status", bg="midnightblue", fg="khaki", command=self.update_book_status).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_library_screen).pack(pady=10)

    # Updates the status of a book in the library
    def update_book_status(self):

        # Retrieving input values
        title = self.book_title_entry.get() # Getting the book title
        new_status = self.new_status_var.get() # Getting the selected new status

        # Validating input fields
        if not title or new_status == "Select Status":
            messagebox.showerror("Error", "All fields are required!")
            return

        # Reading and updating the book status in the file
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file

            updated_books = [] # List to hold updated book details
            found = False # Flag to check if the book is found
            for book in books:
                book_details = book.strip().split(",") # Splitting each line into details
                if book_details[0].lower() == title.lower():
                    book_details[4] = new_status # Updating the status
                    found = True
                updated_books.append(",".join(book_details) + "\n")

            if found:
                with open("library_books.txt", "w") as file:
                    file.writelines(updated_books) # Writing updated book details to the file
                messagebox.showinfo("Success", "Book status updated successfully!")
            else:
                messagebox.showerror("Error", "Book not found!")

            self.create_library_screen()
        # Error handling for missing file
        except FileNotFoundError:
            messagebox.showerror("Error", "Library file not found!")

        # Error handling for file operation failures
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update book status: {e}")

    # Clears all widgets from the current screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy() # Destroy each widget
