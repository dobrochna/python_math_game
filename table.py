import random


class Table:  # create and fill table for the game

    def __init__(self, size):
        self.table = []
        self.take_table = []
        self.sums_rows = []
        self.sums_columns = []

        for place in range(size**2):
            self.table.append(random.randint(1, 9))
            self.take_table.append(random.randint(0, 1))

        counter_rows = 0
        summary_rows = 0
        for element, decision in zip(self.table, self.take_table):
            if decision == 1:
                summary_rows += element
            counter_rows += 1
            if counter_rows == size:
                self.sums_rows.append(summary_rows)
                summary_rows = 0
                counter_rows = 0


