n = int(input())
result = n * 45
result += (n // 2 - 1 + n % 2) * 15
result += ((n + 1) // 2 - 1 + (n + 1) % 2) * 5
print('%d %d' % (result // 60 + 9, result % 60))