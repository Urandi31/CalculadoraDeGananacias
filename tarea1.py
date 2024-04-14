import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

class MusicStudioProfitCalculator:
    def __init__(self):
        self.income = []
        self.expenses = []
        self.income_id = 1
        self.expense_id = 1

    def add_income(self, concept, amount):
        self.income.append((self.income_id, concept, amount))
        self.income_id += 1

    def add_expense(self, concept, amount):
        self.expenses.append((self.expense_id, concept, amount))
        self.expense_id += 1

    def calculate_profit(self):
        total_income = sum(amount for _, _, amount in self.income)
        total_expenses = sum(amount for _, _, amount in self.expenses)
        profit = total_income - total_expenses
        return total_income, total_expenses, profit


def add_income():
    concept = income_concept_entry.get()
    amount = float(income_amount_entry.get())
    calculator.add_income(concept, amount)
    update_table()


def add_expense():
    concept = expense_concept_entry.get()
    amount = float(expense_amount_entry.get())
    calculator.add_expense(concept, amount)
    update_table()


def calculate_and_display():
    total_income, total_expenses, profit = calculator.calculate_profit()
    result = f"Total Income: ${total_income:.2f}\nTotal Expenses: ${total_expenses:.2f}\nProfit: ${profit:.2f}" 
    result_text.set(result)
    result_history.append(result)


def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History of Results")
    history_label = ttk.Label(history_window, text="Previous Results")
    history_label.pack(padx=10, pady=10)
    history_text = tk.Text(history_window, height=10, width=50)
    history_text.pack(padx=10, pady=10)
    profit_count = 1
    for result in result_history:
        history_text.insert(tk.END, f"Profit {profit_count}: {result}\n")
        profit_count += 1


def update_table():
    income_tree.delete(*income_tree.get_children())
    for item in calculator.income:
        income_tree.insert("", "end", values=item)
    expenses_tree.delete(*expenses_tree.get_children())
    for item in calculator.expenses:
        expenses_tree.insert("", "end", values=item)


def plot_chart():
    if not calculator.income and not calculator.expenses:
        messagebox.showwarning("No Data", "Please enter income and expenses first.")
        return

    labels = ['Income', 'Expenses']
    sizes = [sum(amount for _, _, amount in calculator.income), sum(amount for _, _, amount in calculator.expenses)]

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Income vs Expenses')
    plt.show()


calculator = MusicStudioProfitCalculator()
result_history = []

root = tk.Tk()
root.title("Music Studio Profit Calculator")
root.configure(bg="#282828")  

income_frame = ttk.LabelFrame(root, text="Add Income")
income_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
income_concept_label = ttk.Label(income_frame, text="Concept:")
income_concept_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
income_concept_entry = ttk.Entry(income_frame)
income_concept_entry.grid(row=0, column=1, padx=5, pady=5)
income_amount_label = ttk.Label(income_frame, text="Amount:")
income_amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
income_amount_entry = ttk.Entry(income_frame)
income_amount_entry.grid(row=1, column=1, padx=5, pady=5)
add_income_button = ttk.Button(income_frame, text="Add", command=add_income)
add_income_button.grid(row=2, columnspan=2, padx=5, pady=5)

expense_frame = ttk.LabelFrame(root, text="Add Expense")
expense_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
expense_concept_label = ttk.Label(expense_frame, text="Concept:")
expense_concept_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
expense_concept_entry = ttk.Entry(expense_frame)
expense_concept_entry.grid(row=0, column=1, padx=5, pady=5)
expense_amount_label = ttk.Label(expense_frame, text="Amount:")
expense_amount_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
expense_amount_entry = ttk.Entry(expense_frame)
expense_amount_entry.grid(row=1, column=1, padx=5, pady=5)
add_expense_button = ttk.Button(expense_frame, text="Add", command=add_expense)
add_expense_button.grid(row=2, columnspan=2, padx=5, pady=5)

table_frame = ttk.Frame(root)
table_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

income_tree = ttk.Treeview(table_frame, columns=("ID", "Concept", "Amount"), show="headings")
income_tree.heading("ID", text="ID")
income_tree.heading("Concept", text="Concept")
income_tree.heading("Amount", text="Amount")
income_tree.pack(side="left", fill="both", expand=True)

expenses_tree = ttk.Treeview(table_frame, columns=("ID", "Concept", "Amount"), show="headings")
expenses_tree.heading("ID", text="ID")
expenses_tree.heading("Concept", text="Concept")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.pack(side="right", fill="both", expand=True)

action_frame = ttk.Frame(root)
action_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

calculate_button = ttk.Button(action_frame, text="Calculate", command=calculate_and_display)
calculate_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

show_history_button = ttk.Button(action_frame, text="Show History", command=show_history)
show_history_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

plot_chart_button = ttk.Button(action_frame, text="Plot Chart", command=plot_chart)
plot_chart_button.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

result_text = tk.StringVar()
result_label = ttk.Label(action_frame, textvariable=result_text)
result_label.grid(row=0, column=3, padx=5, pady=5, sticky="nsew")

root.mainloop()