import tkinter as tk
from tkinter import ttk
import math

##############################
# Right Triangle Solver Logic
##############################
def solve_triangle():
    a_val = entry_a.get().strip()
    b_val = entry_b.get().strip()
    c_val = entry_c.get().strip()
    A_val = entry_A.get().strip()
    B_val = entry_B.get().strip()
    a = float(a_val) if a_val else None
    b = float(b_val) if b_val else None
    c = float(c_val) if c_val else None
    A = float(A_val) if A_val else None
    B = float(B_val) if B_val else None

    try:
        if a and b:
            c = math.hypot(a, b)
            A = math.degrees(math.atan2(a, b))
            B = 90 - A
        elif a and c:
            b = math.sqrt(max(0, c**2 - a**2))
            A = math.degrees(math.asin(a / c))
            B = 90 - A
        elif b and c:
            a = math.sqrt(max(0, c**2 - b**2))
            B = math.degrees(math.asin(b / c))
            A = 90 - B
        elif a and A:
            A_rad = math.radians(A)
            c = a / math.sin(A_rad)
            b = math.sqrt(max(0, c**2 - a**2))
            B = 90 - A
        elif b and B:
            B_rad = math.radians(B)
            c = b / math.sin(B_rad)
            a = math.sqrt(max(0, c**2 - b**2))
            A = 90 - B
        elif c and A:
            A_rad = math.radians(A)
            a = c * math.sin(A_rad)
            b = math.sqrt(max(0, c**2 - a**2))
            B = 90 - A
        elif c and B:
            B_rad = math.radians(B)
            b = c * math.sin(B_rad)
            a = math.sqrt(max(0, c**2 - b**2))
            A = 90 - B
        else:
            tri_result_lbl.config(text="Enter at least two values, including one side.")
            return

        entry_a.delete(0, tk.END)
        entry_b.delete(0, tk.END)
        entry_c.delete(0, tk.END)
        entry_A.delete(0, tk.END)
        entry_B.delete(0, tk.END)
        entry_a.insert(0, f"{a:.4f}" if a else "")
        entry_b.insert(0, f"{b:.4f}" if b else "")
        entry_c.insert(0, f"{c:.4f}" if c else "")
        entry_A.insert(0, f"{A:.2f}" if A else "")
        entry_B.insert(0, f"{B:.2f}" if B else "")

        draw_triangle(a, b, c, A, B)
        tri_result_lbl.config(text="Solved!")
    except Exception as e:
        tri_result_lbl.config(text="Error: Check your inputs.")

def draw_triangle(a, b, c, A, B):
    tri_canvas.delete("all")
    pad = 40
    base = 180
    height = 120

    # ---- Offsets for label adjustment ----
    A_offset_x, A_offset_y = 10, 28    # Angle A (vertex A)
    B_offset_x, B_offset_y = -25, -10  # Angle B (vertex B)
    C_offset_x, C_offset_y = 10, -10   # vertex C
    b_offset_y = 10                    # side b (base)
    a_offset_x = -10                   # side a (vertical leg)
    c_offset_x, c_offset_y = -1, -10   # side c (hypotenuse)
    # --------------------------------------

    # Triangle corners
    x_C, y_C = pad, pad + height         # C (right angle)
    x_B, y_B = pad + base, pad + height  # B
    x_A, y_A = pad, pad                  # A

    tri_canvas.create_polygon(x_C, y_C, x_B, y_B, x_A, y_A, fill='#d0eaff')
    tri_canvas.create_line(x_C, y_C, x_B, y_B, width=3)
    tri_canvas.create_line(x_B, y_B, x_A, y_A, width=3)
    tri_canvas.create_line(x_A, y_A, x_C, y_C, width=3)

    # Midpoints for side labels
    mx_b, my_b = (x_C + x_B) / 2, (y_C + y_B) / 2
    mx_a, my_a = (x_A + x_C) / 2, (y_A + y_C) / 2
    mx_c, my_c = (x_A + x_B) / 2, (y_A + y_B) / 2

    # Sides
    tri_canvas.create_text(mx_b, my_b + b_offset_y, text=f"b = {b:.2f}" if b else "b")
    tri_canvas.create_text(mx_a + a_offset_x, my_a, text=f"a = {a:.2f}" if a else "a", anchor="e")
    tri_canvas.create_text(mx_c + c_offset_x, my_c + c_offset_y, text=f"c = {c:.2f}" if c else "c")

    # Angles
    tri_canvas.create_text(x_A + A_offset_x, y_A + A_offset_y, text=f"A\n{A:.2f}°" if A else "A", anchor="w")
    tri_canvas.create_text(x_B + B_offset_x, y_B + B_offset_y, text=f"B\n{B:.2f}°" if B else "B", anchor="e")
    tri_canvas.create_text(x_C + C_offset_x, y_C + C_offset_y, text="C", anchor="w")

