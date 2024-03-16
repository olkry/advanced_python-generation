# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" соответствует выпадению Орла,
# а буква "Р" - выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.

list_inp = input().split('О')
print(len(max(list_inp)))
# =====================
# count = 0
# grabber = 0
# for char in list_inp:
#     if char == 'Р':
#         grabber += 1
#     else:
#         grabber = 0
#
#     if count < grabber:
#         count = grabber
#
# print(count)

