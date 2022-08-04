## 14888
## 연산자 끼워넣기 - DFS

import sys
input = sys.stdin.readline

n = int(input())
# 최댓값, 최솟값을 모두 출력해야한다.
max_num, min_num = -1e9, 1e9    # 초기값

def dfs(depth, total, sum, sub, mul, div):
    global max_num, min_num
    if depth == n:
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return
    
    if sum:
        dfs(depth+1, total+num[depth], sum-1, sub, mul, div)
    if sub:
        dfs(depth+1, total-num[depth], sum, sub-1, mul, div)
    if mul:
        dfs(depth+1, total*num[depth], sum, sub, mul-1, div)
    if div:
        # 음수를 양수로 나눌때는 양수로 바꾼뒤 몫을 취하고 음수 붙이기
        dfs(depth+1, total//num[depth], sum, sub-1, mul, div-1)


num = list(map(int, input().split()))
operate = list(map(int, input().split()))   # + - * /
dfs(1, num[0], operate[0], operate[1], operate[2], operate[3])

# 최대값, 최솟값 순으로 출력
print(max_num)
print(min_num)