root = tk.Tk()
root.title("Integrated Calculator")

# Notebook setup
style = ttk.Style()
style.configure("TNotebook.Tab", font=('Arial', 16), padding=[20, 10])
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

##############################
# Tab 1: Calculator
##############################
calc_frame = ttk.Frame(notebook)
notebook.add(calc_frame, text="Calculator")

calc_frame.rowconfigure(tuple(range(7)), weight=1)
calc_frame.columnconfigure(tuple(range(4)), weight=1)

calc_display = tk.Entry(calc_frame, font=('Arial', 20), borderwidth=2, relief="groove", justify='right')
calc_display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=4, pady=4)

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
    elif value == '←':
        calc_display.delete(len(current)-1, tk.END)
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

# Layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0), ('←',5,1)
]
for (text, row, col) in buttons:
    tk.Button(calc_frame, text=text, font=('Arial', 16),
              command=lambda v=text: calc_button_click(v)).grid(
        row=row, column=col, padx=2, pady=2, sticky="nsew")

tk.Button(calc_frame, text="In → mm", font=('Arial', 15), command=in_to_mm).grid(
    row=6, column=0, columnspan=2, padx=2, pady=4, sticky="nsew")
tk.Button(calc_frame, text="mm → In", font=('Arial', 15), command=mm_to_in).grid(
    row=6, column=2, columnspan=2, padx=2, pady=4, sticky="nsew")

##############################
# Tab 2: Percent Finder
##############################
percent_frame = ttk.Frame(notebook)
notebook.add(percent_frame, text="Percent Finder")
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
tk.Button(percent_frame, text="Calculate % Changed", font=('Arial', 15),
          command=calc_percent).grid(row=2, column=0, columnspan=2, sticky="nsew", padx=8, pady=8)
percent_result = tk.Label(percent_frame, text="", font=('Arial', 16))
percent_result.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=8, pady=8)

##############################
# Tab 3: Right Triangle Solver
##############################
tri_frame = ttk.Frame(notebook)
notebook.add(tri_frame, text="Right Triangle Solver")

tri_input_frame = tk.Frame(tri_frame)
tri_input_frame.pack(side=tk.LEFT, padx=15, pady=15)

tk.Label(tri_input_frame, text="Side a (height):").grid(row=0, column=0)
tk.Label(tri_input_frame, text="Side b (base):").grid(row=1, column=0)
tk.Label(tri_input_frame, text="Side c (hypotenuse):").grid(row=2, column=0)
tk.Label(tri_input_frame, text="Angle A (top, deg):").grid(row=3, column=0)
tk.Label(tri_input_frame, text="Angle B (bottom right, deg):").grid(row=4, column=0)
entry_a = tk.Entry(tri_input_frame)
entry_b = tk.Entry(tri_input_frame)
entry_c = tk.Entry(tri_input_frame)
entry_A = tk.Entry(tri_input_frame)
entry_B = tk.Entry(tri_input_frame)
entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)
entry_A.grid(row=3, column=1)
entry_B.grid(row=4, column=1)
tk.Button(tri_input_frame, text="Calculate", command=solve_triangle).grid(row=5, column=0, columnspan=2, pady=8)
tri_result_lbl = tk.Label(tri_input_frame, text="")
tri_result_lbl.grid(row=6, column=0, columnspan=2)

tri_canvas = tk.Canvas(tri_frame, width=260, height=200, bg="white")
tri_canvas.pack(side=tk.RIGHT, padx=15, pady=15)
draw_triangle(None, None, None, None, None)

root.mainloop()
