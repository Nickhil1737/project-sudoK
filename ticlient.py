import asyncio
import websockets
# from tictac import TicTac
async def gameon():
    uri = "ws://127.0.0.1:6789"
    async with websockets.connect(uri) as websocket:
        # t1 = TicTac()
        # print(glistc)
        #t1.show_tictac()
        #r = int(input("Enter button\t"))
        #await websocket.send(str(r))
        s = await websocket.recv()
        print("recieved ",s)
        #c = int(input("Enter column\t"))
        #t1.play_move(r,c)
        #t1.show_tictac()

        r = int(input("Enter button\t"))
        await websocket.send(str(r))
        s = await websocket.recv()
        print("recieved ",s)

        r = int(input("Enter button\t"))
        await websocket.send(str(r))
        s = await websocket.recv()
        print("recieved ",s)
        # r = int(s[0])
        # c = int(s[1])
        #t1.play_move(r,c,1)
        #t1.show_tictac()
        s = await websocket.recv()
        print("recieved ",s)
        s = await websocket.recv()
        print("recieved ",s)

asyncio.get_event_loop().run_until_complete(gameon())

