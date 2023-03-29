import tkinter as tk

root = tk.Tk()
root.geometry("800x800")

# board canvas
canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

light_color = "white"
dark_color = "green"

# Create the squares on the board, 100x100 each
for x in range(8):
    for y in range(8):
        x1 = x * 100
        y1 = y * 100
        x2 = x1 + 100
        y2 = y1 + 100
        if (x + y) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill=light_color)
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill=dark_color)


root.mainloop()