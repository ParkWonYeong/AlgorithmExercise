## 치킨배달

from itertools import combinations

# N 도시길이, M 가능한 최대 치킨집 개수
n,m = map(int, input().split())
home, chicken = [],[]

for i in range(n):
    city = list(map(int, input().split()))
    for j in range(n):
        if city[j] > 0:
            # 1=home, 2=chicken
            if city[j] == 1:
                home.append((i,j))
            else:
                chicken.append((i,j))

# M개의 치킨집을 선택하는 경우의 수를 모은 리스트
pick = list(combinations(chicken, m))

# ans 값을 최대한으로 두고 min으로 줄여나간다.
ans = 1e9

# 각 경우의 수에 따른 치킨거리를 구한다.
for k in pick:
    chicken_sum = 0
    
    # "치킨거리"를 구한다.
    for dx, dy in home:
        chicken_distance = 1e9
        for mx, my in k:
            chicken_distance = min(chicken_distance, abs(dx-mx)+abs(dy-my))
        chicken_sum += chicken_distance
    
    ans = min(ans, chicken_sum)

print(ans)