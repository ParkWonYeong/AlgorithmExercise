## 4153

while 1:
    tri = list(map(int, input().split()))
    tri.sort()
    if tri[2]==0:
        break
    else:
        if tri[2]**2 == tri[0]**2 + tri[1]**2:
            print("right")
        else:
            print("wrong")

# 30840KB, 64ms