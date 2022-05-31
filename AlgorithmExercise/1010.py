## 1010
# combination 구현

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())
for _ in range(T):
    n,m = map(int, input().split())
    answer = factorial(m) // (factorial(n) * factorial(m-n))
    print(answer)

# 30840KB, 108ms