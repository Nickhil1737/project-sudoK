from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import numpy as np

class SudoKo:
    def __init__(self,threadob):
        self.root = Tk()
        self.root.title('SudoKo')
        self.root.geometry("400x400")
        self.matrix = np.zeros((9,9))
        self.set_names = []
        self.row_sets = []
        self.col_sets = []
        self.set_sets = []
        self.make_sets()
        self.thread_websocket = threadob
        self.clickers = []

# Drop Down Boxes

        self.options = [
            "","1","2","3","4","5","6","7","8","9" ]	
        self.clicked00 = StringVar()
        self.clicked00.set(self.options[0])
        self.drop00 = OptionMenu(self.root, self.clicked00, *self.options, command=self.clicker00)
        self.drop00.grid(row=0,column=0)
        self.clicked01 = StringVar()
        self.clicked01.set(self.options[0])
        self.drop01 = OptionMenu(self.root, self.clicked01, *self.options, command=self.clicker01)
        self.drop01.grid(row=0,column=1)
        self.clicked02 = StringVar()
        self.clicked02.set(self.options[0])
        self.drop02 = OptionMenu(self.root, self.clicked02, *self.options, command=self.clicker02)
        self.drop02.grid(row=0,column=2)
        self.clicked03 = StringVar()
        self.clicked03.set(self.options[0])
        self.drop03 = OptionMenu(self.root, self.clicked03, *self.options, command=self.clicker03)
        self.drop03.grid(row=0,column=3)
        self.clicked04 = StringVar()
        self.clicked04.set(self.options[0])
        self.drop04 = OptionMenu(self.root, self.clicked04, *self.options, command=self.clicker04)
        self.drop04.grid(row=0,column=4)
        self.clicked05 = StringVar()
        self.clicked05.set(self.options[0])
        self.drop05 = OptionMenu(self.root, self.clicked05, *self.options, command=self.clicker05)
        self.drop05.grid(row=0,column=5)
        self.clicked06 = StringVar()
        self.clicked06.set(self.options[0])
        self.drop06 = OptionMenu(self.root, self.clicked06, *self.options, command=self.clicker06)
        self.drop06.grid(row=0,column=6)
        self.clicked07 = StringVar()
        self.clicked07.set(self.options[0])
        self.drop07 = OptionMenu(self.root, self.clicked07, *self.options, command=self.clicker07)
        self.drop07.grid(row=0,column=7)
        self.clicked08 = StringVar()
        self.clicked08.set(self.options[0])
        self.drop08 = OptionMenu(self.root, self.clicked08, *self.options, command=self.clicker08)
        self.drop08.grid(row=0,column=8)
        self.clicked10 = StringVar()
        self.clicked10.set(self.options[0])
        self.drop10 = OptionMenu(self.root, self.clicked10, *self.options, command=self.clicker10)
        self.drop10.grid(row=1,column=0)
        self.clicked11 = StringVar()
        self.clicked11.set(self.options[0])
        self.drop11 = OptionMenu(self.root, self.clicked11, *self.options, command=self.clicker11)
        self.drop11.grid(row=1,column=1)
        self.clicked12 = StringVar()
        self.clicked12.set(self.options[0])
        self.drop12 = OptionMenu(self.root, self.clicked12, *self.options, command=self.clicker12)
        self.drop12.grid(row=1,column=2)
        self.clicked13 = StringVar()
        self.clicked13.set(self.options[0])
        self.drop13 = OptionMenu(self.root, self.clicked13, *self.options, command=self.clicker13)
        self.drop13.grid(row=1,column=3)
        self.clicked14 = StringVar()
        self.clicked14.set(self.options[0])
        self.drop14 = OptionMenu(self.root, self.clicked14, *self.options, command=self.clicker14)
        self.drop14.grid(row=1,column=4)
        self.clicked15 = StringVar()
        self.clicked15.set(self.options[0])
        self.drop15 = OptionMenu(self.root, self.clicked15, *self.options, command=self.clicker15)
        self.drop15.grid(row=1,column=5)
        self.clicked16 = StringVar()
        self.clicked16.set(self.options[0])
        self.drop16 = OptionMenu(self.root, self.clicked16, *self.options, command=self.clicker16)
        self.drop16.grid(row=1,column=6)
        self.clicked17 = StringVar()
        self.clicked17.set(self.options[0])
        self.drop17 = OptionMenu(self.root, self.clicked17, *self.options, command=self.clicker17)
        self.drop17.grid(row=1,column=7)
        self.clicked18 = StringVar()
        self.clicked18.set(self.options[0])
        self.drop18 = OptionMenu(self.root, self.clicked18, *self.options, command=self.clicker18)
        self.drop18.grid(row=1,column=8)
        self.clicked20 = StringVar()
        self.clicked20.set(self.options[0])
        self.drop20 = OptionMenu(self.root, self.clicked20, *self.options, command=self.clicker20)
        self.drop20.grid(row=2,column=0)
        self.clicked21 = StringVar()
        self.clicked21.set(self.options[0])
        self.drop21 = OptionMenu(self.root, self.clicked21, *self.options, command=self.clicker21)
        self.drop21.grid(row=2,column=1)
        self.clicked22 = StringVar()
        self.clicked22.set(self.options[0])
        self.drop22 = OptionMenu(self.root, self.clicked22, *self.options, command=self.clicker22)
        self.drop22.grid(row=2,column=2)
        self.clicked23 = StringVar()
        self.clicked23.set(self.options[0])
        self.drop23 = OptionMenu(self.root, self.clicked23, *self.options, command=self.clicker23)
        self.drop23.grid(row=2,column=3)
        self.clicked24 = StringVar()
        self.clicked24.set(self.options[0])
        self.drop24 = OptionMenu(self.root, self.clicked24, *self.options, command=self.clicker24)
        self.drop24.grid(row=2,column=4)
        self.clicked25 = StringVar()
        self.clicked25.set(self.options[0])
        self.drop25 = OptionMenu(self.root, self.clicked25, *self.options, command=self.clicker25)
        self.drop25.grid(row=2,column=5)
        self.clicked26 = StringVar()
        self.clicked26.set(self.options[0])
        self.drop26 = OptionMenu(self.root, self.clicked26, *self.options, command=self.clicker26)
        self.drop26.grid(row=2,column=6)
        self.clicked27 = StringVar()
        self.clicked27.set(self.options[0])
        self.drop27 = OptionMenu(self.root, self.clicked27, *self.options, command=self.clicker27)
        self.drop27.grid(row=2,column=7)
        self.clicked28 = StringVar()
        self.clicked28.set(self.options[0])
        self.drop28 = OptionMenu(self.root, self.clicked28, *self.options, command=self.clicker28)
        self.drop28.grid(row=2,column=8)
        self.clicked30 = StringVar()
        self.clicked30.set(self.options[0])
        self.drop30 = OptionMenu(self.root, self.clicked30, *self.options, command=self.clicker30)
        self.drop30.grid(row=3,column=0)
        self.clicked31 = StringVar()
        self.clicked31.set(self.options[0])
        self.drop31 = OptionMenu(self.root, self.clicked31, *self.options, command=self.clicker31)
        self.drop31.grid(row=3,column=1)
        self.clicked32 = StringVar()
        self.clicked32.set(self.options[0])
        self.drop32 = OptionMenu(self.root, self.clicked32, *self.options, command=self.clicker32)
        self.drop32.grid(row=3,column=2)
        self.clicked33 = StringVar()
        self.clicked33.set(self.options[0])
        self.drop33 = OptionMenu(self.root, self.clicked33, *self.options, command=self.clicker33)
        self.drop33.grid(row=3,column=3)
        self.clicked34 = StringVar()
        self.clicked34.set(self.options[0])
        self.drop34 = OptionMenu(self.root, self.clicked34, *self.options, command=self.clicker34)
        self.drop34.grid(row=3,column=4)
        self.clicked35 = StringVar()
        self.clicked35.set(self.options[0])
        self.drop35 = OptionMenu(self.root, self.clicked35, *self.options, command=self.clicker35)
        self.drop35.grid(row=3,column=5)
        self.clicked36 = StringVar()
        self.clicked36.set(self.options[0])
        self.drop36 = OptionMenu(self.root, self.clicked36, *self.options, command=self.clicker36)
        self.drop36.grid(row=3,column=6)
        self.clicked37 = StringVar()
        self.clicked37.set(self.options[0])
        self.drop37 = OptionMenu(self.root, self.clicked37, *self.options, command=self.clicker37)
        self.drop37.grid(row=3,column=7)
        self.clicked38 = StringVar()
        self.clicked38.set(self.options[0])
        self.drop38 = OptionMenu(self.root, self.clicked38, *self.options, command=self.clicker38)
        self.drop38.grid(row=3,column=8)
        self.clicked40 = StringVar()
        self.clicked40.set(self.options[0])
        self.drop40 = OptionMenu(self.root, self.clicked40, *self.options, command=self.clicker40)
        self.drop40.grid(row=4,column=0)
        self.clicked41 = StringVar()
        self.clicked41.set(self.options[0])
        self.drop41 = OptionMenu(self.root, self.clicked41, *self.options, command=self.clicker41)
        self.drop41.grid(row=4,column=1)
        self.clicked42 = StringVar()
        self.clicked42.set(self.options[0])
        self.drop42 = OptionMenu(self.root, self.clicked42, *self.options, command=self.clicker42)
        self.drop42.grid(row=4,column=2)
        self.clicked43 = StringVar()
        self.clicked43.set(self.options[0])
        self.drop43 = OptionMenu(self.root, self.clicked43, *self.options, command=self.clicker43)
        self.drop43.grid(row=4,column=3)
        self.clicked44 = StringVar()
        self.clicked44.set(self.options[0])
        self.drop44 = OptionMenu(self.root, self.clicked44, *self.options, command=self.clicker44)
        self.drop44.grid(row=4,column=4)
        self.clicked45 = StringVar()
        self.clicked45.set(self.options[0])
        self.drop45 = OptionMenu(self.root, self.clicked45, *self.options, command=self.clicker45)
        self.drop45.grid(row=4,column=5)
        self.clicked46 = StringVar()
        self.clicked46.set(self.options[0])
        self.drop46 = OptionMenu(self.root, self.clicked46, *self.options, command=self.clicker46)
        self.drop46.grid(row=4,column=6)
        self.clicked47 = StringVar()
        self.clicked47.set(self.options[0])
        self.drop47 = OptionMenu(self.root, self.clicked47, *self.options, command=self.clicker47)
        self.drop47.grid(row=4,column=7)
        self.clicked48 = StringVar()
        self.clicked48.set(self.options[0])
        self.drop48 = OptionMenu(self.root, self.clicked48, *self.options, command=self.clicker48)
        self.drop48.grid(row=4,column=8)
        self.clicked50 = StringVar()
        self.clicked50.set(self.options[0])
        self.drop50 = OptionMenu(self.root, self.clicked50, *self.options, command=self.clicker50)
        self.drop50.grid(row=5,column=0)
        self.clicked51 = StringVar()
        self.clicked51.set(self.options[0])
        self.drop51 = OptionMenu(self.root, self.clicked51, *self.options, command=self.clicker51)
        self.drop51.grid(row=5,column=1)
        self.clicked52 = StringVar()
        self.clicked52.set(self.options[0])
        self.drop52 = OptionMenu(self.root, self.clicked52, *self.options, command=self.clicker52)
        self.drop52.grid(row=5,column=2)
        self.clicked53 = StringVar()
        self.clicked53.set(self.options[0])
        self.drop53 = OptionMenu(self.root, self.clicked53, *self.options, command=self.clicker53)
        self.drop53.grid(row=5,column=3)
        self.clicked54 = StringVar()
        self.clicked54.set(self.options[0])
        self.drop54 = OptionMenu(self.root, self.clicked54, *self.options, command=self.clicker54)
        self.drop54.grid(row=5,column=4)
        self.clicked55 = StringVar()
        self.clicked55.set(self.options[0])
        self.drop55 = OptionMenu(self.root, self.clicked55, *self.options, command=self.clicker55)
        self.drop55.grid(row=5,column=5)
        self.clicked56 = StringVar()
        self.clicked56.set(self.options[0])
        self.drop56 = OptionMenu(self.root, self.clicked56, *self.options, command=self.clicker56)
        self.drop56.grid(row=5,column=6)
        self.clicked57 = StringVar()
        self.clicked57.set(self.options[0])
        self.drop57 = OptionMenu(self.root, self.clicked57, *self.options, command=self.clicker57)
        self.drop57.grid(row=5,column=7)
        self.clicked58 = StringVar()
        self.clicked58.set(self.options[0])
        self.drop58 = OptionMenu(self.root, self.clicked58, *self.options, command=self.clicker58)
        self.drop58.grid(row=5,column=8)
        self.clicked60 = StringVar()
        self.clicked60.set(self.options[0])
        self.drop60 = OptionMenu(self.root, self.clicked60, *self.options, command=self.clicker60)
        self.drop60.grid(row=6,column=0)
        self.clicked61 = StringVar()
        self.clicked61.set(self.options[0])
        self.drop61 = OptionMenu(self.root, self.clicked61, *self.options, command=self.clicker61)
        self.drop61.grid(row=6,column=1)
        self.clicked62 = StringVar()
        self.clicked62.set(self.options[0])
        self.drop62 = OptionMenu(self.root, self.clicked62, *self.options, command=self.clicker62)
        self.drop62.grid(row=6,column=2)
        self.clicked63 = StringVar()
        self.clicked63.set(self.options[0])
        self.drop63 = OptionMenu(self.root, self.clicked63, *self.options, command=self.clicker63)
        self.drop63.grid(row=6,column=3)
        self.clicked64 = StringVar()
        self.clicked64.set(self.options[0])
        self.drop64 = OptionMenu(self.root, self.clicked64, *self.options, command=self.clicker64)
        self.drop64.grid(row=6,column=4)
        self.clicked65 = StringVar()
        self.clicked65.set(self.options[0])
        self.drop65 = OptionMenu(self.root, self.clicked65, *self.options, command=self.clicker65)
        self.drop65.grid(row=6,column=5)
        self.clicked66 = StringVar()
        self.clicked66.set(self.options[0])
        self.drop66 = OptionMenu(self.root, self.clicked66, *self.options, command=self.clicker66)
        self.drop66.grid(row=6,column=6)
        self.clicked67 = StringVar()
        self.clicked67.set(self.options[0])
        self.drop67 = OptionMenu(self.root, self.clicked67, *self.options, command=self.clicker67)
        self.drop67.grid(row=6,column=7)
        self.clicked68 = StringVar()
        self.clicked68.set(self.options[0])
        self.drop68 = OptionMenu(self.root, self.clicked68, *self.options, command=self.clicker68)
        self.drop68.grid(row=6,column=8)
        self.clicked70 = StringVar()
        self.clicked70.set(self.options[0])
        self.drop70 = OptionMenu(self.root, self.clicked70, *self.options, command=self.clicker70)
        self.drop70.grid(row=7,column=0)
        self.clicked71 = StringVar()
        self.clicked71.set(self.options[0])
        self.drop71 = OptionMenu(self.root, self.clicked71, *self.options, command=self.clicker71)
        self.drop71.grid(row=7,column=1)
        self.clicked72 = StringVar()
        self.clicked72.set(self.options[0])
        self.drop72 = OptionMenu(self.root, self.clicked72, *self.options, command=self.clicker72)
        self.drop72.grid(row=7,column=2)
        self.clicked73 = StringVar()
        self.clicked73.set(self.options[0])
        self.drop73 = OptionMenu(self.root, self.clicked73, *self.options, command=self.clicker73)
        self.drop73.grid(row=7,column=3)
        self.clicked74 = StringVar()
        self.clicked74.set(self.options[0])
        self.drop74 = OptionMenu(self.root, self.clicked74, *self.options, command=self.clicker74)
        self.drop74.grid(row=7,column=4)
        self.clicked75 = StringVar()
        self.clicked75.set(self.options[0])
        self.drop75 = OptionMenu(self.root, self.clicked75, *self.options, command=self.clicker75)
        self.drop75.grid(row=7,column=5)
        self.clicked76 = StringVar()
        self.clicked76.set(self.options[0])
        self.drop76 = OptionMenu(self.root, self.clicked76, *self.options, command=self.clicker76)
        self.drop76.grid(row=7,column=6)
        self.clicked77 = StringVar()
        self.clicked77.set(self.options[0])
        self.drop77 = OptionMenu(self.root, self.clicked77, *self.options, command=self.clicker77)
        self.drop77.grid(row=7,column=7)
        self.clicked78 = StringVar()
        self.clicked78.set(self.options[0])
        self.drop78 = OptionMenu(self.root, self.clicked78, *self.options, command=self.clicker78)
        self.drop78.grid(row=7,column=8)
        self.clicked80 = StringVar()
        self.clicked80.set(self.options[0])
        self.drop80 = OptionMenu(self.root, self.clicked80, *self.options, command=self.clicker80)
        self.drop80.grid(row=8,column=0)
        self.clicked81 = StringVar()
        self.clicked81.set(self.options[0])
        self.drop81 = OptionMenu(self.root, self.clicked81, *self.options, command=self.clicker81)
        self.drop81.grid(row=8,column=1)
        self.clicked82 = StringVar()
        self.clicked82.set(self.options[0])
        self.drop82 = OptionMenu(self.root, self.clicked82, *self.options, command=self.clicker82)
        self.drop82.grid(row=8,column=2)
        self.clicked83 = StringVar()
        self.clicked83.set(self.options[0])
        self.drop83 = OptionMenu(self.root, self.clicked83, *self.options, command=self.clicker83)
        self.drop83.grid(row=8,column=3)
        self.clicked84 = StringVar()
        self.clicked84.set(self.options[0])
        self.drop84 = OptionMenu(self.root, self.clicked84, *self.options, command=self.clicker84)
        self.drop84.grid(row=8,column=4)
        self.clicked85 = StringVar()
        self.clicked85.set(self.options[0])
        self.drop85 = OptionMenu(self.root, self.clicked85, *self.options, command=self.clicker85)
        self.drop85.grid(row=8,column=5)
        self.clicked86 = StringVar()
        self.clicked86.set(self.options[0])
        self.drop86 = OptionMenu(self.root, self.clicked86, *self.options, command=self.clicker86)
        self.drop86.grid(row=8,column=6)
        self.clicked87 = StringVar()
        self.clicked87.set(self.options[0])
        self.drop87 = OptionMenu(self.root, self.clicked87, *self.options, command=self.clicker87)
        self.drop87.grid(row=8,column=7)
        self.clicked88 = StringVar()
        self.clicked88.set(self.options[0])
        self.drop88 = OptionMenu(self.root, self.clicked88, *self.options, command=self.clicker88)
        self.drop88.grid(row=8,column=8)

        self.clickers.append(self.clicked00)
        self.clickers.append(self.clicked01)
        self.clickers.append(self.clicked02)
        self.clickers.append(self.clicked03)
        self.clickers.append(self.clicked04)
        self.clickers.append(self.clicked05)
        self.clickers.append(self.clicked06)
        self.clickers.append(self.clicked07)
        self.clickers.append(self.clicked08)
        self.clickers.append(self.clicked10)
        self.clickers.append(self.clicked11)
        self.clickers.append(self.clicked12)
        self.clickers.append(self.clicked13)
        self.clickers.append(self.clicked14)
        self.clickers.append(self.clicked15)
        self.clickers.append(self.clicked16)
        self.clickers.append(self.clicked17)
        self.clickers.append(self.clicked18)
        self.clickers.append(self.clicked20)
        self.clickers.append(self.clicked21)
        self.clickers.append(self.clicked22)
        self.clickers.append(self.clicked23)
        self.clickers.append(self.clicked24)
        self.clickers.append(self.clicked25)
        self.clickers.append(self.clicked26)
        self.clickers.append(self.clicked27)
        self.clickers.append(self.clicked28)
        self.clickers.append(self.clicked30)
        self.clickers.append(self.clicked31)
        self.clickers.append(self.clicked32)
        self.clickers.append(self.clicked33)
        self.clickers.append(self.clicked34)
        self.clickers.append(self.clicked35)
        self.clickers.append(self.clicked36)
        self.clickers.append(self.clicked37)
        self.clickers.append(self.clicked38)
        self.clickers.append(self.clicked40)
        self.clickers.append(self.clicked41)
        self.clickers.append(self.clicked42)
        self.clickers.append(self.clicked43)
        self.clickers.append(self.clicked44)
        self.clickers.append(self.clicked45)
        self.clickers.append(self.clicked46)
        self.clickers.append(self.clicked47)
        self.clickers.append(self.clicked48)
        self.clickers.append(self.clicked50)
        self.clickers.append(self.clicked51)
        self.clickers.append(self.clicked52)
        self.clickers.append(self.clicked53)
        self.clickers.append(self.clicked54)
        self.clickers.append(self.clicked55)
        self.clickers.append(self.clicked56)
        self.clickers.append(self.clicked57)
        self.clickers.append(self.clicked58)
        self.clickers.append(self.clicked60)
        self.clickers.append(self.clicked61)
        self.clickers.append(self.clicked62)
        self.clickers.append(self.clicked63)
        self.clickers.append(self.clicked64)
        self.clickers.append(self.clicked65)
        self.clickers.append(self.clicked66)
        self.clickers.append(self.clicked67)
        self.clickers.append(self.clicked68)
        self.clickers.append(self.clicked70)
        self.clickers.append(self.clicked71)
        self.clickers.append(self.clicked72)
        self.clickers.append(self.clicked73)
        self.clickers.append(self.clicked74)
        self.clickers.append(self.clicked75)
        self.clickers.append(self.clicked76)
        self.clickers.append(self.clicked77)
        self.clickers.append(self.clicked78)
        self.clickers.append(self.clicked80)
        self.clickers.append(self.clicked81)
        self.clickers.append(self.clicked82)
        self.clickers.append(self.clicked83)
        self.clickers.append(self.clicked84)
        self.clickers.append(self.clicked85)
        self.clickers.append(self.clicked86)
        self.clickers.append(self.clicked87)
        self.clickers.append(self.clicked88)

        # self.root.mainloop()

    def clicker00 (self,event):
        myLabel = Label(self.root, text=self.clicked00.get()).grid(row=12,column=2)
        val = 0
        if self.clicked00.get() != "":
            val = int(self.clicked00.get())
        if self.check_sudoko_property(0,0,val) == False:
            self.clicked00.set("")
    def clicker01 (self,event):
        myLabel = Label(self.root, text=self.clicked01.get()).grid(row=12,column=2)
        val = 0
        if self.clicked01.get() != "":
            val = int(self.clicked01.get())
        if self.check_sudoko_property(0,1,val) == False:
            self.clicked01.set("")
    def clicker02 (self,event):
        myLabel = Label(self.root, text=self.clicked02.get()).grid(row=12,column=2)
        val = 0
        if self.clicked02.get() != "":
            val = int(self.clicked02.get())
        if self.check_sudoko_property(0,2,val) == False:
            self.clicked02.set("")
    def clicker03 (self,event):
        myLabel = Label(self.root, text=self.clicked03.get()).grid(row=12,column=2)
        val = 0
        if self.clicked03.get() != "":
            val = int(self.clicked03.get())
        if self.check_sudoko_property(0,3,val) == False:
            self.clicked03.set("")
    def clicker04 (self,event):
        myLabel = Label(self.root, text=self.clicked04.get()).grid(row=12,column=2)
        val = 0
        if self.clicked04.get() != "":
            val = int(self.clicked04.get())
        if self.check_sudoko_property(0,4,val) == False:
            self.clicked04.set("")
    def clicker05 (self,event):
        myLabel = Label(self.root, text=self.clicked05.get()).grid(row=12,column=2)
        val = 0
        if self.clicked05.get() != "":
            val = int(self.clicked05.get())
        if self.check_sudoko_property(0,5,val) == False:
            self.clicked05.set("")
    def clicker06 (self,event):
        myLabel = Label(self.root, text=self.clicked06.get()).grid(row=12,column=2)
        val = 0
        if self.clicked06.get() != "":
            val = int(self.clicked06.get())
        if self.check_sudoko_property(0,6,val) == False:
            self.clicked06.set("")
    def clicker07 (self,event):
        myLabel = Label(self.root, text=self.clicked07.get()).grid(row=12,column=2)
        val = 0
        if self.clicked07.get() != "":
            val = int(self.clicked07.get())
        if self.check_sudoko_property(0,7,val) == False:
            self.clicked07.set("")
    def clicker08 (self,event):
        myLabel = Label(self.root, text=self.clicked08.get()).grid(row=12,column=2)
        val = 0
        if self.clicked08.get() != "":
            val = int(self.clicked08.get())
        if self.check_sudoko_property(0,8,val) == False:
            self.clicked08.set("")
    def clicker10 (self,event):
        myLabel = Label(self.root, text=self.clicked10.get()).grid(row=12,column=2)
        val = 0
        if self.clicked10.get() != "":
            val = int(self.clicked10.get())
        if self.check_sudoko_property(1,0,val) == False:
            self.clicked10.set("")
    def clicker11 (self,event):
        myLabel = Label(self.root, text=self.clicked11.get()).grid(row=12,column=2)
        val = 0
        if self.clicked11.get() != "":
            val = int(self.clicked11.get())
        if self.check_sudoko_property(1,1,val) == False:
            self.clicked11.set("")
    def clicker12 (self,event):
        myLabel = Label(self.root, text=self.clicked12.get()).grid(row=12,column=2)
        val = 0
        if self.clicked12.get() != "":
            val = int(self.clicked12.get())
        if self.check_sudoko_property(1,2,val) == False:
            self.clicked12.set("")
    def clicker13 (self,event):
        myLabel = Label(self.root, text=self.clicked13.get()).grid(row=12,column=2)
        val = 0
        if self.clicked13.get() != "":
            val = int(self.clicked13.get())
        if self.check_sudoko_property(1,3,val) == False:
            self.clicked13.set("")
    def clicker14 (self,event):
        myLabel = Label(self.root, text=self.clicked14.get()).grid(row=12,column=2)
        val = 0
        if self.clicked14.get() != "":
            val = int(self.clicked14.get())
        if self.check_sudoko_property(1,4,val) == False:
            self.clicked14.set("")
    def clicker15 (self,event):
        myLabel = Label(self.root, text=self.clicked15.get()).grid(row=12,column=2)
        val = 0
        if self.clicked15.get() != "":
            val = int(self.clicked15.get())
        if self.check_sudoko_property(1,5,val) == False:
            self.clicked15.set("")
    def clicker16 (self,event):
        myLabel = Label(self.root, text=self.clicked16.get()).grid(row=12,column=2)
        val = 0
        if self.clicked16.get() != "":
            val = int(self.clicked16.get())
        if self.check_sudoko_property(1,6,val) == False:
            self.clicked16.set("")
    def clicker17 (self,event):
        myLabel = Label(self.root, text=self.clicked17.get()).grid(row=12,column=2)
        val = 0
        if self.clicked17.get() != "":
            val = int(self.clicked17.get())
        if self.check_sudoko_property(1,7,val) == False:
            self.clicked17.set("")
    def clicker18 (self,event):
        myLabel = Label(self.root, text=self.clicked18.get()).grid(row=12,column=2)
        val = 0
        if self.clicked18.get() != "":
            val = int(self.clicked18.get())
        if self.check_sudoko_property(1,8,val) == False:
            self.clicked18.set("")
    def clicker20 (self,event):
        myLabel = Label(self.root, text=self.clicked20.get()).grid(row=12,column=2)
        val = 0
        if self.clicked20.get() != "":
            val = int(self.clicked20.get())
        if self.check_sudoko_property(2,0,val) == False:
            self.clicked20.set("")
    def clicker21 (self,event):
        myLabel = Label(self.root, text=self.clicked21.get()).grid(row=12,column=2)
        val = 0
        if self.clicked21.get() != "":
            val = int(self.clicked21.get())
        if self.check_sudoko_property(2,1,val) == False:
            self.clicked21.set("")
    def clicker22 (self,event):
        myLabel = Label(self.root, text=self.clicked22.get()).grid(row=12,column=2)
        val = 0
        if self.clicked22.get() != "":
            val = int(self.clicked22.get())
        if self.check_sudoko_property(2,2,val) == False:
            self.clicked22.set("")
    def clicker23 (self,event):
        myLabel = Label(self.root, text=self.clicked23.get()).grid(row=12,column=2)
        val = 0
        if self.clicked23.get() != "":
            val = int(self.clicked23.get())
        if self.check_sudoko_property(2,3,val) == False:
            self.clicked23.set("")
    def clicker24 (self,event):
        myLabel = Label(self.root, text=self.clicked24.get()).grid(row=12,column=2)
        val = 0
        if self.clicked24.get() != "":
            val = int(self.clicked24.get())
        if self.check_sudoko_property(2,4,val) == False:
            self.clicked24.set("")
    def clicker25 (self,event):
        myLabel = Label(self.root, text=self.clicked25.get()).grid(row=12,column=2)
        val = 0
        if self.clicked25.get() != "":
            val = int(self.clicked25.get())
        if self.check_sudoko_property(2,5,val) == False:
            self.clicked25.set("")
    def clicker26 (self,event):
        myLabel = Label(self.root, text=self.clicked26.get()).grid(row=12,column=2)
        val = 0
        if self.clicked26.get() != "":
            val = int(self.clicked26.get())
        if self.check_sudoko_property(2,6,val) == False:
            self.clicked26.set("")
    def clicker27 (self,event):
        myLabel = Label(self.root, text=self.clicked27.get()).grid(row=12,column=2)
        val = 0
        if self.clicked27.get() != "":
            val = int(self.clicked27.get())
        if self.check_sudoko_property(2,7,val) == False:
            self.clicked27.set("")
    def clicker28 (self,event):
        myLabel = Label(self.root, text=self.clicked28.get()).grid(row=12,column=2)
        val = 0
        if self.clicked28.get() != "":
            val = int(self.clicked28.get())
        if self.check_sudoko_property(2,8,val) == False:
            self.clicked28.set("")
    def clicker30 (self,event):
        myLabel = Label(self.root, text=self.clicked30.get()).grid(row=12,column=2)
        val = 0
        if self.clicked30.get() != "":
            val = int(self.clicked30.get())
        if self.check_sudoko_property(3,0,val) == False:
            self.clicked30.set("")
    def clicker31 (self,event):
        myLabel = Label(self.root, text=self.clicked31.get()).grid(row=12,column=2)
        val = 0
        if self.clicked31.get() != "":
            val = int(self.clicked31.get())
        if self.check_sudoko_property(3,1,val) == False:
            self.clicked31.set("")
    def clicker32 (self,event):
        myLabel = Label(self.root, text=self.clicked32.get()).grid(row=12,column=2)
        val = 0
        if self.clicked32.get() != "":
            val = int(self.clicked32.get())
        if self.check_sudoko_property(3,2,val) == False:
            self.clicked32.set("")
    def clicker33 (self,event):
        myLabel = Label(self.root, text=self.clicked33.get()).grid(row=12,column=2)
        val = 0
        if self.clicked33.get() != "":
            val = int(self.clicked33.get())
        if self.check_sudoko_property(3,3,val) == False:
            self.clicked33.set("")
    def clicker34 (self,event):
        myLabel = Label(self.root, text=self.clicked34.get()).grid(row=12,column=2)
        val = 0
        if self.clicked34.get() != "":
            val = int(self.clicked34.get())
        if self.check_sudoko_property(3,4,val) == False:
            self.clicked34.set("")
    def clicker35 (self,event):
        myLabel = Label(self.root, text=self.clicked35.get()).grid(row=12,column=2)
        val = 0
        if self.clicked35.get() != "":
            val = int(self.clicked35.get())
        if self.check_sudoko_property(3,5,val) == False:
            self.clicked35.set("")
    def clicker36 (self,event):
        myLabel = Label(self.root, text=self.clicked36.get()).grid(row=12,column=2)
        val = 0
        if self.clicked36.get() != "":
            val = int(self.clicked36.get())
        if self.check_sudoko_property(3,6,val) == False:
            self.clicked36.set("")
    def clicker37 (self,event):
        myLabel = Label(self.root, text=self.clicked37.get()).grid(row=12,column=2)
        val = 0
        if self.clicked37.get() != "":
            val = int(self.clicked37.get())
        if self.check_sudoko_property(3,7,val) == False:
            self.clicked37.set("")
    def clicker38 (self,event):
        myLabel = Label(self.root, text=self.clicked38.get()).grid(row=12,column=2)
        val = 0
        if self.clicked38.get() != "":
            val = int(self.clicked38.get())
        if self.check_sudoko_property(3,8,val) == False:
            self.clicked38.set("")
    def clicker40 (self,event):
        myLabel = Label(self.root, text=self.clicked40.get()).grid(row=12,column=2)
        val = 0
        if self.clicked40.get() != "":
            val = int(self.clicked40.get())
        if self.check_sudoko_property(4,0,val) == False:
            self.clicked40.set("")
    def clicker41 (self,event):
        myLabel = Label(self.root, text=self.clicked41.get()).grid(row=12,column=2)
        val = 0
        if self.clicked41.get() != "":
            val = int(self.clicked41.get())
        if self.check_sudoko_property(4,1,val) == False:
            self.clicked41.set("")
    def clicker42 (self,event):
        myLabel = Label(self.root, text=self.clicked42.get()).grid(row=12,column=2)
        val = 0
        if self.clicked42.get() != "":
            val = int(self.clicked42.get())
        if self.check_sudoko_property(4,2,val) == False:
            self.clicked42.set("")
    def clicker43 (self,event):
        myLabel = Label(self.root, text=self.clicked43.get()).grid(row=12,column=2)
        val = 0
        if self.clicked43.get() != "":
            val = int(self.clicked43.get())
        if self.check_sudoko_property(4,3,val) == False:
            self.clicked43.set("")
    def clicker44 (self,event):
        myLabel = Label(self.root, text=self.clicked44.get()).grid(row=12,column=2)
        val = 0
        if self.clicked44.get() != "":
            val = int(self.clicked44.get())
        if self.check_sudoko_property(4,4,val) == False:
            self.clicked44.set("")
    def clicker45 (self,event):
        myLabel = Label(self.root, text=self.clicked45.get()).grid(row=12,column=2)
        val = 0
        if self.clicked45.get() != "":
            val = int(self.clicked45.get())
        if self.check_sudoko_property(4,5,val) == False:
            self.clicked45.set("")
    def clicker46 (self,event):
        myLabel = Label(self.root, text=self.clicked46.get()).grid(row=12,column=2)
        val = 0
        if self.clicked46.get() != "":
            val = int(self.clicked46.get())
        if self.check_sudoko_property(4,6,val) == False:
            self.clicked46.set("")
    def clicker47 (self,event):
        myLabel = Label(self.root, text=self.clicked47.get()).grid(row=12,column=2)
        val = 0
        if self.clicked47.get() != "":
            val = int(self.clicked47.get())
        if self.check_sudoko_property(4,7,val) == False:
            self.clicked47.set("")
    def clicker48 (self,event):
        myLabel = Label(self.root, text=self.clicked48.get()).grid(row=12,column=2)
        val = 0
        if self.clicked48.get() != "":
            val = int(self.clicked48.get())
        if self.check_sudoko_property(4,8,val) == False:
            self.clicked48.set("")
    def clicker50 (self,event):
        myLabel = Label(self.root, text=self.clicked50.get()).grid(row=12,column=2)
        val = 0
        if self.clicked50.get() != "":
            val = int(self.clicked50.get())
        if self.check_sudoko_property(5,0,val) == False:
            self.clicked50.set("")
    def clicker51 (self,event):
        myLabel = Label(self.root, text=self.clicked51.get()).grid(row=12,column=2)
        val = 0
        if self.clicked51.get() != "":
            val = int(self.clicked51.get())
        if self.check_sudoko_property(5,1,val) == False:
            self.clicked51.set("")
    def clicker52 (self,event):
        myLabel = Label(self.root, text=self.clicked52.get()).grid(row=12,column=2)
        val = 0
        if self.clicked52.get() != "":
            val = int(self.clicked52.get())
        if self.check_sudoko_property(5,2,val) == False:
            self.clicked52.set("")
    def clicker53 (self,event):
        myLabel = Label(self.root, text=self.clicked53.get()).grid(row=12,column=2)
        val = 0
        if self.clicked53.get() != "":
            val = int(self.clicked53.get())
        if self.check_sudoko_property(5,3,val) == False:
            self.clicked53.set("")
    def clicker54 (self,event):
        myLabel = Label(self.root, text=self.clicked54.get()).grid(row=12,column=2)
        val = 0
        if self.clicked54.get() != "":
            val = int(self.clicked54.get())
        if self.check_sudoko_property(5,4,val) == False:
            self.clicked54.set("")
    def clicker55 (self,event):
        myLabel = Label(self.root, text=self.clicked55.get()).grid(row=12,column=2)
        val = 0
        if self.clicked55.get() != "":
            val = int(self.clicked55.get())
        if self.check_sudoko_property(5,5,val) == False:
            self.clicked55.set("")
    def clicker56 (self,event):
        myLabel = Label(self.root, text=self.clicked56.get()).grid(row=12,column=2)
        val = 0
        if self.clicked56.get() != "":
            val = int(self.clicked56.get())
        if self.check_sudoko_property(5,6,val) == False:
            self.clicked56.set("")
    def clicker57 (self,event):
        myLabel = Label(self.root, text=self.clicked57.get()).grid(row=12,column=2)
        val = 0
        if self.clicked57.get() != "":
            val = int(self.clicked57.get())
        if self.check_sudoko_property(5,7,val) == False:
            self.clicked57.set("")
    def clicker58 (self,event):
        myLabel = Label(self.root, text=self.clicked58.get()).grid(row=12,column=2)
        val = 0
        if self.clicked58.get() != "":
            val = int(self.clicked58.get())
        if self.check_sudoko_property(5,8,val) == False:
            self.clicked58.set("")
    def clicker60 (self,event):
        myLabel = Label(self.root, text=self.clicked60.get()).grid(row=12,column=2)
        val = 0
        if self.clicked60.get() != "":
            val = int(self.clicked60.get())
        if self.check_sudoko_property(6,0,val) == False:
            self.clicked60.set("")
    def clicker61 (self,event):
        myLabel = Label(self.root, text=self.clicked61.get()).grid(row=12,column=2)
        val = 0
        if self.clicked61.get() != "":
            val = int(self.clicked61.get())
        if self.check_sudoko_property(6,1,val) == False:
            self.clicked61.set("")
    def clicker62 (self,event):
        myLabel = Label(self.root, text=self.clicked62.get()).grid(row=12,column=2)
        val = 0
        if self.clicked62.get() != "":
            val = int(self.clicked62.get())
        if self.check_sudoko_property(6,2,val) == False:
            self.clicked62.set("")
    def clicker63 (self,event):
        myLabel = Label(self.root, text=self.clicked63.get()).grid(row=12,column=2)
        val = 0
        if self.clicked63.get() != "":
            val = int(self.clicked63.get())
        if self.check_sudoko_property(6,3,val) == False:
            self.clicked63.set("")
    def clicker64 (self,event):
        myLabel = Label(self.root, text=self.clicked64.get()).grid(row=12,column=2)
        val = 0
        if self.clicked64.get() != "":
            val = int(self.clicked64.get())
        if self.check_sudoko_property(6,4,val) == False:
            self.clicked64.set("")
    def clicker65 (self,event):
        myLabel = Label(self.root, text=self.clicked65.get()).grid(row=12,column=2)
        val = 0
        if self.clicked65.get() != "":
            val = int(self.clicked65.get())
        if self.check_sudoko_property(6,5,val) == False:
            self.clicked65.set("")
    def clicker66 (self,event):
        myLabel = Label(self.root, text=self.clicked66.get()).grid(row=12,column=2)
        val = 0
        if self.clicked66.get() != "":
            val = int(self.clicked66.get())
        if self.check_sudoko_property(6,6,val) == False:
            self.clicked66.set("")
    def clicker67 (self,event):
        myLabel = Label(self.root, text=self.clicked67.get()).grid(row=12,column=2)
        val = 0
        if self.clicked67.get() != "":
            val = int(self.clicked67.get())
        if self.check_sudoko_property(6,7,val) == False:
            self.clicked67.set("")
    def clicker68 (self,event):
        myLabel = Label(self.root, text=self.clicked68.get()).grid(row=12,column=2)
        val = 0
        if self.clicked68.get() != "":
            val = int(self.clicked68.get())
        if self.check_sudoko_property(6,8,val) == False:
            self.clicked68.set("")
    def clicker70 (self,event):
        myLabel = Label(self.root, text=self.clicked70.get()).grid(row=12,column=2)
        val = 0
        if self.clicked70.get() != "":
            val = int(self.clicked70.get())
        if self.check_sudoko_property(7,0,val) == False:
            self.clicked70.set("")
    def clicker71 (self,event):
        myLabel = Label(self.root, text=self.clicked71.get()).grid(row=12,column=2)
        val = 0
        if self.clicked71.get() != "":
            val = int(self.clicked71.get())
        if self.check_sudoko_property(7,1,val) == False:
            self.clicked71.set("")
    def clicker72 (self,event):
        myLabel = Label(self.root, text=self.clicked72.get()).grid(row=12,column=2)
        val = 0
        if self.clicked72.get() != "":
            val = int(self.clicked72.get())
        if self.check_sudoko_property(7,2,val) == False:
            self.clicked72.set("")
    def clicker73 (self,event):
        myLabel = Label(self.root, text=self.clicked73.get()).grid(row=12,column=2)
        val = 0
        if self.clicked73.get() != "":
            val = int(self.clicked73.get())
        if self.check_sudoko_property(7,3,val) == False:
            self.clicked73.set("")
    def clicker74 (self,event):
        myLabel = Label(self.root, text=self.clicked74.get()).grid(row=12,column=2)
        val = 0
        if self.clicked74.get() != "":
            val = int(self.clicked74.get())
        if self.check_sudoko_property(7,4,val) == False:
            self.clicked74.set("")
    def clicker75 (self,event):
        myLabel = Label(self.root, text=self.clicked75.get()).grid(row=12,column=2)
        val = 0
        if self.clicked75.get() != "":
            val = int(self.clicked75.get())
        if self.check_sudoko_property(7,5,val) == False:
            self.clicked75.set("")
    def clicker76 (self,event):
        myLabel = Label(self.root, text=self.clicked76.get()).grid(row=12,column=2)
        val = 0
        if self.clicked76.get() != "":
            val = int(self.clicked76.get())
        if self.check_sudoko_property(7,6,val) == False:
            self.clicked76.set("")
    def clicker77 (self,event):
        myLabel = Label(self.root, text=self.clicked77.get()).grid(row=12,column=2)
        val = 0
        if self.clicked77.get() != "":
            val = int(self.clicked77.get())
        if self.check_sudoko_property(7,7,val) == False:
            self.clicked77.set("")
    def clicker78 (self,event):
        myLabel = Label(self.root, text=self.clicked78.get()).grid(row=12,column=2)
        val = 0
        if self.clicked78.get() != "":
            val = int(self.clicked78.get())
        if self.check_sudoko_property(7,8,val) == False:
            self.clicked78.set("")
    def clicker80 (self,event):
        myLabel = Label(self.root, text=self.clicked80.get()).grid(row=12,column=2)
        val = 0
        if self.clicked80.get() != "":
            val = int(self.clicked80.get())
        if self.check_sudoko_property(8,0,val) == False:
            self.clicked80.set("")
    def clicker81 (self,event):
        myLabel = Label(self.root, text=self.clicked81.get()).grid(row=12,column=2)
        val = 0
        if self.clicked81.get() != "":
            val = int(self.clicked81.get())
        if self.check_sudoko_property(8,1,val) == False:
            self.clicked81.set("")
    def clicker82 (self,event):
        myLabel = Label(self.root, text=self.clicked82.get()).grid(row=12,column=2)
        val = 0
        if self.clicked82.get() != "":
            val = int(self.clicked82.get())
        if self.check_sudoko_property(8,2,val) == False:
            self.clicked82.set("")
    def clicker83 (self,event):
        myLabel = Label(self.root, text=self.clicked83.get()).grid(row=12,column=2)
        val = 0
        if self.clicked83.get() != "":
            val = int(self.clicked83.get())
        if self.check_sudoko_property(8,3,val) == False:
            self.clicked83.set("")
    def clicker84 (self,event):
        myLabel = Label(self.root, text=self.clicked84.get()).grid(row=12,column=2)
        val = 0
        if self.clicked84.get() != "":
            val = int(self.clicked84.get())
        if self.check_sudoko_property(8,4,val) == False:
            self.clicked84.set("")
    def clicker85 (self,event):
        myLabel = Label(self.root, text=self.clicked85.get()).grid(row=12,column=2)
        val = 0
        if self.clicked85.get() != "":
            val = int(self.clicked85.get())
        if self.check_sudoko_property(8,5,val) == False:
            self.clicked85.set("")
    def clicker86 (self,event):
        myLabel = Label(self.root, text=self.clicked86.get()).grid(row=12,column=2)
        val = 0
        if self.clicked86.get() != "":
            val = int(self.clicked86.get())
        if self.check_sudoko_property(8,6,val) == False:
            self.clicked86.set("")
    def clicker87 (self,event):
        myLabel = Label(self.root, text=self.clicked87.get()).grid(row=12,column=2)
        val = 0
        if self.clicked87.get() != "":
            val = int(self.clicked87.get())
        if self.check_sudoko_property(8,7,val) == False:
            self.clicked87.set("")
    def clicker88 (self,event):
        myLabel = Label(self.root, text=self.clicked88.get()).grid(row=12,column=2)
        val = 0
        if self.clicked88.get() != "":
            val = int(self.clicked88.get())
        if self.check_sudoko_property(8,8,val) == False:
            self.clicked88.set("")


    def check_sudoko_property(self,r,c,val,dosend=True):
        setnum = 0
        for x in range(9):
            if (r,c) in self.set_sets[x]:
                print("found the set",x)
                setnum = x
                break
        preval = self.matrix[r][c]
        if val in self.row_sets[r]:
            self.thread_websocket.do_activate(str(r)+str(c)+str(0))
            # messagebox.showerror("same number in row")
            if preval != 0:
                self.row_sets[r].remove(preval)
                self.col_sets[c].remove(preval)
                self.set_sets[setnum].remove(preval)
            return False
        if val in self.col_sets[c]:
            self.thread_websocket.do_activate(str(r)+str(c)+str(0))
            # messagebox.showerror("same number in column")
            if preval != 0:
                self.row_sets[r].remove(preval)
                self.col_sets[c].remove(preval)
                self.set_sets[setnum].remove(preval)
            return False
        if val in self.set_sets[setnum]:
            self.thread_websocket.do_activate(str(r)+str(c)+str(0))
            messagebox.showerror("same number in box whick is important...")
            if preval != 0:
                self.row_sets[r].remove(preval)
                self.col_sets[c].remove(preval)
                self.set_sets[setnum].remove(preval)
            return False
        preval = self.matrix[r][c]
        if dosend:
            self.thread_websocket.do_activate(str(r)+str(c)+str(val))
        else:
            self.clickers[9*r+c].set(self.options[val])
        if preval != 0:
            self.row_sets[r].remove(preval)
            self.col_sets[c].remove(preval)
            self.set_sets[setnum].remove(preval)
        if val == 0:
            self.matrix[r][c] = 0
            return True
        self.matrix[r][c] = val
        self.row_sets[r].add(val)
        self.col_sets[c].add(val)
        self.set_sets[setnum].add(val)
        return True

    def make_sets(self):
        setnames = []
        for i in range(0,9,3):
            for j in range(0,9,3):
                setnames.append((i,j))
        # print(setnames)
        for cnt in range(9):
            self.set_sets.append(set())
            self.set_names.append(set())
            self.row_sets.append(set())
            self.col_sets.append(set())
            r,c = setnames[cnt]
            for i in range(3):
                for j in range(3):
                    self.set_names[cnt].add((r+i,c+j))
        # for x in self.set_names:
            # print(x)
