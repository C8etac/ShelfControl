"""
Author: Catelynn Barfell
Date written: 06/25/2024
Assignment: Module 08 Final Project
Short Desc: Shelf control is a book management system that allows users to manage their library, create reading lists, set and track goals, and achieve reading milestones.
"""

import tkinter as tk
from modules import library, reading_list, goals, achievements
from PIL import Image, ImageTk  

# Main application class for the ShelfControl system
class ShelfControlApp:
    def __init__(self, root):
        self.root = root # Main application window
        self.root.title("ShelfControl") # Setting the title of the main window
        self.root.configure(bg="black")  # Setting the background color to black
        self.home_screen() # Displaying the home screen

    #  Displays the home screen with navigation buttons to different modules
    def home_screen(self):
        self.clear_screen() # Clear any existing widgets
        
        # Displaying the main image on top of the screen
        self.img1 = ImageTk.PhotoImage(Image.open("ShelfControl.jpg")) 
        tk.Label(self.root, image=self.img1, bg="black").pack(pady=5)
        
        # Adding buttons for navigation
        tk.Button(self.root, text="Library", bg = "midnightblue", fg = "khaki", command=self.open_library).pack(pady=10)
        tk.Button(self.root, text="Reading List", bg = "midnightblue", fg = "khaki", command=self.open_reading_list).pack(pady=10)
        tk.Button(self.root, text="Goals", bg = "midnightblue", fg = "khaki", command=self.open_goals).pack(pady=10)
        tk.Button(self.root, text="Achievements", bg = "midnightblue", fg = "khaki", command=self.open_achievements).pack(pady=10)
        tk.Button(self.root, text="Exit", bg = "midnightblue", fg = "khaki", command=self.root.quit).pack(pady=10)

    # Clears all widgets from the current screen
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy() # Destroy each widget

    #  Opens the Library module
    def open_library(self):
        self.clear_screen() # Clear the current screen
        library.LibraryModule(self.root, self.home_screen) # Initialize the Library module

    # Opens the Reading List module
    def open_reading_list(self):
        self.clear_screen() # Clear the current screen
        reading_list.ReadingListModule(self.root, self.home_screen) # Initialize the Reading List module

    # Opens the Goals module
    def open_goals(self):
        self.clear_screen() # Clear the current screen
        goals.GoalsModule(self.root, self.home_screen) # Initialize the Goals module

    # Opens the Achievements module
    def open_achievements(self):
        self.clear_screen() # Clear the current screen
        achievements.AchievementsModule(self.root, self.home_screen) # Initialize the Achievements module

# Main loop to start the application
root = tk.Tk() # Create the main window
app = ShelfControlApp(root) # Initialize the ShelfControl application
root.mainloop() # Run the main event loop
