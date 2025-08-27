import tkinter as tk
from tkinter import ttk

def calc_button_click(value):
    current = calc_display.get()
    if value == '=':
        try:
            result = str(eval(current))
            calc_display.delete(0, tk.END)
            calc_display.insert(tk.END, result)
        except:
            calc_display.delete(0, tk.END)
            calc_display.insert(tk.END, "Error")
    elif value == 'C':
        calc_display.delete(0, tk.END)
    else:
        calc_display.insert(tk.END, value)

def in_to_mm():
    try:
        val = float(calc_display.get())
        result = val * 25.4
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, f"{result:.2f}")
    except:
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, "Error")

def mm_to_in():
    try:
        val = float(calc_display.get())
        result = val / 25.4
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, f"{result:.4f}")
    except:
        calc_display.delete(0, tk.END)
        calc_display.insert(tk.END, "Error")

def backspace():
    current = calc_display.get()
    if len(current) > 0:
        calc_display.delete(len(current)-1, tk.END)


def calc_percent():
    try:
        original = float(percent_entry1.get())
        new = float(percent_entry2.get())
        if original == 0:
            percent_result.config(text="Divide by zero!")
            return
        result = ((new - original) / original) * 100
        percent_result.config(text=f"Change: {result:.2f}%")
    except:
        percent_result.config(text="Error")

root = tk.Tk()
root.title("G's Calculator")
root.minsize(380, 480)

# Style for bigger tabs
style = ttk.Style()
style.configure("TNotebook.Tab", font=('Arial', 16), padding=[20, 10])

notebook = ttk.Notebook(root)
calc_frame = ttk.Frame(notebook)
percent_frame = ttk.Frame(notebook)
notebook.add(calc_frame, text="Calculator")
notebook.add(percent_frame, text="Percent Finder")
notebook.pack(fill='both', expand=True)

###############################
# Calculator Panel
###############################
for i in range(7):  # 7 rows for buttons + conversion
    calc_frame.rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    calc_frame.columnconfigure(j, weight=1)

calc_display = tk.Entry(calc_frame, font=('Arial', 20), borderwidth=2, relief="groove", justify='right')
calc_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]
for (text, row, col) in buttons:
    tk.Button(calc_frame, text=text, font=('Arial', 16),
              command=lambda v=text: calc_button_click(v)).grid(
        row=row, column=col, padx=2, pady=2, sticky="nsew"
    )
# Add the backspace button (row=5, column=1 example)
tk.Button(calc_frame, text="←", font=('Arial', 16),
          command=backspace).grid(
    row=5, column=1, padx=2, pady=2, sticky="nsew"
)

# Add conversion buttons below calculator
tk.Button(calc_frame, text="In → mm", font=('Arial', 15), command=in_to_mm).grid(
    row=6, column=0, columnspan=2, padx=2, pady=4, sticky="nsew"
)
tk.Button(calc_frame, text="mm → In", font=('Arial', 15), command=mm_to_in).grid(
    row=6, column=2, columnspan=2, padx=2, pady=4, sticky="nsew"
)

###############################
# Percent Finder Panel
###############################
for i in range(5):
    percent_frame.rowconfigure(i, weight=1)
for j in range(2):
    percent_frame.columnconfigure(j, weight=1)

tk.Label(percent_frame, text="Original Value:", font=('Arial', 14)).grid(row=0, column=0, sticky="e", padx=8, pady=8)
percent_entry1 = tk.Entry(percent_frame, font=('Arial', 16))
percent_entry1.grid(row=0, column=1, sticky="nsew", padx=8, pady=8)

tk.Label(percent_frame, text="New Value:", font=('Arial', 14)).grid(row=1, column=0, sticky="e", padx=8, pady=8)
percent_entry2 = tk.Entry(percent_frame, font=('Arial', 16))
percent_entry2.grid(row=1, column=1, sticky="nsew", padx=8, pady=8)

tk.Button(percent_frame, text="Calculate % Changed", font=('Arial', 15),
          command=calc_percent).grid(row=2, column=0, columnspan=2, sticky="nsew", padx=8, pady=8)

percent_result = tk.Label(percent_frame, text="", font=('Arial', 16))
percent_result.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=8, pady=8)

root.mainloop()
