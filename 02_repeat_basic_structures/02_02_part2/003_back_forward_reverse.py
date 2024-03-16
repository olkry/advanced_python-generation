# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу, которая меняет местами соседние элементы списка. Если в списке нечетное количество элементов, то последний остается на своем месте.

number_list = [int(num) for num in input().split()]

for i in range(1, len(number_list), 2):
    number_list[i], number_list[i-1] = number_list[i-1], number_list[i]
print(*number_list)
