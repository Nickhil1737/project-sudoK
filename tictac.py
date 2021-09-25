import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy

class TicTac:
    def __init__ (self):
        # 3 X 3 tictac
        self.root = Tk()
        self.R = -1
        self.C = -1
        self.s = []
        self.root.title('Tic-Tac-Toe')
        self.clicked = True
        self.count = 0
        i = 0
        j = 0
        self.b1 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b1))
        self.b2 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b2))
        self.b3 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b3))
        self.b4 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b4))
        self.b5 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b5))
        self.b6 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b6))
        self.b7 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b7))
        self.b8 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b8))
        self.b9 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b9))
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.buttons = [self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9,]

        self.root.mainloop()

    def b_click(self,b):
        cnt = 0
        for x in self.buttons:
            if x == b:
                self.R = cnt//3
                self.C = cnt % 3
            cnt += 1
        
        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Hey X won" )
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", "Hey O won" )
            #self.checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )

    
    #def play_move (self,i,j,flip = False):
        #self.s[2*i+2][3+j*2] = 'X'
        #if flip:    self.s[2*i+2][3+j*2] = 'O'

    #def show_tictac (self):
        #for row in self.s:
            #for col in row:
                #print(col,end='')
            #print()

    def check_winner (self):
        arr = numpy.zeros((3,3))
        cnt = 0
        for x in self.buttons:
            if x["text"] == "X":
                i = cnt//3
                j = cnt%3
                arr[i][j] += 1
            elif x["text"] == "O":
                i = cnt//3
                j = cnt%3
                arr[i][j] -= 1
                #elif self.s[i][j]["text"] == 'O':
                #    arr[i][j] -= 1
            cnt += 1
        colsum = numpy.sum(arr,axis=0)
        rowsum = numpy.sum(arr,axis=1)
        if rowsum[0] == 3 or rowsum[1] == 3 or rowsum[2] == 3 or rowsum[0] == -3 or rowsum[1] == -3 or rowsum[2] == -3:
            return self.game_over()
        elif colsum[0] == 3 or colsum[1] == 3 or colsum[2] == 3 or colsum[0] == -3 or colsum[1] == -3 or colsum[2] == -3:
            return self.game_over()
        elif abs(arr[0][0]+arr[1][1]+arr[2][2]) == 3 or abs(arr[0][2]+arr[1][1]+arr[2][0]) == 3:
            return self.game_over()
        elif self.count == 9:
            return self.game_over()
        return False
        
        

    def game_over(self):
        #messagebox.showinfo("We have a winner")
        print("\n\n")
        print( "███▀▀▀██ ███▀▀▀███ ███▀█▄█▀███ ██▀▀▀")
        print( "██    ██ ██     ██ ██   █   ██ ██   ")
        print( "██   ▄▄▄ ██▄▄▄▄▄██ ██   ▀   ██ ██▀▀▀")
        print( "██    ██ ██     ██ ██       ██ ██   ")
        print( "███▄▄▄██ ██     ██ ██       ██ ██▄▄▄")
        print( "                                    ")
        print( "███▀▀▀███ ▀███  ██▀ ██▀▀▀ ██▀▀▀▀██▄ ")
        print( "██     ██   ██  ██  ██    ██     ██ ")
        print( "██     ██   ██  ██  ██▀▀▀ ██▄▄▄▄▄▀▀ ")
        print( "██     ██   ██  █▀  ██    ██     ██ ")
        print( "███▄▄▄███    ▀█▀    ██▄▄▄ ██     ██▄")
        print("\n\n")
        self.root.destroy()
        return True

#t1 = TicTac()

