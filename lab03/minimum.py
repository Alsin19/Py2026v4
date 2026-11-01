a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))

minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c

print(f"Минимальное число: {minimum}")

