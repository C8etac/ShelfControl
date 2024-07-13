import tkinter as tk

class ReadingListModule:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.create_reading_list_screen()

    def create_reading_list_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Reading List", font=("Arial", 20)).pack(pady=10)
        
        tk.Button(self.root, text="To Be Read (TBR) List", command=self.show_tbr_list).pack(pady=5)
        tk.Button(self.root, text="Reading List", command=self.show_reading_list).pack(pady=5)
        tk.Button(self.root, text="Finished List", command=self.show_finished_list).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.return_callback).pack(pady=10)

    def show_tbr_list(self):
        self.clear_screen()
        tk.Label(self.root, text="To Be Read (TBR) List", font=("Arial", 18)).pack(pady=10)
        # Code to display TBR list
        tk.Button(self.root, text="Back", command=self.create_reading_list_screen).pack(pady=10)

    def show_reading_list(self):
        self.clear_screen()
        tk.Label(self.root, text="Reading List", font=("Arial", 18)).pack(pady=10)
        # Code to display currently reading list
        tk.Button(self.root, text="Back", command=self.create_reading_list_screen).pack(pady=10)

    def show_finished_list(self):
        self.clear_screen()
        tk.Label(self.root, text="Finished List", font=("Arial", 18)).pack(pady=10)
        # Code to display finished books list
        tk.Button(self.root, text="Back", command=self.create_reading_list_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()