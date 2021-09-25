import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy

def b_click(b):
    global s,clicked,count,root
    r = -1
    c = -1
    for i in range(0,3):
        for j in range(0,3):
            if s[i][j] == b:
                r = i
                c = j

    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        #self.check_winner()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        #self.checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )
# 3 X 3 tictac
root = Tk()
s = []
root.title('Tic-Tac-Toe')
clicked = True
count = 0

for i in range(0,3):
    s.append([])
    for j in range(0,3):
        b = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b))
        b.grid(row=i, column=j)
        s[i].append(b)
root.mainloop()


    
    #def play_move (self,i,j,flip = False):
        #self.s[2*i+2][3+j*2] = 'X'
        #if flip:    self.s[2*i+2][3+j*2] = 'O'

    #def show_tictac (self):
        #for row in self.s:
            #for col in row:
                #print(col,end='')
            #print()

def check_winner ():
    global s,clicked,count,root
    arr = numpy.zeros((3,3))
    for i in range(0,3):
        for j in range(0,3):
            # print(self.s[i*2+2][j*2+3],end = '')
            if s[i][j]["text"] == 'X':
                arr[i][j] += 1
            elif s[i][j]["text"] == 'O':
                arr[i][j] -= 1
    colsum = numpy.sum(arr,axis=0)
    rowsum = numpy.sum(arr,axis=1)
    if rowsum[0] == 3 or rowsum[1] == 3 or rowsum[2] == 3 or rowsum[0] == -3 or rowsum[1] == -3 or rowsum[2] == -3:
        self.game_over()
    elif colsum[0] == 3 or colsum[1] == 3 or colsum[2] == 3 or colsum[0] == -3 or colsum[1] == -3 or colsum[2] == -3:
        self.game_over()
    elif abs(arr[0][0]+arr[1][1]+arr[2][2]) == 3 or abs(arr[0][2]+arr[1][1]+arr[2][0]) == 3:
        self.game_over()



def game_over(self):
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

