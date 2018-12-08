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

        # transpose arrays for calculations
        transposed_num_table = list(map(list, zip(*self.num_table)))
        transposed_take_table = list(map(list, zip(*self.take_table)))

        # check if sum in any column or array isnt equal to 0
        for sublist in self.take_table:
            if not any(sublist):
                # if it is write one random 0 as 1
                sublist[random.randint(0, size-1)] = 1

        for sublist in transposed_take_table:
            if not any(sublist):
                # if it is write one random 0 as 1
                sublist[random.randint(0, size - 1)] = 1
        self.take_table = list(map(list, zip(*transposed_take_table)))

        # calculate sums for rows
        for subelementlist, sebdecisionlist in zip(self.num_table, self.take_table):
            counter_rows = 0
            summary_rows = 0
            for element, decision in zip(subelementlist, sebdecisionlist):
                if decision == 1:
                    summary_rows += element
                counter_rows += 1
                if counter_rows == size:
                    self.sums_rows.append(summary_rows)

        # calculate sums for columns
        for subelementlist, sebdecisionlist in zip(transposed_num_table, transposed_take_table):
            counter_columns = 0
            summary_columns = 0
            for element, decision in zip(subelementlist, sebdecisionlist):
                if decision == 1:
                    summary_columns += element
                counter_columns += 1
                if counter_columns == size:
                    self.sums_columns.append(summary_columns)

    def __print__(self, size):
        # print empty table
        print('----'*size)
        print('|' + '   |'*size)


