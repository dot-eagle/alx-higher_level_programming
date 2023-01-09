#!/usr/bin/python3

print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()



"""
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for row in range(len(matrix)):
            for item in range(len(matrix[row])):
                if item != len(matrix[row]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[row][item]), end=endspace)
            print()

"""
