import asyncio
import websockets
from tictac import TicTac
async def gameon():
    uri = "ws://127.0.0.1:8765"
    async with websockets.connect(uri) as websocket:
        t1 = TicTac()
        t1.show_tictac()
        r = int(input("Enter row\t"))
        c = int(input("Enter column\t"))
        t1.play_move(r,c)
        t1.show_tictac()

        await websocket.send(str(r)+str(c))

        s = await websocket.recv()
        r = int(s[0])
        c = int(s[1])
        t1.play_move(r,c,1)
        t1.show_tictac()

asyncio.get_event_loop().run_until_complete(gameon())

