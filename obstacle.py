from random import randint

class Obstacle():
    def __init__(self, canvas):
        self.canvas = canvas
        self.top = randint(50, 150)
        self.bottom = self.top + 100
        self.x2 = 500
        self.x1 = 450
        self.canvas.create_rectangle(self.x1, 0, self.x2, self.top, outline='#000000', fill='#00FF00')
        self.canvas.create_rectangle(self.x1, self.bottom, self.x2, 250, outline='#000000', fill='#00FF00')
    
    def nextPosition(self):
        self.x1 -= 10
        self.x2 -= 10

    def draw(self):
        self.canvas.create_rectangle(self.x1, 0, self.x2, self.top, outline='#000000', fill='#00FF00')
        self.canvas.create_rectangle(self.x1, self.bottom, self.x2, 250, outline='#000000', fill='#00FF00')