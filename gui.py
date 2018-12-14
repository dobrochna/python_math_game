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

    def init_buttons(self):
        # init buttons in window to choose the size of the table
        self.three_button = tk.Button(self.root, text="3x3", activebackground="#0099e6", bd=4,
                                      command=lambda: self.init_table_size(3))
        self.three_button.place(x=150, y=150)
        self.four_button = tk.Button(self.root, text="4x4", activebackground="#0099e6", bd=4,
                                     command=lambda: self.init_table_size(4))
        self.four_button.place(x=200, y=150)
        self.five_button = tk.Button(self.root, text="5x5", activebackground="#0099e6", bd=4,
                                     command=lambda: self.init_table_size(5))
        self.five_button.place(x=250, y=150)
        self.six_button = tk.Button(self.root, text="6x6", activebackground="#0099e6", bd=4,
                                    command=lambda: self.init_table_size(6))
        self.six_button.place(x=300, y=150)
        self.quit_button = tk.Button(self.root, text="quit", activebackground="#ff8080", bd=4,
                                     command=self.root.destroy).place(x=450, y=450)

    def init_table_size(self, size):
        self.size = size
        self.destroy_buttons()
        self.lets_start = tk.Label(self.root, text="You selected a board: %ix%i. Great, let's play!" % (size, size),
                                   padx=10, pady=10, font="Helvetica 10").place(x=100, y=100)
        self.table_grid = Grid(self.root, self.size)

    def destroy_buttons(self):
        self.msg.destroy()
        self.three_button.destroy()
        self.four_button.destroy()
        self.five_button.destroy()
        self.six_button.destroy()


class Grid():
    def __init__(self, master, size):
        self.size = size
        self.canvas = tk.Canvas(master, width=260, height=260)
        self.canvas.place(x=120, y=150)
        self.grid_step = 35
        self.start_x = 120-(self.size/2)*self.grid_step
        self.start_y = 120-(self.size/2)*self.grid_step

        # init game table
        game_table = table.Table(self.size)

        # print table with numbers
        for row in range(0, self.size):
            for column in range(0, self.size):
                self.canvas.create_rectangle(self.start_x+column*self.grid_step, self.start_y+row*self.grid_step,
                                             self.start_x+(column+1)*self.grid_step, self.start_y+(row+1)*self.grid_step,
                                             fill="#b3d1ff")
                self.canvas.create_text(self.start_x+18+column*self.grid_step, self.start_y+18+row*self.grid_step,
                                        text=str(game_table.num_table[row][column]), font="Helvetica 10 bold")

        # print rows sums
        for row in range(0, self.size):
            self.canvas.create_text(self.start_x+18+self.size*self.grid_step, self.start_y+18+row*self.grid_step,
                                    text=str(game_table.sums_rows[row]), font="Helvetica 10 bold")

        # print columns sums
        for column in range(0, self.size):
            self.canvas.create_text(self.start_x+18+column*self.grid_step, self.start_y+18+self.size*self.grid_step,
                                    text=str(game_table.sums_columns[column]), font="Helvetica 10 bold")

    def bind_mouse_click(self, callback=None):
        if callback is None:
            callback = self.change_colour_on_click
        self.canvas.bind("<Button-1>", callback)

    def change_colour_on_click(self, event, color='green'):
        pass



