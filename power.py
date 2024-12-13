def degree(a,b):
    if b == 0:
        return 1
    return int(a) * degree(int(a), int(b)-1)
user_input_1 = input("Введите число ")
user_input_2 = input("Введите значение степени ")
print(f"Результат: {degree(user_input_1, user_input_2)}")