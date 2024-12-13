def sum(a):
    if len(a) == 0:
        return 0
    else:
        return sum(a[1:]) + int(a[0])
user_input = [7, 2, 5, 3, 6]
print(f"Cумма элементов массива равна: {sum(user_input)}")