import tkinter as tk

class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack(side="left",expand=1)
        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)
        self.entrythingy2 = tk.Entry()
        self.entrythingy2.pack(side="left",expand=1)
        self.contents = tk.StringVar()
        self.contents.set("this is a vari33")
        self.entrythingy2["textvariable"] = self.contents
        self.entrythingy2.bind('<Key-Return>', self.print_contents)
        self.entrythingy3 = tk.Entry()
        self.entrythingy3.pack(side="left",expand=1)
        self.contents = tk.StringVar()
        self.contents.set("this is a vari33")
        self.entrythingy3["textvariable"] = self.contents
        self.entrythingy3.bind('<Key-Return>', self.print_contents)
        self.pack()
        self.entrythingy4 = tk.Entry()
        self.entrythingy4.pack(expand=1)
        self.contents = tk.StringVar()
        self.contents.set("this is a vari33")
        self.entrythingy4["textvariable"] = self.contents
        self.entrythingy4.bind('<Key-Return>', self.print_contents)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def print_contents(self, event):
        print("Hi. The current entry content is:", self.contents.get())

    def create_widgets(self):

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
    def say_bye(self):
        print("hi there, everyone!")

root = tk.Tk()
app = Game(master=root)
app.mainloop()
import tkinter as tk

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
'''
root = tk.Tk()
myapp = App(root)
myapp.mainloop()
'''

class App2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
'''
myapp = App2()

#
# here are method calls to the window manager class
#
myapp.master.title("My Do-Nothing Application")
myapp.master.maxsize(1000, 400)

# start the program
myapp.mainloop()

'''
