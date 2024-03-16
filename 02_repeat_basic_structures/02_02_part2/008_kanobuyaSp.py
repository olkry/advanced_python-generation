# Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру.
# Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок.
# Помогите ребятам вновь бросить честный жребий и определить, кто будет делать следующий модуль в новом курсе.


options = ['камень', 'ножницы', 'бумага', 'ящерица', 'Спок']
results = ['Тимур', 'Руслан', 'ничья']
combination = -1
first_player = input()
second_player = input()

if (first_player == options[0] and (second_player == options[1] or second_player == options[3])) or (
        first_player == options[1] and (second_player == options[2] or second_player == options[3])) or (
        first_player == options[2] and (second_player == options[0] or second_player == options[4])) or (
        first_player == options[3] and (second_player == options[2] or second_player == options[4])) or (
        first_player == options[4] and (second_player == options[0] or second_player == options[1])):
    combination = 0
elif (first_player == options[0] and (second_player == options[2] or second_player == options[4])) or (
        first_player == options[1] and (second_player == options[0] or second_player == options[4])) or (
        first_player == options[2] and (second_player == options[1] or second_player == options[3])) or (
        first_player == options[3] and (second_player == options[0] or second_player == options[1])) or (
        first_player == options[4] and (second_player == options[2] or second_player == options[3])):
    combination = 1

print(results[combination])

# ============================
# options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
# results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]
#
# timur_move = input()
# ruslan_move = input()
#
# case = options.index(timur_move) - options.index(ruslan_move)
# res = results[case]
#
# print(res)
