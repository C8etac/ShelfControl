# Achievements Module
# Responsible for displaying and tracking reading achievements
import tkinter as tk
from tkinter import messagebox

class AchievementsModule:
    def __init__(self, root, return_callback):
        self.root = root # Main application window
        self.return_callback = return_callback # Callback to return to the home screen
        self.create_achievements_screen() # Display the achievements screen

    #  Displays the main screen for the achievements module
    def create_achievements_screen(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Achievements",  bg="black", fg="khaki", font=("Arial", 20)).pack(pady=10)
        
        # Adding buttons to navigate to different functionalities within the achievements module
        tk.Button(self.root, text="View Achievements", bg = "midnightblue", fg = "khaki", command=self.view_achievements).pack(pady=5)
        tk.Button(self.root, text="Milestones", bg = "midnightblue", fg = "khaki", command=self.view_milestones).pack(pady=5)
        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.return_callback).pack(pady=10)

    # Displays the list of earned achievements
    def view_achievements(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Achievements",  bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
         # Tracking and displaying achievements
        achievements = self.track_achievements()
        if not achievements:
            tk.Label(self.root, text="No achievements found.", bg="black", fg="khaki").pack()
        else:
            for achievement in achievements:
                tk.Label(self.root, text=achievement, bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.create_achievements_screen).pack(pady=10)

    # Displays the list of reading milestones
    def view_milestones(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Milestones",  bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
        # Defining and displaying milestones
        milestones = [
            "Read 1 book",
            "Read 5 books",
            "Read 10 books",
            "Complete a series",
            "Read a book from each genre",
            "Read your first Fiction book",
            "Read your first Non-Fiction book",
            "Read your first Science Fiction book",
            "Read your first Fantasy book",
            "Read your first Mystery book",
            "Read your first Biography book",
            "Read your first History book",
            "Read your first Horror book",
            "Read your first Romance book",
            "Read your first Thriller book",
            "Read your first Young Adult book"
        ]
        
        for milestone in milestones:
            tk.Label(self.root, bg="black", fg="khaki", text=milestone).pack()

        tk.Button(self.root, text="Back", bg = "midnightblue", fg = "khaki", command=self.create_achievements_screen).pack(pady=10)

    def track_achievements(self):
        book_counts = self.count_books() # Counting the number of books in each status category
        genres = set() # Set to hold unique genres
        series = set() # Set to hold unique series
        genre_achievements = set() # Set to hold achieved genres
        achievements = [] # List to hold achievements

        # Adding achievements based on the number of books read
        if book_counts['Read'] >= 1:
            achievements.append("Read 1 book")
        if book_counts['Read'] >= 5:
            achievements.append("Read 5 books")
        if book_counts['Read'] >= 10:
            achievements.append("Read 10 books")

        specified_genres = ["Fiction", "Non-Fiction", "Science Fiction", "Fantasy", "Mystery", "Biography", "History", "Horror", "Romance", "Thriller", "Young Adult"]
        
        # Tracking genres and series
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if len(book_details) == 5:
                        genre = book_details[2]
                        series_name = book_details[3]
                        if book_details[4] == "Read":
                            genres.add(genre)
                            if series_name:
                                series.add(series_name)
                            if genre in specified_genres and genre not in genre_achievements:
                                genre_achievements.add(genre)
                                achievements.append(f"Read your first {genre} book")
        except FileNotFoundError:
            pass

        # Adding achievements based on the number of genres and series completed
        if len(series) > 0:
            achievements.append("Complete a series")
        if len(genres) >= 5:
            achievements.append("Read a book from each genre")

        return achievements

    # Counts the number of books in each status category
    def count_books(self):
        book_counts = {"To Be Read": 0, "Reading": 0, "Read": 0} # Dictionary to hold book counts
        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines() # Reading all lines from the file
                for book in books:
                    book_details = book.strip().split(",") # Splitting each line into details
                    if len(book_details) == 5:
                        status = book_details[4]
                        if status in book_counts:
                            book_counts[status] += 1
        except FileNotFoundError:
            pass
        return book_counts

    # Clears all widgets from the current screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy() # Destroy each widget
