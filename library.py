import tkinter as tk
from tkinter import messagebox

class LibraryModule:
    def __init__(self, root, return_callback):
        self.root = root
        self.return_callback = return_callback
        self.create_library_screen()

    def create_library_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Library", font=("Arial", 20)).pack(pady=10)
        
        tk.Button(self.root, text="Add New Book", command=self.add_new_book).pack(pady=5)
        tk.Button(self.root, text="View Library", command=self.view_library).pack(pady=5)
        tk.Button(self.root, text="Search Books", command=self.search_books).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.return_callback).pack(pady=10)

    def add_new_book(self):
        self.clear_screen()
        tk.Label(self.root, text="Add New Book", font=("Arial", 18)).pack(pady=10)
        
        tk.Label(self.root, text="Title:").pack()
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        tk.Label(self.root, text="Author:").pack()
        self.author_entry = tk.Entry(self.root)
        self.author_entry.pack()

        tk.Label(self.root, text="Genre:").pack()
        self.genre_entry = tk.Entry(self.root)
        self.genre_entry.pack()

        tk.Label(self.root, text="Series:").pack()
        self.series_entry = tk.Entry(self.root)
        self.series_entry.pack()

        tk.Label(self.root, text="Status:").pack()
        self.status_entry = tk.Entry(self.root)
        self.status_entry.pack()

        tk.Button(self.root, text="Add Book", command=self.save_book).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_library_screen).pack(pady=10)

    def save_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        series = self.series_entry.get()
        status = self.status_entry.get()

        if not title or not author or not genre or not status:
            messagebox.showerror("Error", "All fields except series are required!")
            return

        book_details = f"{title},{author},{genre},{series},{status}\n"
        
        try:
            with open("library_books.txt", "a") as file:
                file.write(book_details)
            messagebox.showinfo("Success", "Book added successfully!")
            self.create_library_screen()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save book: {e}")

    def view_library(self):
        self.clear_screen()
        tk.Label(self.root, text="Library Catalog", font=("Arial", 18)).pack(pady=10)

        try:
            with open("library_books.txt", "r") as file:
                books = file.readlines()
                for book in books:
                    book_details = book.strip().split(",")
                    book_info = f"Title: {book_details[0]}, Author: {book_details[1]}, Genre: {book_details[2]}, Series: {book_details[3]}, Status: {book_details[4]}"
                    tk.Label(self.root, text=book_info).pack()
        except FileNotFoundError:
            tk.Label(self.root, text="No books found.").pack()

        tk.Button(self.root, text="Back", command=self.create_library_screen).pack(pady=10)

    def search_books(self):
        self.clear_screen()
        tk.Label(self.root, text="Search Books", font=("Arial", 18)).pack(pady=10)
        # Code to search for specific books
        tk.Button(self.root, text="Back", command=self.create_library_screen).pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()