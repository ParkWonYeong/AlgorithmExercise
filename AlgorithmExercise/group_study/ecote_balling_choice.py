## 볼링공 고르기

n,m = map(int, input().split()) # n: 볼링공 개수 / m: 볼링공 최대무게
weight = list(map(int, input().split()))
ans = 0

# 이중반복문으로 비교
for i in range(n):
    for j in range(i,n):
        if weight[i] != weight[j]:
            ans += 1

print(ans)