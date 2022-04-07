## 2884

H,M = map(int, input().split())

if M<45:    # M이 45분보다 작은 경우
    if H == 0:      # 시간이 하루를 넘기는 경계일 경우
        h = 23
        m = M-45+60
    else:
        h = H-1
        m = M-45+60
else:       # M이 45분보다 크거나 같은 경우
    h = H
    m = M-45

print(h, m)

## 30864KB, 76ms