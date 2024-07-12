import tkinter as tk
from modules import library, reading_list, goals, achievements

class ShelfControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ShelfControl")
        self.home_screen()
  
    def home_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="ShelfControl", font=("Arial", 24)).pack(pady=20) 
            
        tk.Button(self.root, text="Library", command=self.open_library).pack(pady=10)
        tk.Button(self.root, text="Reading List", command=self.open_reading_list).pack(pady=10)
        tk.Button(self.root, text="Goals", command=self.open_goals).pack(pady=10)
        tk.Button(self.root, text="Achievements", command=self.open_achievements).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def open_library(self):
        self.clear_screen()
        library.LibraryModule(self.root, self.home_screen)

    def open_reading_list(self):
        self.clear_screen()
        reading_list.ReadingListModule(self.root, self.home_screen)

    def open_goals(self):
        self.clear_screen()
        goals.GoalsModule(self.root, self.home_screen)

    def open_achievements(self):
        self.clear_screen()
        achievements.AchievementsModule(self.root, self.home_screen)

root = tk.Tk()
app = ShelfControlApp(root)
root.mainloop()