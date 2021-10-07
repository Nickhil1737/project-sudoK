from tkinter import *
from tkinter import ttk
import numpy as np

class SudoKo:
    def __init__(self,threadob):
        self.root = Tk()
        self.root.title('SudoKo')
        self.root.geometry("400x400")
        self.matrix = np.zeros((9,9))
        self.set_names = []
        self.row_sets = []
        self.col_sets = []
        self.set_sets = []
        self.make_sets()
        self.thread_websocket = threadob
        self.clickers = []

# Drop Down Boxes

        self.options = [
            "","1","2","3","4","5","6","7","8","9" ]	
        self.clicked00 = StringVar()
        self.clicked00.set(self.options[0])
        self.drop00 = OptionMenu(self.root, self.clicked00, *self.options, command=self.clicker00)
        self.drop00.grid(row=0,column=0)
        self.clicked01 = StringVar()
        self.clicked01.set(self.options[0])
        self.drop01 = OptionMenu(self.root, self.clicked01, *self.options, command=self.clicker01)
        self.drop01.grid(row=0,column=1)
        self.clicked02 = StringVar()
        self.clicked02.set(self.options[0])
        self.drop02 = OptionMenu(self.root, self.clicked02, *self.options, command=self.clicker02)
        self.drop02.grid(row=0,column=2)
        self.clicked10 = StringVar()
        self.clicked10.set(self.options[0])
        self.drop10 = OptionMenu(self.root, self.clicked10, *self.options, command=self.clicker10)
        self.drop10.grid(row=1,column=0)
        self.clicked11 = StringVar()
        self.clicked11.set(self.options[0])
        self.drop11 = OptionMenu(self.root, self.clicked11, *self.options, command=self.clicker11)
        self.drop11.grid(row=1,column=1)
        self.clicked12 = StringVar()
        self.clicked12.set(self.options[0])
        self.drop12 = OptionMenu(self.root, self.clicked12, *self.options, command=self.clicker12)
        self.drop12.grid(row=1,column=2)
        self.clicked20 = StringVar()
        self.clicked20.set(self.options[0])
        self.drop20 = OptionMenu(self.root, self.clicked20, *self.options, command=self.clicker20)
        self.drop20.grid(row=2,column=0)
        self.clicked21 = StringVar()
        self.clicked21.set(self.options[0])
        self.drop21 = OptionMenu(self.root, self.clicked21, *self.options, command=self.clicker21)
        self.drop21.grid(row=2,column=1)
        self.clicked22 = StringVar()
        self.clicked22.set(self.options[0])
        self.drop22 = OptionMenu(self.root, self.clicked22, *self.options, command=self.clicker22)
        self.drop22.grid(row=2,column=2)

        self.clickers.append(self.clicked00)
        self.clickers.append(self.clicked01)
        self.clickers.append(self.clicked02)
        self.clickers.append(self.clicked10)
        self.clickers.append(self.clicked11)
        self.clickers.append(self.clicked12)
        self.clickers.append(self.clicked20)
        self.clickers.append(self.clicked21)
        self.clickers.append(self.clicked22)

            

        # self.root.mainloop()

    def clicker00 (self,event):
        myLabel = Label(self.root, text=self.clicked00.get()).grid(row=10,column=8)
        val = 0
        if self.clicked00.get() != "":
            val = int(self.clicked00.get())
        if self.check_sudoko_property(0,0,val) == False:
            self.clicked00.set("")
    def clicker01 (self,event):
        myLabel = Label(self.root, text=self.clicked01.get()).grid(row=10,column=8)
        val = 0
        if self.clicked01.get() != "":
            val = int(self.clicked01.get())
        if self.check_sudoko_property(0,1,val) == False:
            self.clicked01.set("")
    def clicker02 (self,event):
        myLabel = Label(self.root, text=self.clicked02.get()).grid(row=10,column=8)
        val = 0
        if self.clicked02.get() != "":
            val = int(self.clicked02.get())
        if self.check_sudoko_property(0,2,val) == False:
            self.clicked02.set("")
    def clicker10 (self,event):
        myLabel = Label(self.root, text=self.clicked10.get()).grid(row=10,column=8)
        val = 0
        if self.clicked10.get() != "":
            val = int(self.clicked10.get())
        if self.check_sudoko_property(1,0,val) == False:
            self.clicked10.set("")
    def clicker11 (self,event):
        myLabel = Label(self.root, text=self.clicked11.get()).grid(row=10,column=8)
        val = 0
        if self.clicked11.get() != "":
            val = int(self.clicked11.get())
        if self.check_sudoko_property(1,1,val) == False:
            self.clicked11.set("")
    def clicker12 (self,event):
        myLabel = Label(self.root, text=self.clicked12.get()).grid(row=10,column=8)
        val = 0
        if self.clicked12.get() != "":
            val = int(self.clicked12.get())
        if self.check_sudoko_property(1,2,val) == False:
            self.clicked12.set("")
    def clicker20 (self,event):
        myLabel = Label(self.root, text=self.clicked20.get()).grid(row=10,column=8)
        val = 0
        if self.clicked20.get() != "":
            val = int(self.clicked20.get())
        if self.check_sudoko_property(2,0,val) == False:
            self.clicked20.set("")
    def clicker21 (self,event):
        myLabel = Label(self.root, text=self.clicked21.get()).grid(row=10,column=8)
        val = 0
        if self.clicked21.get() != "":
            val = int(self.clicked21.get())
        if self.check_sudoko_property(2,1,val) == False:
            self.clicked21.set("")
    def clicker22 (self,event):
        myLabel = Label(self.root, text=self.clicked22.get()).grid(row=10,column=8)
        val = 0
        if self.clicked22.get() != "":
            val = int(self.clicked22.get())
        if self.check_sudoko_property(2,2,val) == False:
            self.clicked22.set("")


    def check_sudoko_property(self,r,c,val,dosend=True):
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
        if dosend:
            self.thread_websocket.do_activate(str(r)+str(c)+str(val))
        else:
            self.clickers[3*r+c].set(str(val))
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
