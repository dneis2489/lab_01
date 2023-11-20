def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a

# Пример использования
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

gcd = euclidean_algorithm(num1, num2)

print(f"Наибольший общий делитель ({num1}, {num2}): {gcd}")