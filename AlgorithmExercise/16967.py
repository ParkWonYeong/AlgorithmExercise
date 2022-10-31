### 배열 복원하기

# 야매 풀기 시도
from collections import deque
import sys
input = sys.stdin.readline

h,w,x,y = map(int, input().split())
answer = []

for _ in range(h+x):
    check = deque(map(int, input().split()))

    if check[0] == 0:   # 앞부분이 0인 줄이면
        while check[0] == 0:
            check.popleft()
        if list(check) not in answer:
            answer.append(list(check))

    elif check[-1] == 0:    # 뒷부분이 0인 줄이면
        while check[-1] == 0:
            check.pop()
        answer.append(list(check))

for i in answer:
    print(*i)

## 예제는 맞았으나 채점 틀림(^^...)



### 정답 코드 ###
H, W, X, Y = map(int, input().split())

arr_B = list(list(map(int, input().split())) for _ in range(H+X))
arr_A = [arr_B[i][:W] for i in range(X)] + [[0]*W for _ in range(H-X-1)] + [arr_B[-1][Y:W+Y]]

for i in range(H):
    if i < X:
        print(*arr_A[i])
        continue
    if i == H-1:
        print(*arr_A[-1])
        continue

    for j in range(W):
        # 앞부분에만 겹침없이 포함되는 경우(별도 연산없이 그대로 출력)
        if j < Y:
            arr_A[i][j] = arr_B[i][j]
            print(arr_B[i][j], end=' ')
            continue

        # 겹치는 부분 계산(Bij = Aij + A(i-X)(j-Y) 식 이용)
        arr_A[i][j] = arr_B[i][j] - arr_A[i-X][j-Y]
        print(arr_A[i][j], end=' ')
    print()