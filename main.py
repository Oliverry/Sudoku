import interface
import tkinter as tk

root = tk.Tk()
root.title("Sudoku")
root.resizable(False, False)
app = interface.SudokuInterface(master=root)
app.mainloop()