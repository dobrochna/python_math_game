import tkinter as tk


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.image = tk.PhotoImage(file="logo.png")
        self.logo = tk.Label(self.root, image=self.image, padx=10, pady=10).grid(row=0, column=7, columnspan=3, rowspan=3)
        self.label = tk.Label(self.root, text='Simple Puzzle game', padx=100, pady=10, fg="dark blue", font="Helvetica 12 bold").grid(row=0, column=0, columnspan=6)
        self.msg = tk.Label(self.root, text='Choose the board size for the game', padx=10, pady=10, font="Helvetica 10").grid(row=5, column=3, columnspan=5)
        self.display_buttons()

    def display_buttons(self):
        three_button = tk.Button(self.root, text="3x3", activebackground="light blue", bd=4).grid(row=6, column=3)
        four_button = tk.Button(self.root, text="4x4", activebackground="light blue", bd=4).grid(row=6, column=4)
        five_button = tk.Button(self.root, text="5x5", activebackground="light blue", bd=4).grid(row=6, column=5)
        six_button = tk.Button(self.root, text="6x6", activebackground="light blue", bd=4).grid(row=6, column=6)