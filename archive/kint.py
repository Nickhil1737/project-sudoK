
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()                 
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
            command=self.quit)      
        self.quitButton.grid()      

app = Application()                 
app.master.title('Sample application')
app.mainloop()
class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["bg"] = "white"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.hi_there.config(fg="red", bg="blue")

        self.bye = tk.Button(self)
        self.bye["text"] = "click to say bye"
        self.bye["bg"] = "white"
        self.bye["command"] = self.say_bye
        self.bye.pack(side="top")
        self.bye.config(fg="red", bg="blue")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    def say_bye(self):
        print("hi there, everyone!")
#root = tk.Tk()
#app = Game(master=root)
#app.mainloop()
#import tkinter as tk

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("this is a variable")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())
#root = tk.Tk()
#myapp = App(root)
#myapp.mainloop()

class App2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
#myapp = App2()

#
# here are method calls to the window manager class
#
#myapp.master.title("My Do-Nothing Application")
#myapp.master.maxsize(1000, 400)

# start the program
#myapp.mainloop()

