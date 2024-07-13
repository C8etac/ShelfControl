import tkinter as tk

class GoalsModule:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.create_goals_screen()

    def create_goals_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Goals", font=("Arial", 20)).pack(pady=10)
        
        tk.Button(self.root, text="Set Goals", command=self.set_goals).pack(pady=5)
        tk.Button(self.root, text="Track Progress", command=self.track_progress).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.return_callback).pack(pady=10)

    def set_goals(self):
        self.clear_screen()
        tk.Label(self.root, text="Set Goals", font=("Arial", 18)).pack(pady=10)
        
        tk.Label(self.root, text="Book Title:").pack()
        self.book_title_entry = tk.Entry(self.root)
        self.book_title_entry.pack()

        tk.Label(self.root, text="Deadline (YYYY-MM-DD):").pack()
        self.deadline_entry = tk.Entry(self.root)
        self.deadline_entry.pack()

        tk.Button(self.root, text="Set Goal", command=self.save_goal).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_goals_screen).pack(pady=10)

    def save_goal(self):
        book_title = self.book_title_entry.get()
        deadline = self.deadline_entry.get()

        if not book_title or not deadline:
            tk.messagebox.showerror("Error", "All fields are required!")
            return

        # Here, you would save the goal to a database or file
        tk.messagebox.showinfo("Success", "Goal set successfully!")
        self.create_goals_screen()

    def track_progress(self):
        self.clear_screen()
        tk.Label(self.root, text="Track Progress", font=("Arial", 18)).pack(pady=10)
        # Code to display current goals and progress
        tk.Button(self.root, text="Back", command=self.create_goals_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
