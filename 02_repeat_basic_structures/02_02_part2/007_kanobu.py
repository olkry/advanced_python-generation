# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов".
# Для этого они решили сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.

options = ['камень', 'ножницы', 'бумага']
results = ['Тимур', 'Руслан', 'ничья']
combination = -1
first_player = input()
second_player = input()

if (first_player == options[0] and second_player == options[1]) or (
        first_player == options[1] and second_player == options[2]) or (
        first_player == options[2] and second_player == options[0]):
    combination = 0
elif (first_player == options[1] and second_player == options[0]) or (
        first_player == options[2] and second_player == options[1]) or (
        first_player == options[0] and second_player == options[2]):
    combination = 1

print(results[combination])

# =======================
# options = ["камень", "ножницы", "бумага"]
# results = ["ничья", "Руслан", "Тимур"]
#
# timur_move = input()
# ruslan_move = input()
#
# case = options.index(timur_move) - options.index(ruslan_move)
# res = results[case]
#
# print(res)
# =========================
# x, y = input(), input()
# var = ['камень', 'ножницы', 'бумага']
# ans = ['ничья', 'Руслан', 'Тимур']
# print(ans[var.index(x) - var.index(y)])
# ===========================
# tm, rs = input(), input()
# print('ничья' if tm == rs else 'Тимур' if tm + rs in 'каменьножницыбумагакамень' else 'Руслан')