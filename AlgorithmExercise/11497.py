## 11497

t = int(input())

for _ in range(t):
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    ans = 0
    for i in range(0,n-2):
        ans = max(ans, abs(trees[i+2] - trees[i]))
    print(ans)