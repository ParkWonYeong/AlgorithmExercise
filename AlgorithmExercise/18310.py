## 18310
## 안테나

n = int(input())
loc = list(map(int, input().split()))
loc.sort()

if n % 2 == 0:   # 짝수개인 경우
    print(loc[n//2 - 1])
else:
    print(loc[(n+1)//2 - 1])