a = int(input("a: "))
b = int(input("b: "))

if a < b:
    # По возрастанию: range(a, b + 1) включает b
    for number in range(a, b + 1):
        print(number)
elif a > b:
    # По убыванию: range(a, b - 1, -1) включает b
    for number in range(a, b - 1, -1):
        print(number)
else:
    # Одно число при равенстве
    print(a)

