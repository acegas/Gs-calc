import tkinter as tk
from tkinter import ttk

def calc_percent():
    try:
        original = float(percent_entry1.get())
        new = float(percent_entry2.get())
        result = ((new - original) / original) * 100
        percent_result.config(text=f"Change: {result:.2f}%")
    except:
        percent_result.config(text="Error")

def convert_inches_mm():
    try:
        val = float(conv_entry.get())
        if conv_var.get() == 'in_to_mm':
            result = val * 25.4
            conv_result.config(text=f"{result:.2f} mm")
        else:
            result = val / 25.4
            conv_result.config(text=f"{result:.2f} in")
    except:
        conv_result.config(text="Error")

root = tk.Tk()
root.title("Calculator with Unit Converter")

notebook = ttk.Notebook(root)
calc_frame = ttk.Frame(notebook)
conv_frame = ttk.Frame(notebook)
percent_frame = ttk.Frame(notebook)
notebook.add(calc_frame, text="Calculator")
notebook.add(conv_frame, text="Inches ↔ mm")
notebook.add(percent_frame, text="Percent Finder")
notebook.pack(fill='both', expand=True)

# Calculator - just a placeholder for now
tk.Label(calc_frame, text="Calculator coming soon!").pack(pady=40)

# Inches ↔ mm Converter
conv_var = tk.StringVar(value='in_to_mm')
conv_entry = tk.Entry(conv_frame)
conv_entry.pack(pady=5)
ttk.Radiobutton(conv_frame, text="Inches to Millimeters", variable=conv_var, value='in_to_mm').pack()
ttk.Radiobutton(conv_frame, text="Millimeters to Inches", variable=conv_var, value='mm_to_in').pack()
tk.Button(conv_frame, text="Convert", command=convert_inches_mm).pack(pady=5)
conv_result = tk.Label(conv_frame, text="")
conv_result.pack()

# Percent Finder
percent_entry1 = tk.Entry(percent_frame)
percent_entry1.pack(pady=2)
percent_entry2 = tk.Entry(percent_frame)
percent_entry2.pack(pady=2)
tk.Button(percent_frame, text="Calculate % Changed", command=calc_percent).pack(pady=5)
percent_result = tk.Label(percent_frame, text="")
percent_result.pack()

root.mainloop()
