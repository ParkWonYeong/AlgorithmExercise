## 안테나

n = int(input())
location = list(map(int, input().split()))

# 중간값 구하기
location.sort()
print(location[(n-1)//2])