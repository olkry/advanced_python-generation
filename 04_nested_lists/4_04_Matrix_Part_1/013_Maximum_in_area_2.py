# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.

dimension = int(input())
matrix = [[int(rows) for rows in input().split()] for _ in range(dimension)]

maximum = matrix[0][0]

for r in range(dimension):
    for c in range(dimension):
        if (r >= c and r <= dimension - 1 - c) or (r <= c and r >= dimension - 1 - c):
            if maximum < matrix[r][c]:
                maximum = matrix[r][c]

print(maximum)
# ++++++++++++++++++++++

n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

largest = matrix[0][0]

for i in range(n):
    for j in range(n):
        if (i >= j and i + j + 1 <= n) or (i <= j and i + j + 1 >= n):
            if matrix[i][j] > largest:
                largest = matrix[i][j]

print(largest)