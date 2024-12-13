def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return factorial(N-1) * N
number = input("Введите число ")
print(f"Факториал {number} равен {factorial(int(number))}")