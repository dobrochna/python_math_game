import tkinter as tk
import table


class Window:
    def __init__(self):
        # init window for the game
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
        self.table_buttons = []

    def init_buttons(self):
        # init buttons in window to choose the size of the table
        self.three_button = tk.Button(self.root, text="3x3", activebackground="#0099e6", bd=4,
                                      command=lambda: self.init_grid(3))
        self.three_button.place(x=150, y=150)
        self.four_button = tk.Button(self.root, text="4x4", activebackground="#0099e6", bd=4,
                                     command=lambda: self.init_grid(4))
        self.four_button.place(x=200, y=150)
        self.five_button = tk.Button(self.root, text="5x5", activebackground="#0099e6", bd=4,
                                     command=lambda: self.init_grid(5))
        self.five_button.place(x=250, y=150)
        self.six_button = tk.Button(self.root, text="6x6", activebackground="#0099e6", bd=4,
                                    command=lambda: self.init_grid(6))
        self.six_button.place(x=300, y=150)
        self.quit_button = tk.Button(self.root, text="quit", activebackground="#ff8080", bd=4,
                                     command=self.root.destroy).place(x=450, y=450)

    def init_grid(self, size):
        # first destroy buttons
        self.destroy_buttons()

        # then create grid of buttons for the game
        game_table = table.Table(size)

        table_buttons_sublist = []
        for row in range(0, size):
            for column in range(0, size):
                table_buttons_sublist.append(tk.Button(self.root, text=str(game_table.num_table[row][column]),
                                                       height=2, width=4).
                                                       place(x=250+(-(size/2)+column)*40, y=250+(-(size/2)+row)*40))
            self.table_buttons.append(table_buttons_sublist)
            table_buttons_sublist.clear()

        for row in range(0, size):
            print(row)
            for column in range(0, size):
                print(column)
                self.table_buttons[row][column].configure(command=lambda: self.button_clicked(row, column))

        # then print sums values
        self.sums_rows = [tk.Label(self.root, text=str(game_table.sums_rows[row]), height=2, width=4).
                          place(x=250+(-(size/2)+size)*40, y=250+(-(size/2)+row)*40) for row in range(0, size)]
        self.sums_columns = [tk.Label(self.root, text=str(game_table.sums_columns[column]),  height=2, width=4).
                             place(x=250+(-(size/2)+column)*40, y=250+(-(size/2)+size)*40) for column in range(0, size)]

    def button_clicked(self, row, column):
        self.table_buttons[row][column].configure(bg="red")

    def destroy_buttons(self):
        self.msg.destroy()
        self.three_button.destroy()
        self.four_button.destroy()
        self.five_button.destroy()
        self.six_button.destroy()
