## 10103

c,s = 100,100
for i in range(int(input())):
    a,b = map(int, input().split())
    if a == b:
        continue
    elif a > b:
        s -= a
    else:
        c -= b
print(c)
print(s)

# 30840KB, 68ms