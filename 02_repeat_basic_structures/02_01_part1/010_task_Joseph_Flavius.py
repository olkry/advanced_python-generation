# n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек
# выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу,
# определяющую номер человека, который останется в кругу последним.

persons = [per for per in range(1, int(input()) + 1)]
outer = int(input())
out_rout = 0
queue = len(persons)

while queue > 1:
    out_rout += outer - 1
    while out_rout >= queue:
        out_rout -= queue
    else:
        kill = persons.pop(out_rout)
        queue -= 1

print(*persons)

# ====================
# n = int(input())
# k = int(input())
#
# res = 0
# for i in range(1, n + 1):
#     res = (res + k) % i
# print(res + 1)

# ==================
#
# n = int(input())
# k = int(input())
#
# # создаем список людей, где каждый человек – просто номер
# people = list(range(1, n + 1))
# # переменная для текущей позиции "считалки"
# cur = 0
#
# # пока у нас больше одного человека
# while len(people) > 1:
#     # начинаем считалку от текущей позиции cur, постоянно увеличивая ее
#     for _ in range(k - 1):
#         cur += 1
#         # если считалка переваливает за последнего человека,
#         # то ставим ее на первого человека
#         if cur == len(people):
#             cur = 0
#
#     people.pop(cur)
#     # если удалили последнего человека,
#     # то считалку ставим на первого человека
#     if cur == len(people):
#         cur = 0
#
# # выводим единственного оставшегося человека
# print(people[0])