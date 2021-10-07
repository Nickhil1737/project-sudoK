from tkinter import *
from tkinter import ttk
import numpy as np

class SudoKo:
    def __init__(self):
        self.root = Tk()
        self.root.title('SudoKo')
        self.root.geometry("400x400")
        self.matrix = np.zeros((9,9))
        self.set_names = []
        self.row_sets = []
        self.col_sets = []
        self.set_sets = []
        self.make_sets()

# Drop Down Boxes

        self.options = [
            "","1","2","3","4","5","6","7","8","9" ]	

        self.clicked00 = StringVar()
        self.clicked00.set(self.options[0])
        self.drop00 = OptionMenu(self.root, self.clicked00, *self.options, command=self.clicker00)
        self.drop00.grid(row=0,column=0)
            

        self.root.mainloop()

    def clicker00 (self,event):
        myLabel = Label(self.root, text=self.clicked00.get()).grid(row=10,column=8)
        val = 0
        if self.clicked00.get() != "":
            val = int(self.clicked00.get())
        if self.check_sudoko_property(0,0,val) == False:
            self.clicked00.set("")


    def check_sudoko_property(self,r,c,val):
        if val in self.row_sets[r]:
            myLabel = Label(self.root, text="found similar value in row").grid(row=4,column=8)
            return False
        if val in self.col_sets[c]:
            myLabel = Label(self.root, text="found similar value in column").grid(row=4,column=8)
            return False
        setnum = 0
        for x in range(9):
            if (r,c) in self.set_sets[x]:
                print("found the set",x)
                setnum = x
                break
        if val in self.set_sets[setnum]:
            myLabel = Label(self.root, text="found similar value in 3X3 box").grid(row=4,column=8)
            return False
        preval = self.matrix[r][c]
        if preval != 0:
            self.row_sets[r].erase(preval)
            self.col_sets[c].erase(preval)
            self.set_sets[setnum].erase(preval)
        if val == 0:
            self.matrix[r][c] = 0
            return True
        self.matrix[r][c] = val
        self.row_sets[r].add(val)
        self.col_sets[c].add(val)
        self.set_sets[setnum].add(val)
        return True

    def make_sets(self):
        setnames = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                setnames.append((i,j))
        # print(setnames)
        for cnt in range(9):
            self.set_sets.append(set())
            self.set_names.append(set())
            self.row_sets.append(set())
            self.col_sets.append(set())
            r,c = setnames[cnt]
            for i in range(3):
                for j in range(3):
                    self.set_names[cnt].add((r+i,c+j))
        # for x in self.set_names:
            # print(x)

s = SudoKo()
