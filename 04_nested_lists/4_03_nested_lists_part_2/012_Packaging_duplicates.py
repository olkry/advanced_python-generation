# На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает последовательности одинаковых символов заданной строки в подсписки.
#
# Формат входных данных
# На вход программе подается строка текста, содержащая символы, отделенные символом пробела.
#
# Формат выходных данных
# Программа должна вывести указанный вложенный список.

inp_str = input().split()
final_list = []
char_dubl = []

for char in inp_str:
    if not char_dubl:
        char_dubl.append(char)
    else:
        if char in char_dubl:
            char_dubl.append(char)
        else:
            final_list.append(char_dubl)
            char_dubl = [char]
final_list.append(char_dubl)

print(final_list)

# ======================
s = input().split()
# кидаем первый символ в наш список, также удалив его из входного списка
seq = [[s.pop(0)]]

for c in s:
    if c in seq[-1]:
        seq[-1].append(c)
    else:
        seq.append([c])

print(seq)