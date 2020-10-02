class Sudoku:

    def __init__(self):
        # example sudoku field
        self.field = [0, 0, 8, 6, 0, 2, 0, 3, 0, 
                    0, 2, 0, 0, 0, 8, 4, 0, 0, 
                    0, 0, 0, 0, 0, 0, 1, 8, 0,
                    0, 6, 0, 0, 3, 0, 8, 0, 4,
                    0, 4, 0, 5, 0, 0, 0, 0, 7,
                    7, 1, 5, 0, 4, 0, 9, 0, 0,
                    0, 3, 0, 0, 8, 4, 0, 0, 0,
                    0, 8, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 4, 0, 6, 1, 7, 9, 8]

    def checkValid(self):
        # check rows
        for i in range(9):
            numbers = list()
            for j in range(9):
                curr = self.field[i*9+j]
                if curr > 0 and curr not in numbers:
                    numbers.append(curr)
                elif curr > 0:
                    return False
        # check columns
        for i in range(9):
            numbers = list()
            for j in range(9):
                curr = self.field[j*9+i]
                if curr > 0 and curr not in numbers:
                    numbers.append(curr)
                elif curr > 0:
                    return False
        # check boxes
        for i in range(3):
            for j in range(3):
                if not self.checkBoxValid(i*27+j*3):
                    return False
        return True

    def checkBoxValid(self, pos):
        numbers = list()
        for i in range(3):
            for j in range(3):
                curr = self.field[pos+i*9+j]
                if curr > 0 and curr not in numbers:
                    numbers.append(curr)
                elif curr > 0:
                    return False
        return True

sudoku = Sudoku()
print(sudoku.checkValid())