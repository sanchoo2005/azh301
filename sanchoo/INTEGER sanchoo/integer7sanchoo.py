# Ввод двузначного числа
num = int(input("Введите двузначное число: "))

# Получение цифр
a = num // 10
b = num % 10

# Сумма и произведение цифр
sum_digits = a + b
prod_digits = a * b

print("Сумма цифр:", sum_digits)
print("Произведение цифр:", prod_digits)