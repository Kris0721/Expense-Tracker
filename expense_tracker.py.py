import csv
import datetime

# File to store expenses
FILE_NAME = "expense.csv"

# Function to add an expense
def add_expense():
    date = datetime.date.today().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("Expense added successfully!")

# Function to view total expenses
def view_expenses():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            total = 0
            print("\nDate       | Category  | Amount")
            print("-" * 30)
            for row in reader:
                print(f"{row[0]:10} | {row[1]:8} | ₹{row[2]}")
                total += float(row[2])
            print("-" * 30)
            print(f"Total Expenses: ₹{total}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Function to show expenses by category
def category_summary():
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            category_totals = {}
            for row in reader:
                category_totals[row[1]] = category_totals.get(row[1], 0) + float(row[2])

            print("\nCategory-wise Expenses:")
            for category, total in category_totals.items():
                print(f"{category}: ₹{total}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

# Main Menu
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Category-wise Summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        category_summary()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
