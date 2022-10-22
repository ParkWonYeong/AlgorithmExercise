## 큐 2

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())        # 명령의 수
q = deque([])

for i in range(n):
    cmd_ = input()

    if 'push' in cmd_:                  # push
        cmd_c, cmd_n = cmd_.split()
        X = cmd_n
        q.append(X)

    elif 'pop' in cmd_:                 # pop
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif 'size' in cmd_:                # size
        print(len(q))

    elif 'empty' in cmd_:               # empty
        if len(q) == 0:
            print(1)
        else:
            print(0)
    
    elif 'front' in cmd_:               # front
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif 'back' in cmd_:                # back
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
