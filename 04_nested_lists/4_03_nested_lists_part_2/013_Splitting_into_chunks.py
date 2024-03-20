# На вход программе подаются две строки: на одной – символы, на другой – число n. Из первой строки формируется список.
#
# Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков (кусков) указанной длины.

def chunked(text: list, chunk: int):
    el = [[text.pop(0)]]
    for element in text:
        if len(el[-1]) < chunk:
            el[-1].append(element)
        else:
            el.append([element])
    return el


print(chunked(input().split(), int(input())))

# ====================
def chunked(symbols, n):
    result = []
    for i in range(0, len(symbols), n):
        result.append(symbols[i:i + n])
    return result

symbols = input().split()
n = int(input())

print(chunked(symbols, n))
