from tkinter import *
from tkinter.ttk import *
 
root = Tk()
style = Style()
 
e = Entry(justify='center')
e.pack()
Button(text="Hello").pack()
Label(text="Hello").pack()
 
themes = style.theme_names()
i = 0
 
 
def theme_next(event):
    global i
    style.theme_use(themes[i])
    e.delete(0, END)
    e.insert(0, themes[i])
    if i < len(themes)-1:
        i += 1
    else:
        i = 0
 
 
root.bind('<Return>', theme_next)
root.mainloop()