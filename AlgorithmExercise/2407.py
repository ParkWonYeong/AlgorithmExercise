## 2407

n,m = map(int, input().split())
ans = 1
for i in range(n):
    ans *= i+1
for j in range(m):
    ans //= j+1
for k in range(n-m):
    ans //= k+1
print(ans)

# 30840KB, 68ms