# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице.
# Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, и т.д.
#
# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.
#
# Формат входных данных
# На вход программе подаются два числа n и m — количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.


row, column = int(input()), int(input())
matrix = [[input() for _ in range(column)] for _ in range(row)]

for r in range(row):
    for c in range(column):
        print(matrix[r][c], end=' ')
    print()

# +++++++++++++++++++++++++
n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

# ++++++++++++++++++++++++

n, m = int(input()), int(input())
matrix = [[input() for _ in range(m)] for _ in range(n)]

for row in matrix:
    print(*row)

# ++++++++++++++++++++++++++++
n = int(input())
m = int(input())

[print(*[input() for i in range(m)]) for i in range(n)]
