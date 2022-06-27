## 그리디 실전문제 2 - 숫자카드게임

import sys
input = sys.stdin.readline

n,m = map(int, input().split()) # 행과 열
card = []
for _ in range(n): # 행만큼
    check = list(map(int, input().split()))
    # print('check', check)
    card.append(min(check))
    # print('card', card)

print(max(card))