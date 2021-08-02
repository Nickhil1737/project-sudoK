import os

class TicTac:
    def __init__ (self):
        borders = ['│', '─','┌', '┬', '┐', '├', '┼', '┤','└', '┴', '┘',]
        # 3 X 3 tictac
        s = []
        s.append(list("  0  1  2"))
        s.append(list("  "+borders[2]+borders[1]+borders[3]+ borders[1]+borders[3]+  borders[1]+borders[4] ))
        s.append(list("0 "+borders[0] + ' '+ borders[0] + ' ' + borders[0] + ' '+ borders[0]))

        s.append(list("  "+borders[5]+borders[1]+borders[6]+ borders[1]+borders[6]+  borders[1]+borders[7] ))
        s.append(list("1 "+borders[0] + ' '+ borders[0] + ' ' + borders[0] + ' '+ borders[0]))

        s.append(list("  "+borders[5]+borders[1]+borders[6]+ borders[1]+borders[6]+  borders[1]+borders[7] ))
        s.append(list("2 "+borders[0] + ' '+ borders[0] + ' ' + borders[0] + ' '+ borders[0]))

        s.append(list("  "+borders[8]+borders[1]+borders[9]+ borders[1]+borders[9]+  borders[1]+borders[10] ))

        self.s = s

    
    def play_move (self,i,j,flip = False):
        self.s[2*i+2][3+j*2] = 'X'
        if flip:    self.s[2*i+2][3+j*2] = 'O'

    def show_tictac (self):
        for row in self.s:
            for col in row:
                print(col,end='')
            print()

    def check_winner (self):
        for i in range(2,8,2):
            for j in range(3,8,2):
                arr[i-2][j-3] = 0
                if self.s[i][j] == 'X':
                    arr[i-2][j-3] += 1
                elif self.s[i][j] == 'O':
                    arr[i-2][j-3] -= 1
        return False
    def game_over(self):
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




t1 = TicTac()
t1.show_tictac()
t1.play_move(2,0)
t1.play_move(1,0,1)
t1.play_move(0,0)
t1.show_tictac()

t1.game_over()

