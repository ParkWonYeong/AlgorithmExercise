## 1021: 회전하는 큐

from collections import deque

n, m = map(int, input().split())
q = deque([(i+1) for i in range(n)])
want = deque(map(int, input().split()))

cnt = 0
while want:
    # 왼쪽 이동이 가까우면 2, 그렇지 않으면 3번 연산
    # 중간지점을 나눠 왼쪽에 있다면 왼쪽으로 이동(연산 2)하는 것이 더 빠르다.
    # 반면 오른쪽에 있으면 오른쪽으로 이동(연산 3)하는 것이 더 빠르다.
    
    mid = len(q)//2

    # 연산 2
    if q.index(want[0]) <= mid:     # mid와 같은 값일 때도 연산2가 더 빠름 유의.
        while want[0] != q[0]:
            q.append(q.popleft())
            cnt += 1

    # 연산 3
    else:
        while want[0] != q[0]:
            q.appendleft(q.pop())
            cnt += 1

    q.popleft()
    want.popleft()

print(cnt)