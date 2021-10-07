# Sudoku Pair Play Game
A 2 player Sudoku interactive game built on top of python tkinter,asyncio, websockets, and threading where two players can solve the sudoku puzzle together sitting on different computers connected to internet.

### Installation and execution
* clone the git repo
```
git clone https://github.com/Nickhil1737/project-sudoK.git
```
```
cd project-sudoK
```
* create a python venv and install requirements via pip
``` 
pip install -r requirements.txt
```

* one player should run the server program
```
python sudoserver.py [ipaddress]
```

* after this the other player should run client program
```
python sudoclient.py [same ip address]
```

