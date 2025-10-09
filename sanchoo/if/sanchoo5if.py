# Ввод трех целых чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

# Считаем количество положительных и отрицательных чисел
positive_count = 0
negative_count = 0

for num in (a, b, c):
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Количество положительных чисел:", positive_count)
print("Количество отрицательных чисел:", negative_count)