## 정렬된 배열에서 특정 수의 개수 구하기

import sys
input = sys.stdin.readline

n,x = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
check_on = 0            # 해당 숫자가 시작되는 지점에서 1로 바꾼다.
while num:
    check = num.pop(0)
    cnt += 1
    if check == x and check_on == 0:
        start_point = cnt
        check_on = 1
    elif check != x and check_on == 1:
        end_point = cnt
        break
print(end_point-start_point)