import table


if __name__ == "__main__":
    size = 0

    print("Hello in the game!\nHow big table do you want?")

    while True:
        try:
            size = int(input("Pass\n'3' for table 3x3\n'4' for table 4x4\n'5' for table 5x5\n'6' for table 6x6\n"))
        except ValueError:
            print('size must be an integer')
        else:
            if size not in range(3, 7):
                print('Sorry max size is 6x6 and min size is 3x3, try one more time!')
            else:
                print('Great! Lets play!')
                break

    game_table = table.Table(size)
    print(game_table.num_list)
    print(game_table.num_table)
    print(game_table.take_table)