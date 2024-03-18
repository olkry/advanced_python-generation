# На вход программе подается число n. Напишите программу, которая создает и выводит построчно вложенный список,
# состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
#
# Формат входных данных
# На вход программе подается натуральное число n.
#
# Формат выходных данных
# Программа должна вывести построчно указанный вложенный список.


number = int(input())
final_list = []
for i in range(1, number + 1):
    final_list.append(list(range(1, i + 1)))

print(*final_list, sep='\n')