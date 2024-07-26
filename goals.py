# Goals Module
# Responsible for setting and tracking reading goals
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class GoalsModule:
    def __init__(self, root, return_callback):
        self.root = root # Main application window
        self.return_callback = return_callback # Callback to return to the home screen
        self.create_goals_screen() # Display the goals screen

    # Displays the main screen for the goals module
    def create_goals_screen(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Goals", bg="black", fg="khaki", font=("Arial", 20)).pack(pady=10)
        
        # Adding buttons to navigate to different functionalities within the goals module
        buttons = [
            ("Set Yearly Goal", self.set_yearly_goal),
            ("Set Monthly Goal", self.set_monthly_goal),
            ("Track Progress", self.track_progress),
            ("Back", self.return_callback)
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, bg="midnightblue", fg="khaki", command=command).pack(pady=5)

    # Displays the screen to set a yearly reading goal
    def set_yearly_goal(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Set Yearly Goal", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
        # Creating entry fields for the yearly goal
        tk.Label(self.root, text="Number of Books:", bg="black", fg="khaki").pack()
        self.yearly_goal_entry = tk.Entry(self.root) # Entry field for number of books
        self.yearly_goal_entry.pack()

        tk.Label(self.root, text="Year (YYYY):", bg="black", fg="khaki").pack()
        self.year_entry = tk.Entry(self.root) # Entry field for year
        self.year_entry.pack()

        # Adding buttons to save the goal and go back to the goals screen
        tk.Button(self.root, text="Set Goal", bg="midnightblue", fg="khaki", command=self.save_yearly_goal).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_goals_screen).pack(pady=10)

    # Saves the yearly reading goal
    def save_yearly_goal(self):

        # Retrieving input values
        num_books = self.yearly_goal_entry.get() # Getting the number of books
        year = self.year_entry.get() # Getting the year

        # Validating input fields
        if not num_books or not year:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            year = int(year) # Converting year to integer
            num_books = int(num_books) # Converting number of books to integer
        except ValueError:
            messagebox.showerror("Error", "Invalid input! Year and number of books should be integers.")
            return

        goal_details = f"Yearly,{year},{num_books}\n" # Formatting goal details
        
        # Saving goal details to file
        try:
            with open("reading_goals.txt", "a") as file:
                file.write(goal_details)
            messagebox.showinfo("Success", "Yearly goal set successfully!")
            self.create_goals_screen()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save goal: {e}")

    # Displays the screen to set a monthly reading goal
    def set_monthly_goal(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Set Monthly Goal", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
        # Creating entry fields for the monthly goal
        tk.Label(self.root, text="Number of Books:", bg="black", fg="khaki").pack()
        self.monthly_goal_entry = tk.Entry(self.root) # Entry field for number of books
        self.monthly_goal_entry.pack()

        tk.Label(self.root, text="Month (MM-YYYY):", bg="black", fg="khaki").pack()
        self.month_entry = tk.Entry(self.root) # Entry field for month
        self.month_entry.pack()

        # Adding buttons to save the goal and go back to the goals screen
        tk.Button(self.root, text="Set Goal", bg="midnightblue", fg="khaki", command=self.save_monthly_goal).pack(pady=10)
        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_goals_screen).pack(pady=10)

    # Saves the monthly reading goal
    def save_monthly_goal(self):

        # Retrieving input values
        num_books = self.monthly_goal_entry.get() # Getting the number of books
        month_year = self.month_entry.get() # Getting the month

        # Validating input fields
        if not num_books or not month_year:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            datetime.strptime(month_year, "%m-%Y") # Validating month format
            num_books = int(num_books) # Converting number of books to integer
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use MM-YYYY and ensure number of books is an integer.")
            return

        goal_details = f"Monthly,{month_year},{num_books}\n" # Formatting goal details
        
        # Saving goal details to file
        try:
            with open("reading_goals.txt", "a") as file:
                file.write(goal_details)
            messagebox.showinfo("Success", "Monthly goal set successfully!")
            self.create_goals_screen()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save goal: {e}")

    # Displays the progress towards reading goals
    def track_progress(self):
        self.clear_screen() # Clear any existing widgets

        tk.Label(self.root, text="Track Progress", bg="black", fg="khaki", font=("Arial", 18)).pack(pady=10)
        
        # Loading goals and book counts
        yearly_goals, monthly_goals = self.load_goals()
        book_counts = self.count_books()

        # Displaying the progress towards goals
        if not yearly_goals and not monthly_goals:
            tk.Label(self.root, text="No goals found.", bg="black", fg="khaki").pack()
        else:
            if yearly_goals:
                for year, num_books in yearly_goals.items():
                    tk.Label(self.root, text=f"Yearly Goal - Year: {year}, Books: {num_books}, Progress: {book_counts['Read']}", bg="black", fg="khaki").pack()
            
            if monthly_goals:
                for month_year, num_books in monthly_goals.items():
                    tk.Label(self.root, text=f"Monthly Goal - Month: {month_year}, Books: {num_books}, Progress: {book_counts['Read']}", bg="black", fg="khaki").pack()

        tk.Button(self.root, text="Back", bg="midnightblue", fg="khaki", command=self.create_goals_screen).pack(pady=10)

    # Loads yearly and monthly goals from the file
    def load_goals(self):
        yearly_goals = {} # Dictionary to hold yearly goals
        monthly_goals = {} # Dictionary to hold monthly goals
        try:
            with open("reading_goals.txt", "r") as file:
                goals = file.readlines() # Reading all lines from the file
                for goal in goals:
                    goal_details = goal.strip().split(",") # Splitting each line into details
                    if goal_details[0] == "Yearly":
                        yearly_goals[goal_details[1]] = int(goal_details[2])
                    else:
                        monthly_goals[goal_details[1]] = int(goal_details[2])
        except FileNotFoundError:
            pass
        return yearly_goals, monthly_goals

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
