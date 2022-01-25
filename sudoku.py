import random
import numpy as np
import math
from random import choice
import statistics



class Sudoku:
    defaultSudokuTable = """
                        024007006
                        600000000
                        003680415
                        431005000
                        500000032
                        790000060
                        209710800
                        040093000
                        310004750
                    """
    sudokuArray = np.array([[int(i) for i in line] for line in defaultSudokuTable.split()])

    def printSudokuBoard(self, arr):
        print("\n+-------+-------+-------+")
        for i in range(len(arr)):
            line = ""

            if i == 3 or i == 6:
                print('+-------+-------+-------+')
            for j in range(len(arr[i])):
                if j == 3 or j == 6 or (j % 9 == 0 and j == 0):
                    line += "| "
                line += str(arr[i, j]) + " "

                if j == 8:
                    line += "|"

            print(line)
        print("+-------+-------+-------+")



        #     if i % 27 == 0 and i != 0:
        #         line = '+-------+-------+-------+'
        #     if i % 3 == 0:
        #         print("| ", end='')
        #
        #     print(f'{arr[i]}', end=' ')
        #
        # print('|', end='')
        
    def markedNonZeroesElements(self, sudokuBoard):
        for i in range(9):
            for j in range(9):
                if sudokuBoard[i, j] != 0:
                    sudokuBoard[i, j] = 1
        return(sudokuBoard)

    def calculateNoOfDuplicatesRC(self, line, column, sudokuBoard):
        return (9 - len(np.unique(sudokuBoard[: , column])) + len(np.unique(sudokuBoard[line, :])))

    def calculateNumberOfDuplicates(self, sudokuBoard):
        noOfDuplicates = 0
        for i in range(9):
            noOfDuplicates += self.calculateNoOfDuplicatesRC(i, i, sudokuBoard)
        return noOfDuplicates


    def print(self):
        print(self.defaultSudokuTable)



s =  Sudoku()
#s.print()

sudoku = np.array([[int(i) for i in line] for line in s.defaultSudokuTable.split()])

s.printSudokuBoard(sudoku)
print(s.markedNonZeroesElements(sudokuBoard=sudoku))