import tkinter as tk
from tkinter import ttk


def calculate_totals():
    base_salary = float(base_salary_entry.get() or 0)
    bonus = float(bonus_entry.get() or 0)
    expensify = float(expensify_entry.get() or 0)
    insurance = float(insurance_entry.get() or 0)

    total_compensation = base_salary + bonus + expensify + insurance
    total_compensation_label.config(text=f"{total_compensation:.2f}")

    single_tax = total_compensation * 0.05
    military_tax = total_compensation * 0.01
    social_tax = 45  # фіксоване значення для ЄСВ

    single_tax_label.config(text=f"{single_tax:.2f}")
    military_tax_label.config(text=f"{military_tax:.2f}")
    social_tax_label.config(text=f"{social_tax:.2f}")

    # Summary for tax payment
    total_taxes = single_tax + military_tax + social_tax
    total_taxes_label.config(text=f"{total_taxes:.2f}")


# Main window
root = tk.Tk()
root.title("Калькулятор податків")

# Month selection
month_label = ttk.Label(root, text="Місяць")
month_label.grid(row=0, column=0, padx=5, pady=5)
month_combo = ttk.Combobox(root, values=["January", "February", "March", "April", "May", "June", "July", "August",
                                         "September", "October", "November", "December"])
month_combo.grid(row=0, column=1, padx=5, pady=5)
month_combo.set("January")

# Inputs from user
labels = ["Base Salary", "Bonus", "Expensify", "Insurance", "Total"]
entries = []

for i, label in enumerate(labels):
    ttk.Label(root, text=label).grid(row=i + 1, column=0, padx=5, pady=5)
    if label != "Total":
        entry = ttk.Entry(root)
        entry.grid(row=i + 1, column=1, padx=5, pady=5)
        entries.append(entry)
    else:
        total_compensation_label = ttk.Label(root, text="0.00")
        total_compensation_label.grid(row=i + 1, column=1, padx=5, pady=5)

base_salary_entry, bonus_entry, expensify_entry, insurance_entry = entries

# Tax
single_tax_label = ttk.Label(root, text="0.00")
military_tax_label = ttk.Label(root, text="0.00")
social_tax_label = ttk.Label(root, text="0.00")

ttk.Label(root, text="Єдиний податок (5%)").grid(row=6, column=0, padx=5, pady=5)
single_tax_label.grid(row=6, column=1, padx=5, pady=5)

ttk.Label(root, text="Військовий збір (1%)").grid(row=7, column=0, padx=5, pady=5)
military_tax_label.grid(row=7, column=1, padx=5, pady=5)

ttk.Label(root, text="ЄСВ (місячний платіж)").grid(row=8, column=0, padx=5, pady=5)
social_tax_label.grid(row=8, column=1, padx=5, pady=5)

# Підсумок податків
ttk.Label(root, text="Сума для сплати податків").grid(row=9, column=0, padx=5, pady=5)
total_taxes_label = ttk.Label(root, text="0.00")
total_taxes_label.grid(row=9, column=1, padx=5, pady=5)

# Кнопка розрахунку
calculate_button = ttk.Button(root, text="Розрахувати", command=calculate_totals)
calculate_button.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
