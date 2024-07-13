import tkinter as tk

class AchievementsModule:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.create_achievements_screen()

    def create_achievements_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Achievements", font=("Arial", 20)).pack(pady=10)
        
        tk.Button(self.root, text="View Achievements", command=self.view_achievements).pack(pady=5)
        tk.Button(self.root, text="Milestones", command=self.view_milestones).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.return_callback).pack(pady=10)

    def view_achievements(self):
        self.clear_screen()
        tk.Label(self.root, text="Achievements", font=("Arial", 18)).pack(pady=10)
        # Code to display earned achievements
        tk.Button(self.root, text="Back", command=self.create_achievements_screen).pack(pady=10)

    def view_milestones(self):
        self.clear_screen()
        tk.Label(self.root, text="Milestones", font=("Arial", 18)).pack(pady=10)
        # Code to display possible achievements and criteria
        tk.Button(self.root, text="Back", command=self.create_achievements_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()