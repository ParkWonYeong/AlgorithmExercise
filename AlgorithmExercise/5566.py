## 5566

import sys

n,m = map(int, sys.stdin.readline().split())
board = []*(n+m+1)

# 0~(n-1)까지는 지시사항, n~끝까지는 주사위
for _ in range(n+m):
    board.append(int(sys.stdin.readline()))
# start는 칸의 위치를 나타냄. i는 주사위 굴린 횟수.
start,i = 1,0

while 1:
    if start >= n:
        print(i)
        break
    else:
        start += board[n+i]
        start += board[start-1]
        i += 1

# 30840KB, 68ms