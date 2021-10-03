import os
from tictac import TicTac
import asyncio
import websockets
import threading

class WebSocketThread (threading.Thread):
    global t1
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
        t1.bclick(int(data))

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

t1 = TicTac(threadWebSocket)
t1.root.mainloop()
