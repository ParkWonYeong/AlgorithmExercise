## 14681

# (+,+) => 1사분면 / (-,+) => 2사분면 / (-,-) => 3사분면 / (+,-) => 4사분면

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)

else:
    if y > 0:
        print(2)
    else:
        print(3)

# 30840KB, 72ms