a = int(input())
b = int(input())

print(
    a * (1 % (a // b + 1)) +
    b * (1 % (b // a + 1)) *
    (1 % ((int((a * b) - a ** 2) + 1)))
)