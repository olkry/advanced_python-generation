# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
#
# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку,
# и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.
#
# Формат входных данных
# На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести считанную матрицу, за ней пустую строку и ту же матрицу, но поменяв местами строки со столбцами. Элементы матрицы разделять одним пробелом.

row, column = int(input()), int(input())
matrix = [[input() for _ in range(column)] for _ in range(row)]

for rows in matrix:
    print(*rows)

print()

for c in range(column):
    for r in range(row):
        print(matrix[r][c], end=' ')
    print()

# +++++++++++++++++++++++++++
n, m = int(input()), int(input())
matrix = []

for _ in range(n):
    row = [input() for j in range(m)]
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

print()

for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()
