# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа.

number_list, count = [int(num) for num in input().split()], 0
for i in range(len(number_list) - 1):
    count += 1 if number_list[i] < number_list[i + 1] else 0
print(count)
