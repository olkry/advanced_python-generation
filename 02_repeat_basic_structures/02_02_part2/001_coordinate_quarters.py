# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, лежащих в каждой координатной четверти.
# В первой строке записано количество точек. Каждая следующая строка состоит из двух целых чисел —
# координат точки (сначала абсцисса – x, затем ордината – y), разделенных символом пробела.


first, second, third, forth = 0, 0, 0, 0

for _ in range(int(input())):
    coordinate = [int(num) for num in input().split()]
    x_cord = 0
    y_cord = 0
    if 0 in coordinate:
        continue
    else:
        if coordinate[0] > 0:
            x_cord += 1
        if coordinate[1] > 0:
            y_cord += 1
    if x_cord:
        if y_cord:
            first += 1
        else:
            forth += 1
    else:
        if y_cord:
            second += 1
        else:
            third += 1

print(f'Первая четверть: {first}', f'Вторая четверть: {second}',
      f'Третья четверть: {third}', f'Четвертая четверть: {forth}', sep='\n')


# ===========================
# n = int(input())
# count = [0, 0, 0, 0]
# names = ['Первая четверть:', 'Вторая четверть:',
#          'Третья четверть:', 'Четвертая четверть:']
#
# for _ in range(n):
#     x, y = [int(num) for num in input().split()]
#     if x > 0 and y > 0:
#         count[0] += 1
#     elif x < 0 and y > 0:
#         count[1] += 1
#     elif x < 0 and y < 0:
#         count[2] += 1
#     elif x > 0 and y < 0:
#         count[3] += 1
#
# for i in range(4):
#     print(names[i], count[i])

# ==============================
# # put your python code here
# a_1, a_2, a_3, a_4 = 0, 0, 0, 0
# for _ in range(int(input())):
#     x, y = input().split()
#     if int(x) > 0 and int(y) >0:
#         a_1 +=1
#     elif int(x) < 0 and int(y) >0:
#         a_2 += 1
#     elif int(x) < 0 and int(y) < 0 :
#         a_3 += 1
#     elif int(x)> 0 and int(y) < 0 :
#         a_4 +=1
#
# print(f'Первая четверть: {a_1}', f'Вторая четверть: {a_2}', f'Третья четверть: {a_3}', f'Четвертая четверть: {a_4}', sep='\n')
