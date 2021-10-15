import random


class CreateSudokuPuzzle:
    def __init__(self):
        perm = [i for i in range(1,9+1)]
        random.shuffle(perm)
        self.sudoku = [[0 for i in range(9)] for j in range(9)]
        k = -1
        for i in range(9):
            if (i%3 == 0):
                k += 1
            for j in range(9):
                self.sudoku[i][j] = perm[k]
                k = (k+1)%9
            k = (k+3)%9

        arrp = [i for i in range(81)]
        random.shuffle(arrp)
        arrp = arrp[:random.randint(16,20)]
        filled_set = set()
        self.filled_boxes = []
        for x in arrp:
            r = x//9
            c = x%9
            filled_set.add((r,c))
        for i in range(9):
            for j in range(9):
                if (i,j) not in filled_set:
                    self.sudoku[i][j] = 0
        with open("sudoku_state_zero.txt","w") as fileob:
            for i in range(9):
                for j in range(9):
                    fileob.write(str(self.sudoku[i][j]))
                fileob.write('\n')


# t1 = CreateSudokuPuzzle()
# print(t1.filled_boxes)

