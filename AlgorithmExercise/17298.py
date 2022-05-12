## 17298

##### 재귀함수를 이용한 풀이 #####

import sys
sys.setrecursionlimit(10**6)

def NGE(i):

    if i == n-1:
        ans.append(-1)
        return

    elif a[i+1] > maxnum:
        ans.append(a[i+1])
        return

    else:
        NGE(i+1)

## main ##
n = int(input())
a = list(map(int, input().split()))
ans = []*(n+1)

for i in range(n):
    maxnum = a[i]
    NGE(i)

print(' '.join(map(str, ans)))
######## 시간초과 #######


##### stack을 이용한 풀이 #####

# stack은 값이 아닌 index를 저장해야 한다. 

from collections import deque

n = int(input())
a = list(map(int, input().split()))
ans = [-1]*n            # 처음부터 -1을 넣은 배열로 생성한다.
stack = deque()

for i in range(n):
    # stack이 비어있지 않고 stack의 맨 오른쪽(위) 수가 a[i]보다 작은 경우 종료
    while (stack and (stack[-1][0] < a[i])):
        temp, idx = stack.pop()     # pop 함과 동시에 오큰수 업데이트
        ans[idx] = a[i]     # ans에서 그다음 index만큼 옮겨서 a[i]값을 할당한다.

    stack.append([a[i], i])

# print(' '.join(map(str, ans))), 포인터를 이용해서 동일하게 출력 가능
print(*ans)

## 205420KB, 1768ms