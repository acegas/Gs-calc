import tkinter as tk
import math

# Store triangle rotation state: 0, 1, 2, or 3 (times 90 degrees)
rotation = 0

def solve_triangle():
    global triangle_data
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

        triangle_data = (a, b, c, A, B)
        draw_triangle(*triangle_data, rotation)
        result_lbl.config(text=f"Solved!")
    except Exception as e:
        result_lbl.config(text="Error: Check your inputs.")

def rotate_triangle():
    global rotation, triangle_data
    rotation = (rotation + 1) % 4
    draw_triangle(*triangle_data, rotation)

def draw_triangle(a, b, c, A, B, rotation=0):
    canvas.delete("all")
    pad = 40
    base = 180
    height = 120

    # Base triangle points
    points = [
        (pad, pad + height),         # x_C, y_C (right angle, vertex C)
        (pad + base, pad + height),  # x_B, y_B (vertex B)
        (pad, pad)                   # x_A, y_A (vertex A)
    ]

    # Rotate points around center
    cx, cy = pad + base // 2, pad + height // 2
    def rotate(x, y, deg):
        rad = math.radians(deg)
        x0, y0 = x - cx, y - cy
        x_new = x0 * math.cos(rad) - y0 * math.sin(rad) + cx
        y_new = x0 * math.sin(rad) + y0 * math.cos(rad) + cy
        return x_new, y_new
    rotated_pts = [rotate(x, y, 90*rotation) for x, y in points]
    x_C, y_C = rotated_pts[0]
    x_B, y_B = rotated_pts[1]
    x_A, y_A = rotated_pts[2]

    canvas.create_polygon(x_C, y_C, x_B, y_B, x_A, y_A, fill='#d0eaff')
    canvas.create_line(x_C, y_C, x_B, y_B, width=3)
    canvas.create_line(x_B, y_B, x_A, y_A, width=3)
    canvas.create_line(x_A, y_A, x_C, y_C, width=3)

    # Compute midpoint helper
    midpoint = lambda A, B: ((A[0]+B[0])/2, (A[1]+B[1])/2)

    # Side labels
    mx_b, my_b = midpoint((x_C, y_C), (x_B, y_B))
    canvas.create_text(mx_b, my_b + 18, text=f"b = {b:.2f}" if b else "b")

    mx_a, my_a = midpoint((x_A, y_A), (x_C, y_C))
    canvas.create_text(mx_a - 18, my_a, text=f"a = {a:.2f}" if a else "a", anchor="e")

    mx_c, my_c = midpoint((x_A, y_A), (x_B, y_B))
    canvas.create_text(mx_c - 16, my_c - 10, text=f"c = {c:.2f}" if c else "c")

    # Angle B (adjustable placement)
    canvas.create_text(x_B - 10, y_B - 10, text=f"B\n{B:.2f}°" if B else "B", anchor="e")
    # Angle A (adjustable placement)
    canvas.create_text(x_A + 23, y_A + 32, text=f"A\n{A:.2f}°" if A else "A", anchor="w")
    # Vertex C label only
    canvas.create_text(x_C + 10, y_C - 10, text="C", anchor="w")

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
tk.Button(frame, text="Rotate", command=rotate_triangle).grid(row=6, column=0, columnspan=2, pady=4)

result_lbl = tk.Label(frame, text="")
result_lbl.grid(row=7, column=0, columnspan=2)

canvas = tk.Canvas(root, width=260, height=200, bg="white")
canvas.pack(side=tk.RIGHT, padx=15, pady=15)

# Store last-calculated triangle info for rotation
triangle_data = (None, None, None, None, None)
draw_triangle(*triangle_data, rotation)

root.mainloop()
