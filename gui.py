import tkinter as tk
from tkinter import ttk

from PIL import Image

from gameCanvas import gameCanvas

import models

def gameWindow():
    window = tk.Toplevel()
    window.geometry('500x300')
    gameScreen = gameCanvas(window)

    window.mainloop()

def topScoresWindow():
    topScores = models.session.query(models.Scores).order_by(models.desc(models.Scores.score)).limit(10).all()
    scoreList = []
    for score in topScores:
        scoreList.append(score.score)
    scoreList.sort(reverse=True)

    window = tk.Toplevel()
    window.geometry('250x250')
    label = tk.Label(window, text="Top Scores")
    label.pack()
    listbox = tk.Listbox(window)
    listbox.pack()
    for score in scoreList:
        listbox.insert(tk.END, score)
    
    window.mainloop()

def startWindow():
    window = tk.Tk()
    window.title('Fly Pidgey, Fly!')
    window.geometry('250x250')
    
    label = tk.Label(window, text="Welcome to Pidgey Fly!")
    label.pack(pady=4)
    startBtn = tk.Button(window, text="Start Game", command=gameWindow)
    startBtn.pack(pady=4)
    scoresBtn = tk.Button(window, text='Top Scores', command=topScoresWindow)
    scoresBtn.pack(pady=4)
    inst = tk.Label(window, text='Hold a, space, or enter to fly, let go to fall!')
    inst.pack(pady=2)

    window.mainloop()