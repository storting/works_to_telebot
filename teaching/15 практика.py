from tkinter import *
import random 
import time
root = Tk()


root.geometry('700x700')
root.config(cursor='none')
class pop:
    
    point = 0
    def __init__(self, master):
        self.but = Button(text='O')
        self.but2 = Button(text='Apple')
        self.lab = Label(text=self.point, bg='green')
        master.bind('<Motion>', self.inn)
        self.but2.bind('<Enter>', self.aple)
        self.but2.place(x=1, y=1)
        self.lab.place(x=1, y=100)
    def inn(self, event):


        self.x = event.x
        self.y = event.y
        
        root.title("Движение мышью {}x{}".format(self.x, self.y))
        self.but.place(x=self.x, y=self.y)
        if self.x == 1 and self.y == 0:
            self.x = self.x
            self.y = self.y
        if self.x <=5 or self.y <= 5:
            self.but.destroy
    def aple(self, event):
        self.x1 = random.randint(1, 400)
        self.y2 = self.x + 100
        self.but2.place(x=self.x1, y=self.y2)
        self.point += 1
        self.lab['text'] = self.point
        
        
        


f = pop(root)
root.mainloop()