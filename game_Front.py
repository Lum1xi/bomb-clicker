

def front():
    import tkinter as tk
    from main import Bomb
    bomb_setup = Bomb()
    root = tk.Tk()
    root.title("Bomb Game")
    root.geometry('600x600')
    root.iconbitmap("asset/bomb.ico")

    label = tk.Label(text="Press [Enter] to start the game",
                     font=("Comic Sans MS", 20))

    fuse_label = tk.Label(text=f"Time: {bomb_setup.timer}",
                          font=("Comic Sans MS", 20))

    score_label = tk.Label(text=f"Score: {str(bomb_setup.score)}",
                           font=("Comic Sans MS", 20))

    bomb_label = tk.Label(image=bomb_setup.img[0])


    label.pack()
    fuse_label.pack()
    score_label.pack()
    bomb_label.pack()


    root.mainloop()
front()