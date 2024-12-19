def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    ten_pow = 10 ** half_n
    a = x // ten_pow
    b = x % ten_pow
    c = y // ten_pow
    d = y % ten_pow

    ac = karatsuba(a, c)          
    bd = karatsuba(b, d)          
    ab_cd = karatsuba(a + b, c + d)  

    ad_bc = ab_cd - ac - bd

    result = (ac * 10 ** (2 * half_n)) + (ad_bc * 10 ** half_n) + bd
    return result

x = 12345678
y = 87654321

result = karatsuba(x, y)
print(f"Результат умножения: {result}")
print(f"Ожидаемый результат: {x * y}")

input("Нажмите Enter, чтобы закрыть программу...")