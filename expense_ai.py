# Smart Expense Analyzer

expenses = []

def add_expense():
    category = input("Enter category (Food/Travel/Shopping/Other): ")
    amount = float(input("Enter amount: "))
    
    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    print("✅ Expense added successfully!\n")

def analyze_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    total = 0
    category_totals = {}
    
    for expense in expenses:
        total += expense["amount"]
        
        if expense["category"] in category_totals:
            category_totals[expense["category"]] += expense["amount"]
        else:
            category_totals[expense["category"]] = expense["amount"]
    
    print("\n📊 Expense Analysis")
    print("Total Spending:", total)
    
    for category, amount in category_totals.items():
        print(f"{category}: {amount}")
        
        if amount > total * 0.5:
            print(f"⚠ You are spending too much on {category}!")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. Analyze Expenses")
        print("3. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            analyze_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main()
