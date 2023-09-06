from tkinter import *
root = Tk()
class Dendy:
    def __init__(self, master):
        self.lab = Label(master, width=20, height=2)
        self.ent = Entry(master, width=15, justify='center')
        self.redd = Button(master, bg='#ff0000', width=3)
        self.orange = Button(master, bg='#ff7d00', width=3)
        self.yellou = Button(master, bg='#ffff00', width=3)
        self.green = Button(master, bg='#00ff00', width=3)
        self.wblue = Button(master, bg='#007dff', width=3)
        self.blue = Button(master, bg='#0000ff', width=3)
        self.pink = Button(master, bg='#7d00ff', width=3)
        self.redd['command'] = getattr(self, 'red')
        self.orange['command'] = getattr(self, 'orang')
        self.yellou['command'] = getattr(self, 'yello')
        self.green['command'] = getattr(self, 'gren')
        self.wblue['command'] = getattr(self, 'wblu')
        self.blue['command'] = getattr(self, 'blu')
        self.pink['command'] = getattr(self, 'pin')
        self.lab.pack()
        self.ent.pack()
        self.redd.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.orange.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.yellou.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.green.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.wblue.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.blue.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)
        self.pink.pack(side=LEFT, padx=1, pady=5, expand=1, fill=X)

        
    def red(self):
        self.ent.delete(0, END)
        self.lab['text'] = "красный"
        self.ent.insert(0, string='#ff0000')
    def orang(self):
        self.ent.delete(0, END)
        self.lab['text'] = "оранжевый"
        self.ent.insert(0, string='#ff7d00')
    def yello(self):
        self.ent.delete(0, END)
        self.lab['text'] = "жёлтый"
        self.ent.insert(0, string='#ffff00')
    def gren(self):
        self.ent.delete(0, END)
        self.lab['text'] = "зелёный"
        self.ent.insert(0, string='#00ff00')
    def wblu(self):
        self.ent.delete(0, END)
        self.lab['text'] = "голубой"
        self.ent.insert(0, string='#007dff')
    def blu(self):
        self.ent.delete(0, END)
        self.lab['text'] = "синий"
        self.ent.insert(0, string='#0000ff')
    def pin(self):
        self.ent.delete(0, END)
        self.lab['text'] = "фиолетовый"
        self.ent.insert(0, string='#7d00ff')

Rainbol = Dendy(root)
root.mainloop()