#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in range(len(matrix)):
        for col in range(len(matrix[rows])):
            print("{:d}".format(matrix[rows][col]), end="")
            if col < len(matrix[rows]) - 1:
                print(" ", end="")
        print("")
