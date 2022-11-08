## 부분 수열의 합

# n개의 정수로 이루어진 수열
# 크기가 양수인 부분 원소를 다 더한 값이 S가 되는 경우의 수
# 출력 - 합이 S가 되는 부분수열의 개수 출력하기

### sol 1 : combination으로 n개의 조합 구하기 ###
import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, n+1):
    comb = combinations(arr, i)
    # print(list(comb))

    for x in comb:
        if sum(x) == s:
            cnt += 1

print(cnt)

# 30840 KB, 408ms


### sol 2 : dfs ###

def dfs(i, sum):
    global ans

    if i >= n:
        return

    # print('arr[i]=',arr[i], ', sum=', sum)
    sum += arr[i]

    if sum == s:
        ans += 1

    dfs(i+1, sum)           # 현재 arr[i]를 선택한 경우
    dfs(i+1, sum-arr[i])    # 현재 arr[i]를 선택하지 않은 경우

n,s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

dfs(0,0)
print(ans)

# 30840 KB, 512ms