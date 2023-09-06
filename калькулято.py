from tkinter import *
 
root = Tk()
root.title("калькулятор")
class Block:
    def __init__(self, master):
        self.ent1 = Entry(master, width=39)
        self.but_plus = Button(master, text="+", width=5)
        self.but_minus = Button(master, text="-", width=5)
        self.but_umnoj = Button(master, text="*", width=5)
        self.but_delen = Button(master, text="/", width=5)
        self.del_all = Button(master, text='C', width=5)
        self.num_1 = Button(master, text="1", width=5)
        self.num_2 = Button(master, text="2", width=5)
        self.num_3 = Button(master, text="3", width=5)
        self.num_4 = Button(master, text="4", width=5)
        self.num_5 = Button(master, text="5", width=5)
        self.num_6 = Button(master, text="6", width=5)
        self.num_7 = Button(master, text="7", width=5)
        self.num_8 = Button(master, text="8", width=5)
        self.num_9 = Button(master, text="9", width=5)
        self.num_0 = Button(master, text="0", width=5)
        self.lab = Label(master, width=32, height=2, bg='black', fg='white')
        self.but_plus['command'] = getattr(self, 'plus')
        self.but_minus['command'] = getattr(self, 'minus')
        self.but_umnoj['command'] = getattr(self, 'umnoj')
        self.but_delen['command'] = getattr(self, 'delen')
        self.del_all['command'] = getattr(self, 'C')
        self.ent1.grid(row=0, column=0, columnspan=5)
        self.ent2.grid(row=1, column=0, columnspan=5)
        self.but_plus.grid(column=0, row=2)
        self.but_minus.grid(column=1, row=2)
        self.but_umnoj.grid(column=2, row=2)
        self.but_delen.grid(column=3, row=2)
        self.del_all.grid(column=4, row=2)
        self.num_1.grid(row=3, column=0)
        self.num_2.grid(row=3, column=1)
        self.num_3.grid(row=3, column=2)
        self.num_4.grid(row=3, column=3)
        self.num_5.grid(row=3, column=4)
        self.num_6.grid(row=4, column=0)
        self.num_7.grid(row=4, column=1) 
        self.num_8.grid(row=4, column=2) 
        self.num_9.grid(row=4, column=3) 
        self.num_0.grid(row=4, column=4)
        self.lab.grid(row=5, column=0, columnspan=5)
    def plus(self):
        en1 = float(self.ent1.get())

        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lab['text'] = a
        self.ent1.insert(0, float(a))
    def minus(self):
        en1 = float(self.ent1.get())
        en2 = float(self.ent2.get())
        a = en1 - en2
        a
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lab['text'] = a
        self.ent1.insert(0, float(a))
    def umnoj(self):
        en1 = float(self.ent1.get())
        en2 = float(self.ent2.get())
        a = en1 * en2
        a
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lab['text'] = a
        self.ent1.insert(0, float(a))
    def delen(self):
        en1 = float(self.ent1.get())
        en2 = float(self.ent2.get())
        a = en1 / en2
        a
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lab['text'] = a
        self.ent1.insert(0, float(a))
    def C(self):
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.lab['text'] = ''
    




PlusBlock = Block(root)



# когда нибудь обязательно доделаю :D

root.mainloop()