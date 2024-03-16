# На вход программе подается строка текста из натуральных чисел.
# Из элементов строки формируется список чисел. Напишите программу циклического сдвига элементов списка направо,
# когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.

number_list = [int(num) for num in input().split()]
number_list.insert(0, number_list[-1])
print(*number_list[:-1])

# =======================
# seq = input().split()
# new_seq = [seq[-1]] + seq[:-1]
# print(*new_seq)
# =========================
# seq = input().split()
#
# new_seq = []
# new_seq.append(seq[-1])
# new_seq.extend(seq[:-1])
#
# print(*new_seq)
# ==========================
# a = input().split()
#
# print(*[a[-1]] + a[:-1])
# =============================
# digits = [int(c) for c in input().split()]
#
# digits.insert(0, digits.pop())
#
# print(*digits)

