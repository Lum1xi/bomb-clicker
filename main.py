import tkinter as tk
from game_Front import front


class Bomb:
    def __init__(self):
        self.timer = 100
        self.score = 0
        self.press_return = True
        self.img = [tk.PhotoImage(file="asset/1.gif"),
                    tk.PhotoImage(file="asset/2.gif"),
                    tk.PhotoImage(file="asset/3.gif"),
                    tk.PhotoImage(file="asset/4.gif")]
front()