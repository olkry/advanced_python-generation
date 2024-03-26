# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.
# Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; нижней четверти; левой четверти.
# Sample Input 1:
# 4
# 1 2 3 4
# 5 6 7 8
# 3 4 5 6
# 1 2 3 4
# Sample Output 1:
# Верхняя четверть: 5
# Правая четверть: 14
# Нижняя четверть: 5
# Левая четверть: 8

dimension = int(input())
matrix = [[int(rows) for rows in input().split()] for _ in range(dimension)]
up, down, right, left = 0, 0, 0, 0

for r in range(dimension):
    for c in range(dimension):
        if r < c and r < dimension - 1 - c:
            up += matrix[r][c]
        elif r > c and r < dimension - 1 - c:
            left += matrix[r][c]
        elif r < c and r > dimension - 1 - c:
            right += matrix[r][c]
        elif r > c and r > dimension - 1 - c:
            down += matrix[r][c]

print(f'Верхняя четверть: {up}', f'Правая четверть: {right}',
      f'Нижняя четверть: {down}', f'Левая четверть: {left}', sep='\n')

# ++++++++++++++++++++++++++++
n = int(input())
matrix = []
quadrants = [['Верхняя четверть:', 0],
             ['Правая четверть:', 0],
             ['Нижняя четверть:', 0],
             ['Левая четверть:', 0]]

for _ in range(n):
    row = [int(i) for i in input().split()]
    matrix.append(row)

for i in range(n):
    for j in range(n):
        if i < j and i + j + 1 < n :
            quadrants[0][1] += matrix[i][j]
        elif i < j and i + j + 1 > n:
            quadrants[1][1] += matrix[i][j]
        elif i > j and i + j + 1 > n:
            quadrants[2][1] += matrix[i][j]
        elif i > j and i + j + 1 < n:
            quadrants[3][1] += matrix[i][j]

for i in range(4):
    print(quadrants[i][0], quadrants[i][1])
