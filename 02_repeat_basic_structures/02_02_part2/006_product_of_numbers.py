# Напишите программу для определения, является ли число произведением двух чисел из данного набора.
# Программа должна выводить результат в виде ответа «ДА» или «НЕТ».


inp_numbers = [int(input()) for _ in range(int(input()))]
work = int(input())
examination = False

for i in range(len(inp_numbers)):
    for j in range(i + 1, len(inp_numbers)):
        if inp_numbers[i] * inp_numbers[j] == work:
            examination = True
            break

print('ДА' if examination else 'НЕТ')



