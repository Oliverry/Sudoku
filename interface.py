import tkinter as tk
import sudoku

class SudokuInterface(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.canLength = 600
        self.gridmargin = 50
        self.cellLength = (self.canLength-2*self.gridmargin)/9
        self.createWidgets()
    
    def createWidgets(self):
        # create sudoku field
        self.canvas = tk.Canvas(self, width=self.canLength, height=self.canLength, bg="white")
        self.canvas.pack(side="left")

        # draw sudoku grid
        for i in range(10):
            if i % 3 == 0:
                self.canvas.create_line(self.gridmargin, i*self.cellLength+self.gridmargin, self.canLength-self.gridmargin, i*self.cellLength+self.gridmargin, width=3)
            else:
                self.canvas.create_line(self.gridmargin, i*self.cellLength+self.gridmargin, self.canLength-self.gridmargin, i*self.cellLength+self.gridmargin)
        for j in range(10):
            if j % 3 == 0:
                self.canvas.create_line(j*self.cellLength+self.gridmargin, self.gridmargin, j*self.cellLength+self.gridmargin, self.canLength-self.gridmargin, width=3)
            else:
                self.canvas.create_line(j*self.cellLength+self.gridmargin, self.gridmargin, j*self.cellLength+self.gridmargin, self.canLength-self.gridmargin)

        # add side menu
        menuFrame = tk.Frame(self, width=50, bg="#3d3d3d")
        menuFrame.pack(side="right", expand="yes", fill="both")
        tk.Label(menuFrame, text="Sudoku", font="Helvetica 18 bold", bg="#3d3d3d", fg="#ffffff", pady=10).pack()
        tk.Button(menuFrame, text="New Game", font="Courier 14", width=15, command=self.newGame, bg="#3d3d3d", fg="#ffffff").pack()
        tk.Button(menuFrame, text="Check Conditions", font="Courier 14", width=15, command=self.checkConditions, bg="#3d3d3d", fg="#ffffff").pack()
        tk.Button(menuFrame, text="Solve", width=15, font="Courier 14", command=self.solve, bg="#3d3d3d", fg="#ffffff").pack()
        tk.Button(menuFrame, text="Exit", width=15, font="Courier 14", command=self.exitApp, bg="#3d3d3d", fg="#ffffff").pack()
        tk.Label(menuFrame, font="Courier 16", anchor="center", bg="#3d3d3d", fg="#ffffff").pack(fill="none", expand=True)
        tk.Label(menuFrame, text="00:00:00", font="Courier 14", bg="#3d3d3d", fg="#ffffff").pack(side="bottom")
        tk.Label(menuFrame, text="Time", font="Courier 14", bg="#3d3d3d", fg="#ffffff").pack(side="bottom")

    def placeSudoku(self, gameField):
        offset = self.gridmargin+0.5*self.cellLength
        for i in range(9):
            for j in range(9):
                curr = self.sudoku.field[i*9+j]
                if curr > 0:
                    label = tk.Label(self.canvas, text=self.sudoku.field[i*9+j], bg="white", font="Courier 16 bold")
                    self.canvas.create_window(i*self.cellLength+offset, j*self.cellLength+offset, window=label, width=0.9*self.cellLength, height=0.9*self.cellLength)
                else:
                    entry= tk.Entry(self.canvas, bg="white", font="Courier 16", justify="center", relief="flat")
                    self.canvas.create_window(i*self.cellLength+offset, j*self.cellLength+offset, window=entry, width=0.9*self.cellLength, height=0.9*self.cellLength)

    def newGame(self):
        self.sudoku = sudoku.Sudoku()
        self.placeSudoku(self.sudoku.field)

    def checkConditions(self):
        pass

    def solve(self):
        pass

    def exitApp(self):
        self.master.destroy()