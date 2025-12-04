"""
Personal Finance Tracker (CSV ONLY — No JSON)

Features:
- Add expenses
- Add income
- Store all data in a CSV file (transactions.csv)
- Load data from CSV
- Generate monthly reports
"""

import csv
import os
from datetime import datetime

CSV_FILE = "transactions.csv"

# -----------------------------
# CSV Loading / Saving
# -----------------------------

def load_transactions():
    """
    Loads transactions from a CSV file.
    Returns a list of dicts.
    """
    transactions = []

    if not os.path.exists(CSV_FILE):
        return transactions  # Return empty list if file does not exist

    try:
        with open(CSV_FILE, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert amount to float
                row["amount"] = float(row["amount"])
                transactions.append(row)
        return transactions
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []


def append_transaction(transaction):
    """
    Appends a single transaction to the CSV file.
    """
    file_exists = os.path.exists(CSV_FILE)

    try:
        with open(CSV_FILE, "a", newline="") as csvfile:
            fieldnames = ["date", "type", "amount", "category", "description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if file didn't exist
            if not file_exists:
                writer.writeheader()

            writer.writerow(transaction)

        print("💾 Transaction saved successfully!")
    except Exception as e:
        print(f"❌ Error writing to CSV: {e}")


# -----------------------------
# Input Helpers
# -----------------------------

def input_date():
    date_input = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if date_input == "":
        return datetime.today().strftime("%Y-%m-%d")

    try:
        datetime.strptime(date_input, "%Y-%m-%d")
        return date_input
    except ValueError:
        print("❌ Invalid date format.")
        return None


def input_amount():
    amount_input = input("Enter amount: ").strip()
    try:
        amount = float(amount_input)
        if amount <= 0:
            print("❌ Amount must be greater than zero.")
            return None
        return amount
    except ValueError:
        print("❌ Invalid number.")
        return None


# -----------------------------
# Core Features
# -----------------------------

def add_expense():
    print("\n➕ ADD EXPENSE")

    date = input_date()
    if date is None:
        return

    amount = input_amount()
    if amount is None:
        return

    category = input("Category (Food, Rent, Transport etc.): ").strip()
    if category == "":
        category = "Uncategorized"

    description = input("Description (optional): ").strip()

    transaction = {
        "date": date,
        "type": "expense",
        "amount": amount,
        "category": category,
        "description": description
    }

    append_transaction(transaction)
    print("✅ Expense added!\n")


def add_income():
    print("\n💰 ADD INCOME")

    date = input_date()
    if date is None:
        return

    amount = input_amount()
    if amount is None:
        return

    category = input("Source (Salary, Gift, Freelance, etc.): ").strip()
    if category == "":
        category = "Uncategorized"

    description = input("Description (optional): ").strip()

    transaction = {
        "date": date,
        "type": "income",
        "amount": amount,
        "category": category,
        "description": description
    }

    append_transaction(transaction)
    print("✅ Income added!\n")


def show_all_transactions(transactions):
    print("\n📜 ALL TRANSACTIONS")
    if not transactions:
        print("No data found.\n")
        return

    for i, t in enumerate(transactions, start=1):
        sign = "+" if t["type"] == "income" else "-"
        print(f"{i}. {t['date']} | {t['type'].upper():7} | {sign}₹{t['amount']} | {t['category']} | {t['description']}")
    print()


def monthly_report(transactions):
    print("\n📆 MONTHLY REPORT")

    year = input("Year (e.g. 2025): ").strip()
    month = input("Month (1-12): ").strip()

    try:
        year = int(year)
        month = int(month)
    except:
        print("❌ Invalid input.")
        return

    # Filter monthly data
    monthly = []
    for t in transactions:
        try:
            dt = datetime.strptime(t["date"], "%Y-%m-%d")
            if dt.year == year and dt.month == month:
                monthly.append(t)
        except:
            continue

    if not monthly:
        print("No transactions found for this month.\n")
        return

    total_income = sum(t["amount"] for t in monthly if t["type"] == "income")
    total_expenses = sum(t["amount"] for t in monthly if t["type"] == "expense")
    balance = total_income - total_expenses

    # Category breakdown
    categories = {}
    for t in monthly:
        if t["type"] == "expense":
            categories[t["category"]] = categories.get(t["category"], 0) + t["amount"]

    print(f"\n📊 Report for {year}-{month:02d}")
    print(f"Total Income   : ₹{total_income:.2f}")
    print(f"Total Expenses : ₹{total_expenses:.2f}")
    print(f"Balance        : ₹{balance:.2f}\n")

    print("Expense Breakdown:")
    for cat, amt in categories.items():
        print(f"- {cat}: ₹{amt:.2f}")
    print()


# -----------------------------
# MAIN MENU
# -----------------------------

def main():
    print("💰 PERSONAL FINANCE TRACKER (CSV ONLY)")
    print(f"Data file: {os.path.abspath(CSV_FILE)}\n")

    while True:
        print("MENU:")
        print("1. Add Expense")
        print("2. Add Income")
        print("3. Show All Transactions")
        print("4. Monthly Report")
        print("5. Exit\n")

        choice = input("Choose option (1-5): ").strip()

        transactions = load_transactions()

        if choice == "1":
            add_expense()
        elif choice == "2":
            add_income()
        elif choice == "3":
            show_all_transactions(transactions)
        elif choice == "4":
            monthly_report(transactions)
        elif choice == "5":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice.\n")


if __name__ == "__main__":
    main()
