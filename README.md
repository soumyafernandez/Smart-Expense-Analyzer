# 💰 Smart Expense Analyzer

A simple Python-based expense tracking and analysis tool that helps users monitor spending patterns and detect overspending using rule-based logic.

This project was built as part of a hands-on, project-based approach to learning Python and problem-solving.

---

## 🚀 Features

- Add daily expenses with category and amount
- View total spending
- Category-wise spending breakdown
- Overspending alert (if a category exceeds 50% of total spending)
- Simple and interactive command-line interface

---

## 🧠 Problem Statement

Managing daily expenses without tracking can lead to poor financial decisions.  
This project provides a simple command-line solution to:

- Record expenses
- Analyze spending patterns
- Identify high-spending categories

---

## 🛠 Tech Stack

- Python 3
- Lists & Dictionaries
- Functions
- Loops
- Conditional Statements

---

## 📂 Project Structure

```
Smart-Expense-Analyzer/
│
├── expense_ai.py
└── README.md
```

---

## ▶ How to Run

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Smart-Expense-Analyzer.git
```

### 2️⃣ Navigate to Project Folder

```bash
cd Smart-Expense-Analyzer
```

### 3️⃣ Run the Program

```bash
python expense_ai.py
```

---

## 📊 Example Output

```
1. Add Expense
2. Analyze Expenses
3. Exit

Choose option: 1
Enter category: Food
Enter amount: 500
Expense added successfully!

Choose option: 2

Expense Analysis
Total Spending: 1000
Food: 600
⚠ You are spending too much on Food!
```

---

## 🤖 AI Logic Used

This project uses rule-based decision making:

```python
if amount > total * 0.5:
    print("⚠ You are spending too much on that category!")
```

AI (Beginner Level) = Data + Logic + Pattern Recognition

---

## 📈 Future Improvements

- Store data in CSV/JSON
- Add monthly analytics
- Data visualization using Matplotlib
- Budget limit setting
- Convert into a web application (Flask/Django)
- Add basic machine learning prediction

---

## 🎯 Learning Outcomes

- Writing modular Python functions
- Working with data structures (lists & dictionaries)
- Building CLI applications
- Implementing logic-based decision systems
- Thinking like a software engineer

---

## 👩‍💻 Author

Built as part of a project-based Python learning journey.
