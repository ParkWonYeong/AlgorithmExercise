## 화성탐사

import sys
input = sys.stdin.readline

t = int(input())    # 테스트케이스 수

for _ in range(t):
    cost = []
    
    n = int(input())    # 테스트 케이스마다 주어지는 탐사 공간의 크기(NxN)
    for _ in range(n):
        cost.append(list(map(int, input().split())))
