from random import *
class Balls:
    def __init__(self, canvas, color):
        self.canvas = canvas
        x = randint(10,100)
        y = randint(10,100)
        self.img = canvas.create_oval(x, x, y, y, fill = color)
        self.xx = randint(1,10)
        self.yy = randint(1,20)
    def move(self):
        height = self.canvas.winfo_screenheight()
        width = self.canvas.winfo_screenwidth()
        self.canvas.move(self.img, self.xx, self.yy)
        corrx = self.canvas.coords(self.img)
        if corrx[3] >= height or corrx[1] <= 0:
            self.yy = -self.yy
        if corrx[2] >= width or corrx[0] <= 0:
            self.xx = -self.xx
        
