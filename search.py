def search_max(a):
    if len(a) == 0:
        return 0
    return a[0] if a[0] > search_max(a[1:]) else search_max(a[1:])
user_input = [7, 2, 5, 3, 6]
print(f"Максимальный элемент списка: {search_max(user_input)}")