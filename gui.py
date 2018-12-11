import tkinter as tk


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.image = tk.PhotoImage(file="logo.png")
        self.logo = tk.Label(self.root, image=self.image, padx=10, pady=10).place(x=10, y=10)
        self.label = tk.Label(self.root, text='Simple Puzzle game', padx=10, pady=10, fg="dark blue",
                              font="Helvetica 12 bold").place(x=80, y=20)
        self.msg = tk.Label(self.root, text='Choose the board size for the game', padx=10, pady=10,
                            font="Helvetica 10")
        self.msg.place(x=130, y=100)
        self.init_buttons()

    def init_buttons(self):
        self.three_button = tk.Button(self.root, text="3x3", activebackground="light blue", bd=4,
                                      command=lambda: self.display_table(3))
        self.three_button.place(x=150, y=150)
        self.four_button = tk.Button(self.root, text="4x4", activebackground="light blue", bd=4,
                                     command=lambda: self.display_table(4))
        self.four_button.place(x=200, y=150)
        self.five_button = tk.Button(self.root, text="5x5", activebackground="light blue", bd=4,
                                     command=lambda: self.display_table(5))
        self.five_button.place(x=250, y=150)
        self.six_button = tk.Button(self.root, text="6x6", activebackground="light blue", bd=4,
                                    command=lambda: self.display_table(6))
        self.six_button.place(x=300, y=150)
        self.quit_button = tk.Button(self.root, text="quit", activebackground="red", bd=4,
                                     command=self.root.destroy).place(x=450, y=450)

    def display_table(self, size):
        self.destroy_buttons()
        self.canvas = tk.Canvas()

        for number in range(0, size+1):
            for value in range(0, size+1):
                self.canvas.create_rectangle(0+value*40, 0+number*40, 40+value*40, 40+number*40)
        self.canvas.place(x=180-size*10, y=180-size*10)

    def destroy_buttons(self):
        self.msg.destroy()
        self.three_button.destroy()
        self.four_button.destroy()
        self.five_button.destroy()
        self.six_button.destroy()
