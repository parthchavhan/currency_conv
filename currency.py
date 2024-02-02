import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

def convert():
    try:
        amount = float(amount_var.get())
        from_currency = from_currency_var.get().upper()
        to_currency = to_currency_var.get().upper()

        # Fetch the conversion rate
        c = CurrencyRates()
        conversion_rate = c.get_rate(from_currency, to_currency)

        # Calculate the converted amount
        result = round(amount * conversion_rate, 2)

        # Display the result
        result_var.set(f"{amount} {from_currency} = {result} {to_currency}")

        # Update the table
        update_table(from_currency, to_currency, conversion_rate)

    except ValueError:
        result_var.set("Invalid input. Please enter valid numbers.")

def update_table(from_currency, to_currency, conversion_rate):
    # Insert data into the table
    table.insert("", "end", values=(from_currency, to_currency, conversion_rate))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Variables
amount_var = tk.StringVar()
from_currency_var = tk.StringVar()
to_currency_var = tk.StringVar()
result_var = tk.StringVar()

# Labels
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)

# Entry widgets
amount_entry = tk.Entry(root, textvariable=amount_var)
from_currency_entry = tk.Entry(root, textvariable=from_currency_var)
to_currency_entry = tk.Entry(root, textvariable=to_currency_var)
result_entry = tk.Entry(root, textvariable=result_var, state='readonly')

amount_entry.grid(row=0, column=1, padx=10, pady=10)
from_currency_entry.grid(row=1, column=1, padx=10, pady=10)
to_currency_entry.grid(row=2, column=1, padx=10, pady=10)
result_entry.grid(row=3, column=1, padx=10, pady=10)

# Convert button
tk.Button(root, text="Convert", command=convert).grid(row=4, column=0, columnspan=2, pady=10)

# Table
columns = ("From Currency", "To Currency", "Conversion Rate")
table = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    table.heading(col, text=col)
table.grid(row=5, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
