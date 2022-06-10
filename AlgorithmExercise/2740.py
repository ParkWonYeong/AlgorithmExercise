## 2740

import sys
input = sys.stdin.readline

# Matrix A
n,m = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

# Matrix B
m,k = map(int, input().split())
B = []
for _ in range(m):
    B.append(list(map(int, input().split())))

ans = []

for i in range(n):
    ans = []
    for j in range(k):
        answer = 0
        for l in range(m):
            answer += A[i][l]*B[l][j]
        ans.append(answer)
    print(*ans)     # *로 출력시 join(str~) 쓸 필요없이 출력됨.

# 30840KB, 208ms