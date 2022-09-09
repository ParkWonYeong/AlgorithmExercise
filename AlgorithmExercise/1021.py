## 1021: 회전하는 큐

from collections import deque

# 연산 2
def sol1(q):
    x = q.popleft()
    q.append(x)

# 연산 3
def sol1(q):
    x = q.pop()
    q.appendleft(x)


n, m = map(int, input().split())
q = deque([(i+1) for i in range(n)])
want = list(map(int, input().split()))
print(q)
print(want)

now = 1         # 현 위치
cnt = 0         # m까지 카운트
while cnt==m:
    # 절댓값 계산해서 왼쪽 이동이 가까우면 2, 그렇지 않으면 3번 연산
    