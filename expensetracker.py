import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as file:
                self.expenses = json.load(file)
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open('expenses.json', 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, description, category):
        expense = {
            'amount': amount,
            'description': description,
            'category': category,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.expenses.append(expense)
        self.save_expenses()

    def get_monthly_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S').month == month and datetime.strptime(expense['date'], '%Y-%m-%d %H:%M:%S').year == year]
        total = sum(expense['amount'] for expense in monthly_expenses)
        return total, monthly_expenses

    def get_category_summary(self):
        category_summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in category_summary:
                category_summary[category] = 0
            category_summary[category] += expense['amount']
        return category_summary

    def display_expenses(self):
        for expense in self.expenses:
            print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category Summary")
        print("4. View All Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                category = input("Enter category: ")
                tracker.add_expense(amount, description, category)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input. Please enter numeric values for amount.")
        elif choice == '2':
            try:
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2023): "))
                total, expenses = tracker.get_monthly_summary(month, year)
                print(f"\nTotal expenses for {month}/{year}: {total}")
                for expense in expenses:
                    print(f"Amount: {expense['amount']}, Description: {expense['description']}, Category: {expense['category']}, Date: {expense['date']}")
            except ValueError:
                print("Invalid input. Please enter numeric values for month and year.")
        elif choice == '3':
            summary = tracker.get_category_summary()
            print("\nCategory Summary:")
            for category, total in summary.items():
                print(f"{category}: {total}")
        elif choice == '4':
            tracker.display_expenses()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
