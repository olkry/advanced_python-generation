# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию.
# Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.

inputer = []

for digit in input().split():
    if digit not in inputer:
        inputer.append(digit)

print(len(inputer))

# ========================
# numbers = input().split()
# counter = 1
#
# for i in range(len(numbers) - 1):
#     if numbers[i] != numbers[i + 1]:
#         counter += 1
#
# print(counter)
