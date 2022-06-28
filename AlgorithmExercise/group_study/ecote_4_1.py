## ecote_Ch 4-1 상하좌우(구현)

# L: 왼, R: 오, U: 위, D:아래
N = int(input())    # 공간의 크기
place = list(map(str, input().split()))

h,w = 1,1           # h는 세로, w는 가로(h,w)
for i in place:
    if i == 'R':    # 오른쪽 이동
        if w+1 <= N:    w += 1
    elif i == 'L':  # 왼쪽 이동
        if w-1 >= 1:    w -= 1
    elif i == 'U':  # 위로 이동
        if h-1 >=1 :    h -= 1
    elif i == 'D':  # 아래로 이동
        if h+1 <= N:    h += 1

print(h, w)