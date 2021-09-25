from tkinter import *
from tkinter import messagebox
import tkinter as tk

# disable all the buttons
def disable_all_buttons():
	b1.config(state=DISABLED)
	b2.config(state=DISABLED)
	b3.config(state=DISABLED)
	b4.config(state=DISABLED)
	b5.config(state=DISABLED)
	b6.config(state=DISABLED)
	b7.config(state=DISABLED)
	b8.config(state=DISABLED)
	b9.config(state=DISABLED)

class Game():
    def __init__(self,master=None):
        #super().__init__(master)
        #self.master = master
        self.root = Tk()
        self.root.title('Tic-Tac-Toe')
        self.clicked = True
        self.count = 0

        self.reset()
        self.root.mainloop()
#root.iconbitmap('c:/gui/codemy.ico')
#root.geometry("1200x710")

# X starts so true

    def create_restart(self):
        self.restart = tk.Button(text="RESTART", fg="red", command=self.reset)
        self.restart.grid(row = 3,column = 2)


# Check to see if someone won
    def checkifwon(self):
        self.winner = False

        if self.b1["text"] == "X" and self.b2["text"] == "X" and self.b3["text"]  == "X":
            self.b1.config(bg="red")
            self.b2.config(bg="red")
            self.b3.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()
        elif self.b4["text"] == "X" and self.b5["text"] == "X" and self.b6["text"]  == "X":
            self.b4.config(bg="red")
            self.b5.config(bg="red")
            self.b6.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b7["text"] == "X" and self.b8["text"] == "X" and self.b9["text"]  == "X":
            self.b7.config(bg="red")
            self.b8.config(bg="red")
            self.b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b1["text"] == "X" and self.b4["text"] == "X" and self.b7["text"]  == "X":
            self.b1.config(bg="red")
            self.b4.config(bg="red")
            self.b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b2["text"] == "X" and self.b5["text"] == "X" and self.b8["text"]  == "X":
            self.b2.config(bg="red")
            self.b5.config(bg="red")
            self.b8.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b3["text"] == "X" and self.b6["text"] == "X" and self.b9["text"]  == "X":
            self.b3.config(bg="red")
            self.b6.config(bg="red")
            self.b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b1["text"] == "X" and self.b5["text"] == "X" and self.b9["text"]  == "X":
            self.b1.config(bg="red")
            self.b5.config(bg="red")
            self.b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        elif self.b3["text"] == "X" and self.b5["text"] == "X" and self.b7["text"]  == "X":
            self.b3.config(bg="red")
            self.b5.config(bg="red")
            self.b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            #disable_all_buttons()

        #### CHECK FOR O's Win
        elif self.b1["text"] == "O" and self.b2["text"] == "O" and self.b3["text"]  == "O":
            self.b1.config(bg="red")
            self.b2.config(bg="red")
            self.b3.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()
        elif self.b4["text"] == "O" and self.b5["text"] == "O" and self.b6["text"]  == "O":
            self.b4.config(bg="red")
            self.b5.config(bg="red")
            self.b6.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b7["text"] == "O" and self.b8["text"] == "O" and self.b9["text"]  == "O":
            self.b7.config(bg="red")
            self.b8.config(bg="red")
            self.b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b1["text"] == "O" and self.b4["text"] == "O" and self.b7["text"]  == "O":
            self.b1.config(bg="red")
            self.b4.config(bg="red")
            self.b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b2["text"] == "O" and self.b5["text"] == "O" and self.b8["text"]  == "O":
            self.b2.config(bg="red")
            self.b5.config(bg="red")
            self.b8.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b3["text"] == "O" and self.b6["text"] == "O" and self.b9["text"]  == "O":
            self.b3.config(bg="red")
            self.b6.config(bg="red")
            self.b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b1["text"] == "O" and self.b5["text"] == "O" and self.b9["text"]  == "O":
            self.b1.config(bg="red")
            self.b5.config(bg="red")
            self.b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        elif self.b3["text"] == "O" and self.b5["text"] == "O" and self.b7["text"]  == "O":
            self.b3.config(bg="red")
            self.b5.config(bg="red")
            self.b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            #disable_all_buttons()

        # Check if tie
        if self.count == 9 and self.winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
            #disable_all_buttons()
				
# Button clicked function
    def b_click(self,b):
        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            self.checkifwon()
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.checkifwon()
        else:
            messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )

# Start the game over!
    def reset(self):
        self.create_restart()
        self.clicked = True
        self.count = 0

        # Build our buttons
        self.b1 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b1))
        self.b2 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b2))
        self.b3 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b3))

        self.b4 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b4))
        self.b5 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b5))
        self.b6 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b6))

        self.b7 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b7))
        self.b8 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b8))
        self.b9 = Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: self.b_click(self.b9))

        # Grid our buttons to the screen
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.root.mainloop()

# Create menue
#my_menu = Menu(root)
#root.config(menu=my_menu)

# Create Options Menu
#options_menu = Menu(my_menu, tearoff=False)
#my_menu.add_cascade(label="Options", menu=options_menu)
#options_menu.add_command(label="Rest Game", command=reset)

#reset()

ob = Game()
# root.mainloop()
