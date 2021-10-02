import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import numpy

from tkinter import *
import json
import asyncio
import websockets
import threading

class WebSocketThread (threading.Thread):
    global buttons,clicked,count,root
    '''WebSocketThread will make websocket run in an a new thread'''
    
    # overide self init
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        self.uri = "ws://127.0.0.1:6789"
        # self.USERS = set()
        print("Start thread", self.name)

    # overide run method
    def run(self):
        # must set a new loop for asyncio
        asyncio.set_event_loop(asyncio.new_event_loop())
        # setup a server
        asyncio.get_event_loop().run_until_complete(self.listen())
        # keep thread running
        asyncio.get_event_loop().run_forever()

    # listener    
    async def listen(self):
        # x = buttons[0]
        # b_click(x)
        '''listenner is called each time new client is connected
        websockets already ensures that a new thread is run for each client'''
        print("listen is called")
        async with websockets.connect(self.uri) as websocket:
            while True:
                print(" inside listen is called")
                s = await websocket.recv()
                print("recieved ",s)
                await self.handle_message(int(s))

            
    # message handler        
    async def handle_message(self,data):
        print("handle_message: ", data)
        cnt = 0
        for x in buttons:
            if cnt == int(data):
                bclick(x)
                break
            cnt += 1

    # example of an action
    # action: notify

    # action: action
    async def action(self,cnt):
        async with websockets.connect(self.uri) as websocket:
            message = str(cnt)
            print("sending" ,message)
            await websocket.send(message)

    # expose action
    def do_activate(self,cnt):
        '''this method is exposed to outside, not an async coroutine'''
        # use asyncio to run action
        # must call self.action(), not use self.action, because it must be a async coroutine
        asyncio.get_event_loop().run_until_complete(self.action(cnt))


threadWebSocket = WebSocketThread("websocket_server")
threadWebSocket.start()

def game_over():
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
    return True

def check_winner ():
    global buttons,clicked,count,root
    arr = numpy.zeros((3,3))
    cnt = 0
    for x in buttons:
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
        return game_over()
    elif colsum[0] == 3 or colsum[1] == 3 or colsum[2] == 3 or colsum[0] == -3 or colsum[1] == -3 or colsum[2] == -3:
        return game_over()
    elif abs(arr[0][0]+arr[1][1]+arr[2][2]) == 3 or abs(arr[0][2]+arr[1][1]+arr[2][0]) == 3:
        return game_over()
    elif count == 9:
        return game_over()
    return False
        
def clicked():
    global buttons,clicked,count,root
    #threadWebSocket.do_activate()
    lbl.configure(text="Button was clicked !!")
def bclick(b):
    global buttons,clicked,count,root
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", "Hey X won" )
            root.destroy()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", "Hey O won" )
            root.destroy()
        #self.checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )

def b_click(b):
    global buttons,clicked,count,root
    cnt = 0
    for x in buttons:
        if x == b:
            break
        cnt += 1
    
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        threadWebSocket.do_activate(cnt)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", "Hey X won" )
            root.destroy()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        threadWebSocket.do_activate(cnt)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", "Hey O won" )
            root.destroy()
        #self.checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )


# 3 X 3 tictac

root = Tk()
root.title('Tic-Tac-Toe')
clicked = True
count = 0
R = -1
C = -1
# btn = Button(root, text="Start Me", command=clicked)
# btn.grid(column=4, row=2)
b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b3))
b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b6))
b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="white", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
root.mainloop()
