import numpy as np


def print_sudoku_matrix(arr):
    for i in range(len(arr)):
        if i % 9 == 0 and i != 0:
            print('|');
        if i % 27 == 0 and i != 0:
            print('+-------+-------+-------+')
        if i % 3 == 0:
            print("| ", end='')

        print(f'{arr[i]}', end=' ')

    print('|', end='')


def duplictes_on_line(arr, line):
    no = 0
    begin = line * 9
    end = line * 9 + 9
    numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in range(begin, end - 1):
        for j in range(i + 1, end):
            if arr[i] == arr[j] and numbers[arr[i]] == 0:
                no = no + 1
        numbers[arr[i]] = 1

    #print(f'\n {no}')
    #print(numbers);
    return no


def duplictes_on_column(arr, column):
    no = 0

    numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for i in range(8):
        for j in range(i + 1, 9):
            if arr[(9 * i) + column] == arr[(9 * j) + column] and numbers[arr[(9 * i) + column]] == 0:
                no = no + 1
        numbers[arr[(9 * i) + column]] = 1

    #print(f'\n {no}')
    #print(numbers);
    return no


def duplictes_in_square(arr, square):
    no = 0
    numbers = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    k = 0
    ar = []
    while k != 3:
        begin = (k * 9) + (3 * ((int(square / 3) * 9) + square % 3))
        for i in range(begin, begin + 3):
            ar.append(i)
        k += 1

    for i in ar[: -1]:
        for j in ar[ar.index(i) :]:
            if arr[i] == arr[j] and i != j and numbers[arr[i]] == 0:
                no = no + 1
        numbers[arr[i]] = 1

    #print(f'\n {no}')
    #print(numbers);
    return no

def initialize(arr):
    numbers = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for i in range(len(arr)):
        if arr[i] != 0:
            numbers[arr[i]] += 1

    for i in range(len(arr)):
        if arr[i] == 0:
            while True:
                arr[i] = np.random.randint(1, 10)

                if numbers[arr[i]] < 9:
                    break

            numbers[arr[i]] += 1

    return arr

def swaping_values(arr):
    index1 = np.random.randint(0, len(arr))
    index2 = np.random.randint(0, len(arr))
    tmp = 0
    #print(f'index = {index1} - value = {index2}')
    tmp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = tmp

    return arr

def number_of_duplicates(arr):
    no_of_duplicates = 0
    for i in range(9):
        no_of_duplicates += duplictes_on_line(arr, i)
        no_of_duplicates += duplictes_on_column(arr, i)
        no_of_duplicates += duplictes_in_square(arr, i)

    return no_of_duplicates

def markedNonZeroesElements(sudokuBoard):
    mat = np.zeros(len(sudokuBoard))
    for i in range(len(sudokuBoard)):
        if sudokuBoard[i] != 0:
            mat[i] = 1
        else:
            mat[i] = 0

    return(mat)




if __name__ == '__main__':

    arr = np.array([
        1, 0, 0, 0, 0, 6, 3, 0, 8,
        0, 0, 2, 3, 0, 0, 0, 9, 0,
        0, 0, 0, 0, 0, 0, 7, 1, 6,

        7, 0, 8, 9, 4, 0, 0, 0, 2,
        0, 0, 4, 0, 0, 0, 9, 0, 0,
        9, 0, 0, 0, 2, 5, 1, 0, 4,

        6, 2, 9, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 0, 7, 6, 0, 0,
        5, 0, 7, 6, 0, 0, 0, 0, 3,
    ])

    d = markedNonZeroesElements(arr)
    for i in range(len(arr)):
        print("{} - {} ".format(i, d[i]))

    # print_sudoku_matrix(arr)
    # print('')
    # print('')
    #duplictes_on_line(arr, 7)
    #duplictes_on_column(arr, 1)

    # dup = []
    # for i in range(9):
    #     for j in range(9):
    #         dup.append((i * 9) + j)
    #
    # #print_sudoku_matrix(dup)
    #
    # #duplictes_in_square(arr, 6)
    arr1 = initialize(arr)
    # print_sudoku_matrix(arr1)
    #
    # print('')
    # print('')
    # arr1 = swaping_values(arr)
    # print_sudoku_matrix(arr1)
    # while number_of_duplicates(arr1) > 30:
    #     arr1 = swaping_values(arr)
    #     print(number_of_duplicates(arr1))
    #print_sudoku_matrix(arr1)

