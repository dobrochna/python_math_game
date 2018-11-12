import random


class Table:  # create and fill table for the game

    def __init__(self, size):
        self.num_list = []
        self.take_list = []
        self.sums_rows = []
        self.sums_columns = []

        # fill list with random numbers and set if its taken to the sum
        for place in range(size**2):
            self.num_list.append(random.randint(1, 9))
            self.take_list.append(random.randint(0, 1))

        # create arrays (size x size) from lists
        self.num_table = [self.num_list[i: i+size] for i in range(0, len(self.num_list), size)]
        self.take_table = [self.take_list[i: i + size] for i in range(0, len(self.take_list), size)]

        # check if sum in any column or array isnt equal to 0
        for sublist in self.take_table:
            if not any(sublist):
                # if it is write one random 0 as 1
                sublist[random.randint(0, size-1)] = 1

        counter_rows = 0
        summary_rows = 0
        for element, decision in zip(self.num_list, self.take_table):
            if decision == 1:
                summary_rows += element
            counter_rows += 1
            if counter_rows == size:
                self.sums_rows.append(summary_rows)
                summary_rows = 0
                counter_rows = 0


