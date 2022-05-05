## 11050

N,K = map(int, input().split())

n, m = 1,1

for i in range(K):
    n *= (N-i)
    m *= (K-i)

print(n//m)

# 30840KB, 68ms