# На вход программе подаются два целых числа a и b. Напишите программу, которая выводит:
# сумму чисел
# разность чисел
# произведение чисел
# частное чисел
# целую часть от деления
# остаток от деления числа
# корень квадратный из суммы их 10-х степеней:

num_a, num_b = int(input()), int(input())

print(num_a + num_b, num_a - num_b, num_a * num_b, num_a / num_b, sep='\n')
print(num_a // num_b, num_a % num_b, ((num_a ** 10) + (num_b ** 10)) ** 0.5, sep='\n')
