## 정렬된 배열에서 특정 수의 개수 구하기

from collections import deque

import sys
input = sys.stdin.readline

n,x = map(int, input().split())
num = deque(map(int, input().split()))

cnt = 0
check_on = 0            # 해당 숫자가 시작되는 지점에서 1로 바꾼다.
while num:
    check = num.popleft()
    cnt += 1
    if check == x and check_on == 0:
        start_point = cnt
        check_on = 1
    elif check != x and check_on == 1:
        end_point = cnt
        break

    end_point = cnt+1   # 끝부분의 원소를 찾는경우 예외처리.
    
print(end_point-start_point)