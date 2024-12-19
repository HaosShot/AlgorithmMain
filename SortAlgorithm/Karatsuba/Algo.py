def Karatsuba(x, y, n):
    if n == 1:  
        return x * y

    if n % 2 == 0:  
        ten_pow = 10 ** (n // 2)

        a = x // ten_pow
        b = x % ten_pow
        c = y // ten_pow
        d = y % ten_pow
    else:  
        ten_pow = 10 ** (n // 2)

        a = x // ten_pow
        b = x % ten_pow
        c = y // ten_pow
        d = y % ten_pow

    step_1 = a * c
    step_2 = b * d
    step_3 = (a + b) * (c + d)
    step_4 = step_3 - step_1 - step_2
    step_5 = step_1 * (10 ** (2 * (n // 2))) + step_4 * (10 ** (n // 2)) + step_2

    return step_5

x = 123456789123456789
y = 987654321987654321
n = max(len(str(x)), len(str(y)))

result = Karatsuba(x, y, n)
print(f"Результат умножения: {result}")
print(f"Ожидаемый результат: {x * y}")

input("Нажмите Enter, чтобы закрыть программу...")