## 16953.py

### solve 1 ###
# BFS 풀이(bottom-up)
from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    # queue = deque()
    # queue.append((a,1))
    queue = deque([(a,1)])  # 1은 연산 횟수를 의미한다(cnt = 1(연산 최솟값에 1을 더한 값))
    
    while queue:
        now, cnt = queue.popleft()  # queue에 원소가 존재할 때 pop한다.
        if now == b:                # pop한 원소가 b와 같다면,
            print(cnt)              # 연산횟수를 출력하고 종료한다.
            return        
        if now*2 <= b:              # 2배한 값이 b보다 작거나 같다면,
            queue.append((now*2, cnt+1))    # 이를 계산하여 큐에 넣어준다.
        if now*10+1 <= b:           # 끝에 1을 붙인값이 b보다 작거나 같다면,
            queue.append((now*10+1, cnt+1)) # 이를 계산하여 큐에 넣어준다.
    else:
        print(-1)

a,b = map(int, input().split())     # A,B가 주어진다.
bfs(a,b)

# *2 연산을 우선으로 하는 경우의 속도가 아주 약간 더 빨랐다.
# 32368KB, 112ms/116ms



### solve 2 ###
# top-down(거꾸로 생각하기), b를 a로 만들자.
import sys
input = sys.stdin.readline

a,b = map(int,input().split())
cnt = 1
while(b!=a):

    if a>b:
        cnt = -1
        break

    # 연산에 있어 속도적으로 우위를 점하는 것은 수의 끝에 있는 1을 없애는 것이다.
    # 따라서 b의 끝에 1이 존재한다면 우선 끝의 1을 빼는 것이 최선이다.
    elif b%10 == 1:   # b를 10으로 나누었을때 나머지가 1이면(끝에 1이 존재한다면)
        b//=10      # 끝의 1을 뺀다.(10을 나눠 소수점없이 구해주면 된다)
        cnt += 1
    
    # 그럴 수 없을 경우 어쩔수없이 2로 나누는 연산을 해야하지만,
    # 홀수일 경우 2로 나눌 수 없으니 짝수인 경우에만 2로 나누도록 한다.
    elif b%2 == 0:  # b가 짝수인 경우
        b//=2       # 2로 나눈다.
        cnt += 1

    # 그 외의 경우인데 반복하게 된다면 무한루프에 빠지므로 cnt=1로 두고 반복문을 빠져나온다.
    else:
        cnt = -1
        break

print(cnt)

# 30860KB, 68ms