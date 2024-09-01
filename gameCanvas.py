import tkinter as tk
from pidgey import Pidgey
from obstacle import Obstacle
import models

class gameCanvas():
    #This will be our game window
    def __init__(self, window):
        self.canvas = tk.Canvas(window, width=500, height=250, background='#c8e0d2')
        self.canvas.pack()
        self.character = Pidgey(self.canvas, 210, 0)
        self.gameOn = True
        self.obj = Obstacle(self.canvas)
        self.window = window
        self.points=0
        self.canvas.create_text(0, 0, text=str(self.points), font=("Arial", 24), fill="#000000", anchor=tk.NW)
        self.mainLoop()

    def mainLoop(self):
        if self.gameOn == True:
            self.character.positionChange()
            self.obj.nextPosition()
            self.canvas.delete("all")
            self.character.draw()
            if self.character.x > self.obj.x2 - 10 and self.character.x < self.obj.x2 + 10:
                self.points += 10
            self.canvas.create_text(0, 0, text=str(self.points), font=("Arial", 24), fill="#000000", anchor=tk.NW)
            if self.obj.x2 < 0:
                self.obj = None
                self.obj = Obstacle(self.canvas)
            else:
                self.obj.draw()
            if self.character.y > 250:
                self.gameOver()
                return
            if self.character.endX > self.obj.x1 and self.character.x < self.obj.x2:
                if self.character.y < self.obj.top or self.character.endY > self.obj.bottom:
                    self.gameOver()
                    return

            self.canvas.after(25, self.mainLoop)  # 1000 milliseconds = 1 second


    def gameOver(self):
        self.gameOn = False
        self.canvas.delete("all")
        self.canvas.create_text(100, 100, text=f'Points: {str(self.points)}', font=("Arial", 36), fill="#000000", anchor=tk.NW)
        #Record score to database
        newScore = models.Scores(
            score=self.points
        )
        models.session.add(newScore)
        models.session.commit()
        

