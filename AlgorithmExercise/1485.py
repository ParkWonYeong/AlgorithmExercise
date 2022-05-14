## 1485

def check_sq(c):
    
    line1 = (c[0][0]-c[1][0])**2+(c[0][1]-c[1][1])**2
    line2 = (c[1][0]-c[3][0])**2+(c[1][1]-c[3][1])**2
    line3 = (c[0][0]-c[2][0])**2+(c[0][1]-c[2][1])**2
    line4 = (c[2][0]-c[3][0])**2+(c[2][1]-c[3][1])**2
    cross1 = (c[0][0]-c[3][0])**2+(c[0][1]-c[3][1])**2
    cross2 = (c[2][0]-c[1][0])**2+(c[2][1]-c[1][1])**2

    if line1 == line2 == line3 == line4:
        if cross1 == cross2:
            return 1
        else:
            return 0
    else:
        return 0

## main ##
t = int(input())

for i in range(t):
    coordinate=[]
    for j in range(4):
        x,y= list(map(int, input().split()))
        coordinate.append((x,y))
    coordinate.sort(key=lambda x:(x[0], x[1]))  # 좌아래, 좌위, 우아래, 우위 순으로 정렬됨.
    print(check_sq(coordinate))

# 30840KB, 408ms