## 1010

T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    
    if m == 1:
        answer = n
        break

    N,M = n,m
    for i in range(1, m+1):
        N *= n-i
        M *= m-i
    print(M//N)