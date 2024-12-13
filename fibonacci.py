def fibonacci(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)
number = input("Введите число ")
print(f"Число Фибоначчи номер {number} это {fibonacci(int(number))}")