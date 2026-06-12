# Expense Tracker

FILE_NAME = "expenses.txt"


def add_expense():
    try:
        category = input("Enter Expense Category: ").strip()
        
        if category == "":
            print("Category cannot be empty!")
            return

        if category.isdigit():
            print("Category cannot be a number!")
            return

        amount = float(input("Enter Amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0!")
            return

        with open(FILE_NAME, "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense Added Successfully!")

    except ValueError:
        print("Invalid Amount! Please enter a valid number.")


def view_expenses():
    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("\nNo Expenses Found.")
            return

        print("\n===== Expense Records =====")

        for expense in expenses:
            category, amount = expense.strip().split(",")
            print(f"{category} - ₹{amount}")

    except FileNotFoundError:
        print("\nNo expense records found yet.")


def spending_summary():
    total_expense = 0

    try:
        with open(FILE_NAME, "r") as file:
            expenses = file.readlines()

        if len(expenses) == 0:
            print("\nNo Expenses Found.")
            return

        print("\n===== Spending Summary =====")

        for expense in expenses:
            category, amount = expense.strip().split(",")

            print(f"{category} - ₹{amount}")

            total_expense += float(amount)

        print("----------------------------")
        print(f"Total Expense: ₹{total_expense}")

    except FileNotFoundError:
        print("\nNo expense records found yet.")


def menu():

    while True:

        print("\n========== EXPENSE TRACKER ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Spending Summary")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_expense()

            elif choice == 2:
                view_expenses()

            elif choice == 3:
                spending_summary()

            elif choice == 4:
                print("Thank you for using Expense Tracker!")
                break

            else:
                print("Invalid Choice! Please select between 1 and 4.")

        except ValueError:
            print("Please enter a valid number.")


menu()