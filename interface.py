import tkinter as tk
import sudoku

class SudokuInterface(tk.Frame):
    def __init__(self, master, sudoku):
        super().__init__(master)
        self.sudoku = sudoku
        self.pack()

        self.length = 600
        self.gridmargin = 50
        self.createWidgets()
    
    def createWidgets(self):
        # create sudoku field
        canvas = tk.Canvas(self, width=self.length, height=self.length, bg="white")
        canvas.pack(side="left")
        cellLength = (self.length-2*self.gridmargin)/9

        # draw grid
        for i in range(10):
            if i % 3 == 0:
                canvas.create_line(self.gridmargin, i*cellLength+self.gridmargin, self.length-self.gridmargin, i*cellLength+self.gridmargin, width=3)
            else:
                canvas.create_line(self.gridmargin, i*cellLength+self.gridmargin, self.length-self.gridmargin, i*cellLength+self.gridmargin)
        for j in range(10):
            if j % 3 == 0:
                canvas.create_line(j*cellLength+self.gridmargin, self.gridmargin, j*cellLength+self.gridmargin, self.length-self.gridmargin, width=3)
            else:
                canvas.create_line(j*cellLength+self.gridmargin, self.gridmargin, j*cellLength+self.gridmargin, self.length-self.gridmargin)

        # add cell functions
        offset = self.gridmargin+0.5*cellLength
        for i in range(9):
            for j in range(9):
                curr = self.sudoku.field[i*9+j]
                if curr > 0:
                    label = tk.Label(canvas, text=self.sudoku.field[i*9+j], bg="white", font="Courier 16 bold")
                    canvas.create_window(i*cellLength+offset, j*cellLength+offset, window=label, width=0.9*cellLength, height=0.9*cellLength)
                else:
                    entry= tk.Entry(canvas, bg="white", font="Courier 16", justify="center", relief="flat")
                    canvas.create_window(i*cellLength+offset, j*cellLength+offset, window=entry, width=0.9*cellLength, height=0.9*cellLength)

        menuFrame = tk.Frame(self)
        menuFrame.pack(side="right")

        exitButton = tk.Button(menuFrame, text="Exit", command=self.exitApp)
        exitButton.pack()

    def exitApp(self):
        self.destroy()

sudoku = sudoku.Sudoku()
root = tk.Tk()
root.title("Sudoku")
app = SudokuInterface(master=root, sudoku=sudoku)
app.mainloop()