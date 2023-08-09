import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample expense categories
expense_categories = ["Food", "Transportation", "Entertainment", "Utilities", "Other"]

class ExpenseTrackerApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Expense Tracker App")

        self.expense_label = ttk.Label(root, text="Enter Expense:")
        self.expense_label.pack()

        self.expense_entry = ttk.Entry(root)
        self.expense_entry.pack()

        self.category_label = ttk.Label(root, text="Select Category:")
        self.category_label.pack()

        self.category_combobox = ttk.Combobox(root, values=expense_categories)
        self.category_combobox.pack()

        self.submit_button = ttk.Button(root, text="Submit Expense", command=self.submit_expense)
        self.submit_button.pack()

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

    def submit_expense(self):
        expense = self.expense_entry.get()
        category = self.category_combobox.get()

        if expense and category:
            self.plot_expense(category, float(expense))

    def plot_expense(self, category, amount):
        expenses = [300, 200, 400, 150, 250]  # Sample data
        expenses[expense_categories.index(category)] += amount

        self.ax.clear()
        self.ax.pie(expenses, labels=expense_categories, autopct="%1.1f%%")
        self.ax.set_title("Expense Distribution")

        self.canvas.draw()

if _name_ == "_main_":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()