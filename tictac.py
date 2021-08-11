import os
import numpy

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
        arr = numpy.zeros((3,3))
        for i in range(0,3):
            for j in range(0,3):
                print(self.s[i*2+2][j*2+3],end = '')
                if self.s[i*2+2][j*2+3] == 'X':
                    arr[i][j] += 1
                elif self.s[i*2+2][j*2+3] == 'O':
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


if __name__ == "main":
    t1 = TicTac()
    t1.show_tictac()
    t1.play_move(2,0,1)
    t1.play_move(1,1,1)
    t1.play_move(0,2,1)
    t1.show_tictac()

    t1.check_winner()
