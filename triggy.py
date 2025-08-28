import tkinter as tk
import math

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
            result_lbl.config(text="Enter at least two values, including one side.")
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
        result_lbl.config(text=f"Solved!")
    except Exception as e:
        result_lbl.config(text="Error: Check your inputs.")

def draw_triangle(a, b, c, A, B):
    canvas.delete("all")
    pad = 40
    base = 180
    height = 120

    # ---- Offsets for label adjustment ----
    A_offset_x, A_offset_y = 10, 28    # Angle A (vertex A)
    B_offset_x, B_offset_y = -25, -10  # Angle B (vertex B)
    C_offset_x, C_offset_y = 10, -10   # vertex C
    b_offset_y = 10                    # side b (base)
    a_offset_x = -10                   # side a (vertical leg)
    c_offset_x, c_offset_y = -1, -10  # side c (hypotenuse)
    # --------------------------------------

    # Triangle corners
    x_C, y_C = pad, pad + height         # C (right angle)
    x_B, y_B = pad + base, pad + height  # B
    x_A, y_A = pad, pad                  # A

    canvas.create_polygon(x_C, y_C, x_B, y_B, x_A, y_A, fill='#d0eaff')
    canvas.create_line(x_C, y_C, x_B, y_B, width=3)
    canvas.create_line(x_B, y_B, x_A, y_A, width=3)
    canvas.create_line(x_A, y_A, x_C, y_C, width=3)

    # Midpoints for side labels
    mx_b, my_b = (x_C + x_B) / 2, (y_C + y_B) / 2
    mx_a, my_a = (x_A + x_C) / 2, (y_A + y_C) / 2
    mx_c, my_c = (x_A + x_B) / 2, (y_A + y_B) / 2

    # --- Labels ---
    # Sides
    canvas.create_text(mx_b, my_b + b_offset_y, text=f"b = {b:.2f}" if b else "b")
    canvas.create_text(mx_a + a_offset_x, my_a, text=f"a = {a:.2f}" if a else "a", anchor="e")
    canvas.create_text(mx_c + c_offset_x, my_c + c_offset_y, text=f"c = {c:.2f}" if c else "c")

    # Angles
    canvas.create_text(x_A + A_offset_x, y_A + A_offset_y, text=f"A\n{A:.2f}°" if A else "A", anchor="w")
    canvas.create_text(x_B + B_offset_x, y_B + B_offset_y, text=f"B\n{B:.2f}°" if B else "B", anchor="e")
    canvas.create_text(x_C + C_offset_x, y_C + C_offset_y, text="C", anchor="w")

root = tk.Tk()
root.title("Right Triangle Solver")

frame = tk.Frame(root)
frame.pack(side=tk.LEFT, padx=15, pady=15)

tk.Label(frame, text="Side a (height):").grid(row=0, column=0)
tk.Label(frame, text="Side b (base):").grid(row=1, column=0)
tk.Label(frame, text="Side c (hypotenuse):").grid(row=2, column=0)
tk.Label(frame, text="Angle A (top, deg):").grid(row=3, column=0)
tk.Label(frame, text="Angle B (bottom right, deg):").grid(row=4, column=0)
entry_a = tk.Entry(frame)
entry_b = tk.Entry(frame)
entry_c = tk.Entry(frame)
entry_A = tk.Entry(frame)
entry_B = tk.Entry(frame)
entry_a.grid(row=0, column=1)
entry_b.grid(row=1, column=1)
entry_c.grid(row=2, column=1)
entry_A.grid(row=3, column=1)
entry_B.grid(row=4, column=1)

tk.Button(frame, text="Calculate", command=solve_triangle).grid(row=5, column=0, columnspan=2, pady=8)
result_lbl = tk.Label(frame, text="")
result_lbl.grid(row=6, column=0, columnspan=2)

canvas = tk.Canvas(root, width=260, height=200, bg="white")
canvas.pack(side=tk.RIGHT, padx=15, pady=15)
draw_triangle(None, None, None, None, None)

root.mainloop()
