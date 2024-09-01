from PIL import Image, ImageTk
import tkinter as tk

from misc import anyKeyPressed

class Pidgey():
    def __init__(self, canvas, startx, starty):
        self.path = '.\\assets\\pidgey.jpg'
        self.image = Image.open(self.path)
        self.tkImage = ImageTk.PhotoImage(self.image)
        self.canvas = canvas
        self.x = startx
        self.y = starty
        self.endX = self.x + 42
        self.endY = self.y + 32
        self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.tkImage)
        # Keep a reference to the image
        self.canvas.image = self.tkImage

    def positionChange(self):
        if anyKeyPressed():
            self.y -= 5
        else:
            self.y += 10

    def draw(self):
        self.endX = self.x + 42
        self.endY = self.y + 32
        self.canvas.create_image(self.x, self.y, anchor=tk.NW, image=self.tkImage)

