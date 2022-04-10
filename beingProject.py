from tkinter import *
from random import *
from Balls import *
import time

win = Tk()
win.title('Game')
x = win.winfo_screenwidth()
y = win.winfo_screenheight()
win.geometry(str(x)+'x'+str(y))
canvas = Canvas(win, width = x - 200, height = y, bg = 'green')
canvas.grid(row = 0, column = 1)
sidenav = Frame(win, width = 200, height = y, bg = 'blue')
sidenav.grid(row = 0, column = 0)

color = [ 'black', 'blue', 'red', 'orange', 'pink' ]
balls = []
def add():
    balls.append(Balls(canvas, choice(color)))
win.update()

def run():
    global o
    o = 1
    while o:
        for ball in balls:
            ball.move()
        win.update()
        time.sleep(0.01)

def stop():
    global o
    o = 0

button0 = Button(win, text = 'Add', command = add)
button0.place(x = 70, y = 100)

button1 = Button(win, text = 'Start', command = run)
button1.place(x = 70, y = 150)

button2 = Button(win, text = 'Stop', command = stop)
button2.place(x = 70, y = 200)



win.mainloop()
