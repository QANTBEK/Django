def bin_to_dec(binary, decimal):
    for digit in binary:
     decimal = decimal*2 + int(digit)
    return decimal


binary = input()
decimal = 0
print (bin_to_dec(binary,decimal))