a = int(input())
b = int(input())
c = int(input())

cnt = 0

if (a==b):
    cnt += 1
if (a==c):
    cnt += 1
if (b==c):
    cnt += 1

if(cnt==1):
    print("2")
else:
    print(cnt)