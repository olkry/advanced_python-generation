# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического элементов данной строки.
#
# Формат входных данных
# На вход программе подаётся натуральное число n — количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно через пробел.
#
# Формат выходных данных
# Программа должна вывести n чисел — для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной строки.

for _ in range(int(input())):
    row = [int(num) for num in input().split()]
    counter = 0
    for num in row:
        if num > (sum(row)/len(row)):
            counter += 1
    print(counter)
# +++++++++++++++++++++
n = int(input())
matrix = []

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    counter = 0
    average = sum(matrix[i]) / n
    for j in range(n):
        if matrix[i][j] > average:
            counter += 1
    print(counter)