def reverse(a):
    if len(a) == 0:
        return a
    else:
        return reverse(a[1:]) + a[0]
user_input = input("Введите строку ")
print(f"Строка записанная в обратном порядке: {reverse(user_input)}")