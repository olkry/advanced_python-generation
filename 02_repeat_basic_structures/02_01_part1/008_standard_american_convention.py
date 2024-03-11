# На вход программе подаётся натуральное число.
# Напишите программу, которая вставляет в заданное число запятые в соответствии
# со стандартным американским соглашением о запятых в больших числах.

number = input()

if len(number) > 3:
    line = number[-3:]
    while len(number) > 3:
        number = str(int(number) // 1000)
        line = number[-3:] + ',' + line
    print(line)
else:
    print(number)

    # =======

num = input()
for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]
print(num)

# ======================
seq = list(input())
new_s = ""

while len(seq) >= 3:
    new_s += seq.pop(-1) + seq.pop(-1) + seq.pop(-1) + ","  # отрываем 3 последние цифры и ставим после них запятую

new_s += "".join(seq[::-1])  # обрабатываем цифры, которые могли остаться (их 1 или 2)

new_s = new_s[::-1]  # переворачивааем результат в первоначальный вид
new_s = new_s.lstrip(",")  # убираем лишнюю запятую

print(new_s)