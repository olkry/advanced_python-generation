# На вход программе подается число n. Напишите программу, которая создает и выводит построчно список,
# состоящий из n списков [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести построчно указанный список.

number = int(input())
final_list = []
for _ in range(number):
    element = [el for el in range(1, number + 1)]
    final_list.append(element)
print(*final_list, sep='\n')

# =========================
# n = int(input())
# result = []
#
# for _ in range(n):
#     result.append(list(range(1, n + 1)))
#
# print(*result, sep='\n')

