import tkinter as tk
from tkinter import messagebox
from datetime import date

class Expense:
    def _init_(self, description, amount):
        self.date = date.today()
        self.description = description
        self.amount = amount

class FinanceTracker:
    def _init_(self, root):
        self.root = root
        self.root.title("Finance Tracker")
        
        # Store expenses in a list
        self.expenses = []
        
        # Input fields
        tk.Label(root, text="Description:").grid(row=0, column=0)
        self.desc_entry = tk.Entry(root)
        self.desc_entry.grid(row=0, column=1)
        
        tk.Label(root, text="Amount:").grid(row=1, column=0)
        self.amount_entry = tk.Entry(root)
        self.amount_entry.grid(row=1, column=1)
        
        # Buttons
        tk.Button(root, text="Add Expense", command=self.add_expense).grid(row=2, column=0, pady=5)
        tk.Button(root, text="View Expenses", command=self.view_expenses).grid(row=2, column=1, pady=5)
        
    def add_expense(self):
        description = self.desc_entry.get()
        amount = self.amount_entry.get()
        try:
            amount = float(amount)
            new_expense = Expense(description, amount)
            self.expenses.append(new_expense)
            messagebox.showinfo("Success", "Expense added successfully!")
            self.desc_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")
            
    def view_expenses(self):
        expense_list = "\n".join([f"{e.date} - {e.description}: ${e.amount}" for e in self.expenses])
        if expense_list:
            messagebox.showinfo("Expenses", expense_list)
        else:
            messagebox.showinfo("No Expenses", "No expenses recorded yet.")

# Run the app
root = tk.Tk()
app = FinanceTracker(root)
root.mainloop()