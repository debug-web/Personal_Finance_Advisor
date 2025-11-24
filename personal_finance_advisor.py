import csv
from datetime import datetime

def load_transactions(filename="transactions.csv"):
    transactions = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        pass  # File will be created on save
    return transactions

def save_transaction(transaction, filename="transactions.csv"):
    try:
        with open(filename, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "category", "amount", "desc"])
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow(transaction)
    except Exception as ex:
        print("Failed to save transaction:", ex)

def add_transaction():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (e.g. Food, Travel, Shopping): ")
    amount = float(input("Enter amount: "))
    desc = input("Enter short description: ")
    transaction = {"date": date, "category": category, "amount": amount, "desc": desc}
    save_transaction(transaction)
    print("Transaction added!")

def list_transactions(transactions):
    print("\nYour Transactions:")
    print("Date       | Category  | Amount | Description")
    print("---------------------------------------------")
    for t in transactions:
        print(f"{t['date']:10} | {t['category']:8} | {t['amount']:>6} | {t['desc']}")
    print()

def spend_by_category(transactions):
    summary = {}
    for t in transactions:
        amount = float(t['amount'])
        cat = t['category']
        summary[cat] = summary.get(cat, 0) + amount
    print("\nTotal spent by category:")
    for cat, total in summary.items():
        print(f"{cat}: {total:.2f}")

def show_budget_advice(transactions):
    limit = float(input("Set your monthly budget: "))
    month = input("Enter month to analyze (YYYY-MM): ")
    spent = 0
    for t in transactions:
        if t["date"].startswith(month):
            spent += float(t["amount"])
    print(f"\nYou spent Rs.{spent:.2f} in {month}.")
    if spent > limit:
        print("⚠️ You have exceeded your budget!")
    elif spent > 0.9 * limit:
        print("Warning: You are close to exceeding your budget.")
    else:
        print("Good job! You’re within your budget.")

def main():
    while True:
        print("\nMenu:")
        print("1. Add a transaction")
        print("2. View all transactions")
        print("3. Summary by category")
        print("4. Budget advice")
        print("5. Exit")
        choice = input("Choose an option: ")

        transactions = load_transactions()
        if choice == "1":
            add_transaction()
        elif choice == "2":
            list_transactions(transactions)
        elif choice == "3":
            spend_by_category(transactions)
        elif choice == "4":
            show_budget_advice(transactions)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
