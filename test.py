        
r = 0
c = 0
'''
for r in range(9):
    for c in range(9):
        print("        self.clickers.append(self.clicked"+str(r)+str(c)+")")
'''
for r in range(9):
    for c in range(9):
        print("    def clicker"+str(r)+str(c)+" (self,event):")
        print("        myLabel = Label(self.root, text=self.clicked"+str(r)+str(c)+".get()).grid(row=12,column=2)")
        print("        val = 0")
        print("        if self.clicked"+str(r)+str(c)+".get() != \"\":")
        print("            val = int(self.clicked"+str(r)+str(c)+".get())")
        print("        if self.check_sudoko_property("+str(r)+","+str(c)+",val) == False:")
        print("            self.clicked"+str(r)+str(c)+".set(\"\")")
'''
    def clicker00 (self,event):
        myLabel = Label(self.root, text=self.clicked00.get()).grid(row=10,column=8)
        val = 0
        if self.clicked00.get() != "":
            val = int(self.clicked00.get())
        if self.check_sudoko_property("+str(r)+","+str(c)+",val) == False:
            self.clicked00.set("")
            '''
'''
for r in range(9):
    for c in range(9):
        print("        self.clicked"+str(r)+str(c) +" = StringVar()")
        print("        self.clicked"+str(r)+str(c)+".set(self.options[0])")
        print("        self.drop"+str(r)+str(c)+" = OptionMenu(self.root, self.clicked"+str(r)+str(c)+", *self.options, command=self.clicker"+str(r)+str(c)+")")
        print("        self.drop"+str(r)+str(c)+".grid(row="+str(r)+",column="+str(c)+")")
'''
'''

        self.clicked00 = StringVar()
        self.clicked00.set(self.options[0])
        self.drop00 = OptionMenu(self.root, self.clicked00, *self.options, command=self.clicker00)
        self.drop00.grid(row=0,column=0)
        '''
