## 연산자 끼워넣기

# N개의 수로 이루어진 수열
# 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자(덧셈,뺄셈,곱셈,나눗셈)

# 식의 계산은 연산자 우선순위 무시하고 앞에서부터 진행
# 나눗셈은 나눗셈은 정수 나눗셈으로 몫만 취함
# 음수를 양수로 나눌 때는 -(나눗셈결과)
# 만들수 있는 식의 결과가 최대인 것과 최소인 것 구하기

import sys
input = sys.stdin.readline

def dfs(depth, total, sum, sub, mux, div):
    global max_num, min_num

    if depth == n:  # 만약 가장 깊이 도달했다면 종료
        max_num = max(total, max_num)
        min_num = min(total, min_num)
        return

    if sum > 0:
        dfs(depth+1, total+num[depth], sum-1, sub, mux, div)
    
    if sub > 0:
        dfs(depth+1, total-num[depth], sum, sub-1, mux, div)

    if mux > 0:
        dfs(depth+1, total*num[depth], sum, sub, mux-1, div)

    if div > 0:
        if total < 0:   # 음수일 경우
            total = -(abs(total)//num[depth])
        else:
            total = total//num[depth]
        dfs(depth+1, total, sum, sub, mux, div-1)


n = int(input())    # 수의 개수
num = list(map(int, input().split()))
operators = list(map(int, input().split()))     # [덧셈, 뺄셈, 곱셈, 나눗셈]
max_num, min_num = -1e9, 1e9

dfs(1, num[0], operators[0], operators[1], operators[2], operators[3])

print(max_num)
print(min_num)