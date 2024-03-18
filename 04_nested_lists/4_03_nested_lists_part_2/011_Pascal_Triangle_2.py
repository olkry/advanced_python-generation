# На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля.

def pascal_1(number):
    pascal_triangle = []
    for i in range(number + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]
        pascal_triangle.append(row)
    return pascal_triangle


number = int(input())

for row in range(number):
    print(*pascal_1(row)[row])


# == == == == == == == == == == == == == == == == =
# -------------------ФУНКЦИЯ-------------------
def pascal(n):
    triangle = [[1]]

    for i in range(n - 1):
        row = [1]
        for j in range(1, len(triangle[i])):
            row += [sum(triangle[i][j - 1: j + 1])]
        row += [1]
        triangle.append(row.copy())

    return triangle


# --------------------ВЫЗОВ--------------------
[print(*row) for row in pascal(int(input()))]
