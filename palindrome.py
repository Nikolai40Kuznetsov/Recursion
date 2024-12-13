def palindrome(a):
    if len(a) <= 1:
        return True
    if a[0] != a[-1]:
        return False
    return palindrome(a[1:-1])
user_input = input("Введите строку ")
print(palindrome(user_input))