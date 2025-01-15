import tkinter as tk

class Bomb:
    def __init__(self, root):
        self.timer = 100
        self.score = 0
        self.press_return = True

        self.img = [tk.PhotoImage(master=root, file="asset/1.gif"),
                    tk.PhotoImage(master=root, file="asset/2.gif"),
                    tk.PhotoImage(master=root, file="asset/3.gif"),
                    tk.PhotoImage(master=root, file="asset/4.gif")]