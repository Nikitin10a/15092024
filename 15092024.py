x = int(input("Введите 4 цифры года: "))
digit1 = x // 1000
digit2 = (x // 100) % 10
digit3 = (x // 10) % 10
digit4 = x % 10
sum = digit1 + digit2 + digit3 + digit4
print(sum)
if sum % 4 == 0:
    print("особенный")
else:
    print("не особенный")


