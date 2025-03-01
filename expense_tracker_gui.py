import tkinter as tk
from tkinter import ttk, messagebox
import csv
import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

# Colors
BG_COLOR = "#06a3d2"  # Light Blue
BTN_COLOR = "#3af7ff"  # Blue
TEXT_COLOR = "#f3e4d9"  # Green

# Function to add an expense
def add_expense():
    date = datetime.date.today().strftime("%Y-%m-%d")
    category = category_var.get()
    amount = amount_var.get()

    if not category or not amount:
        messagebox.showerror("Error", "Please enter category and amount.")
        return

    try:
        amount = float(amount)
        with open(FILE_NAME, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])
        messagebox.showinfo("Success", "Expense added successfully!")
        amount_var.set("")
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")

# Function to view all expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            expenses_list.delete(*expenses_list.get_children())  # Clear table
            for row in reader:
                expenses_list.insert("", "end", values=row)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No expenses recorded yet.")

# Function to show category summary
def category_summary():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            category_totals = {}
            for row in reader:
                category_totals[row[1]] = category_totals.get(row[1], 0) + float(row[2])

            summary_text = "\n".join(f"{cat}: ₹{amt}" for cat, amt in category_totals.items())
            messagebox.showinfo("Category Summary", summary_text)
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No expenses recorded yet.")

# Main Window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("500x450")
root.configure(bg=BG_COLOR)

# Title
tk.Label(root, text="Expense Tracker", font=("Arial", 20, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=10)

# Entry Frame
frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=5)

tk.Label(frame, text="Category:", font=("Arial", 12), bg=BG_COLOR).grid(row=0, column=0, padx=5, pady=5)
category_var = tk.StringVar()
category_entry = ttk.Entry(frame, textvariable=category_var, width=20)
category_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Amount (₹):", font=("Arial", 12), bg=BG_COLOR).grid(row=1, column=0, padx=5, pady=5)
amount_var = tk.StringVar()
amount_entry = ttk.Entry(frame, textvariable=amount_var, width=20)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=10)

btn_style = {"font": ("Arial", 12, "bold"), "bg": BTN_COLOR, "fg": "white", "width": 15, "bd": 2}

tk.Button(btn_frame, text="Add Expense", command=add_expense, **btn_style).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View Expenses", command=view_expenses, **btn_style).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Category Summary", command=category_summary, **btn_style).grid(row=1, column=0, columnspan=2, padx=5, pady=5)

# Expense List (Table)
columns = ("Date", "Category", "Amount")
expenses_list = ttk.Treeview(root, columns=columns, show="headings")
expenses_list.heading("Date", text="Date")
expenses_list.heading("Category", text="Category")
expenses_list.heading("Amount", text="Amount (₹)")
expenses_list.pack(pady=10)

# Run the App
root.mainloop()
