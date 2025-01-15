import tkinter as tk
from main import Bomb

def front():
    root = tk.Tk()  
    root.title("Bomb Game")
    root.geometry('600x600')
    root.iconbitmap("asset/bomb.ico")

    bomb_setup = Bomb(root)  

    label = tk.Label(root, text="Press [Enter] to start the game",
                     font=("Comic Sans MS", 20))

    fuse_label = tk.Label(root, text=f"Time: {bomb_setup.timer}",
                          font=("Comic Sans MS", 20))

    score_label = tk.Label(root, text=f"Score: {str(bomb_setup.score)}",
                           font=("Comic Sans MS", 20))

    bomb_label = tk.Label(root, image=bomb_setup.img[0])

    label.pack()
    fuse_label.pack()
    score_label.pack()
    bomb_label.pack()

    root.mainloop()



front()