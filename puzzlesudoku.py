import random


class CreateSudokuPuzzle:
    def __init__(self):
        perm = [i for i in range(1,9+1)]
        random.shuffle(perm)
        print(perm)
        self.sudoku = [[0 for i in range(9)] for j in range(9)]
        k = -1
        for i in range(9):
            if (i%3 == 0):
                k += 1
            for j in range(9):
                self.sudoku[i][j] = perm[k]
                k = (k+1)%9
            k = (k+3)%9
        for x in self.sudoku:
            print(x)

        arrp = [i for i in range(81)]
        random.shuffle(arrp)
        x = random.randint(16,20)
        self.arrp = arrp[:x]

