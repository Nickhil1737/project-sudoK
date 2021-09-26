import asyncio
import websockets

# from tictac import TicTac
async def gameon (websocket,path):
    s = await websocket.recv()
    r = int(s)
    print(r)
    # t1.play_move(r,c)
    # t1.show_tictac()
    r = int(input("enter row\t"))
    c = int(input("enter column\t"))

    t1.play_move(r,c,1)
    t1.show_tictac()
    await websocket.send(str(r)+str(c))

start_server = websockets.serve(gameon,'127.0.0.1',8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
