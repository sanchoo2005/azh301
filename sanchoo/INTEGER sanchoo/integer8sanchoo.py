num = int(input("Введите двузначное число: "))
if 10 <= abs(num) <= 99:
    tens = abs(num) // 10
    ones = abs(num) % 10
    swapped = ones * 10 + tens
    if num < 0:
        swapped = -swapped
    print(swapped)
else:
    print("Число не двузначное.")
