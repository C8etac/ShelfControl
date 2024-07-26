# Reading List Module
# Responsible for displaying and managing the reading list
import tkinter as tk

class ReadingListModule:
    def __init__(self, root, return_callback):
        self.root = root # Main application window
        self.return_callback = return_callback # Callback to return to the home screen
        self.create_reading_list_screen() # Display the reading list screen

    # Displays the main screen for the reading list module
    def create_reading_list_screen(self):
        self.clear_screen() # Clear any existing widgets

        # Displaying the title of the Reading List module
        tk.Label(self.root, text="Reading List", bg="black", fg="khaki", font=("Arial", 20)).pack(pady=10)
        
        # Adding buttons to navigate between different lists
        tk.Button(self.root, text="To Be Read (TBR) List", bg = "midnightblue", fg = "khaki", command=self.show_tbr_list).pack(pady=5)
        tk.Button(self.root, text="Reading List", bg = "midnightblue", fg = "khaki", command=self.show_reading_list).pack(pady=5)
        tk.Button(self.root, text="Read List", bg = "midnightblue", fg = "khaki", command=self.show_finished_list).pack(pady=5)
        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.return_callback).pack(pady=10)

    # Displays the list of books to be read
    def show_tbr_list(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="To Be Read (TBR) List", bg = "black", fg = "khaki", font=("Arial", 18)).pack(pady=10)
        
        # Reading the list of books from the file and displaying those marked as "To Be Read"
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if len(book_details) == 5 and book_details[4] == "To Be Read":
                        tk.Label(self.root, bg = "black", fg = "khaki", text=f"Title: {book_details[0]}, Author: {book_details[1]}").pack()
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.").pack()

        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.create_reading_list_screen).pack(pady=10)

    # Displays the list of books currently being read
    def show_reading_list(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Reading List", bg = "black", fg = "khaki", font=("Arial", 18)).pack(pady=10)
        
        # Reading the list of books from the file and displaying those marked as "Reading"
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if len(book_details) == 5 and book_details[4] == "Reading":
                        tk.Label(self.root, bg = "black", fg = "khaki", text=f"Title: {book_details[0]}, Author: {book_details[1]}").pack()
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.").pack()

        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.create_reading_list_screen).pack(pady=10)

    # Displays the list of books that have been read
    def show_finished_list(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Read List", bg = "black", fg = "khaki", font=("Arial", 18)).pack(pady=10)
        
        # Reading the list of books from the file and displaying those marked as "Read"
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if len(book_details) == 5 and book_details[4] == "Read":
                        tk.Label(self.root, bg = "black", fg = "khaki", text=f"Title: {book_details[0]}, Author: {book_details[1]}").pack()
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.").pack()

        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.create_reading_list_screen).pack(pady=10)

    # Clears all widgets from the current screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy() # Destroy each widget
