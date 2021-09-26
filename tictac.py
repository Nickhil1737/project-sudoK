import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy
# this demonstrates a simple websocket server with GUI which sends messages to its clients
# vuquangtrong@gmail.com

from tkinter import *
import json
import asyncio
import websockets
import threading

class WebSocketThread (threading.Thread):
    '''WebSocketThread will make websocket run in an a new thread'''
    
    # overide self init
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        self.USERS = set()
        print("Start thread", self.name)

    # overide run method
    def run(self):
        # must set a new loop for asyncio
        asyncio.set_event_loop(asyncio.new_event_loop())
        # setup a server
        asyncio.get_event_loop().run_until_complete(websockets.serve(self.listen, 'localhost', 6789))
        # keep thread running
        asyncio.get_event_loop().run_forever()

    # listener    
    async def listen(self, websocket, path):
        '''listenner is called each time new client is connected
        websockets already ensures that a new thread is run for each client'''

        print("listen: ", websocket)
        
        # register new client #
        self.USERS.add(websocket)
        await self.notify_users()

        # this loop to get massage from client #
        while True:
            try:
                msg = await websocket.recv()
                if msg is None:
                    break
                await self.handle_message(client, msg)

            except websockets.exceptions.ConnectionClosed:
                print("close: ", websocket)
                break

        self.USERS.remove(websocket)
        await self.notify_users()
    
    # message handler        
    async def handle_message(self, client, data):
        print("handle_message: ", client, data)

    # example of an action
    # action: notify
    async def notify_users(self):
        '''notify the number of current connected clients'''
        if self.USERS: # asyncio.wait doesn't accept an empty list
            message = json.dumps({'type': 'users', 'count': len(self.USERS)})
            await asyncio.wait([user.send(message) for user in self.USERS])

    # action: action
    async def action(self):
        #self.tic.blick(0,1)
        '''this is an action which will be executed when user presses on button'''
        if self.USERS: # asyncio.wait doesn't accept an empty list
            message = json.dumps({'type': 'activation', 'count':'true'})
            await asyncio.wait([user.send(message) for user in self.USERS])

    # expose action
    def do_activate(self):
        '''this method is exposed to outside, not an async coroutine'''
        # use asyncio to run action
        # must call self.action(), not use self.action, because it must be a async coroutine
        asyncio.get_event_loop().run_until_complete(self.action())


# start WebSocketThread #

# helper function for window
    
# tkinter application
#window = Tk()

# set up GUI #
#window.title("tkinter GUI")
#window.geometry('200x120')
 
#lbl = Label(window, text="Hello")
#lbl.grid(column=0, row=0)

#self.btn = Button(window, text="Start Me", command=clicked)
#self.btn.grid(column=4, row=2)

# start GUI #
#window.mainloop()
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
        self.btn = Button(window, text="Start Me", command=clicked)
        self.btn.grid(column=4, row=2)
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
    def clicked(self):
        self.threadWebSocket.do_activate()
        lbl.configure(text="Button was clicked !!")
    def bclick(self,r,c):
        d = r*3+c
        cnt = 0
        for x in self.buttons:
            if cnt == d:
                self.b_click(x)
            cnt += 1
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
        #ticlient.glistc.append((self.R,self.C))

    
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


threadWebSocket=WebSocketThread("websocket_server")
threadWebSocket.start()
t1 = TicTac(threadWebSocket)
