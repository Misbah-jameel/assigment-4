import tkinter as tk

# Canvas size
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
        self.canvas.pack()

        # Draw grid of blue cells
        self.cells = []
        for y in range(0, HEIGHT, CELL_SIZE):
            row = []
            for x in range(0, WIDTH, CELL_SIZE):
                rect = self.canvas.create_rectangle(x, y, x+CELL_SIZE, y+CELL_SIZE, fill="blue", outline="black")
                row.append(rect)
            self.cells.append(row)

        # Bind mouse events
        self.canvas.bind("<B1-Motion>", self.erase)  # Left-click drag to erase

    def erase(self, event):
        """ Changes the color of the rectangle under the cursor to white """
        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE
        if 0 <= row < len(self.cells) and 0 <= col < len(self.cells[row]):
            self.canvas.itemconfig(self.cells[row][col], fill="white")

# Run the application
root = tk.Tk()
root.title("Eraser on Canvas")
app = EraserApp(root)
root.mainloop()
