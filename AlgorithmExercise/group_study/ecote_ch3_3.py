### 숫자 카드 게임

import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ans = 0

for i in range(n):
    cards = list(map(int, input().split()))
    card = min(cards)
    ans = max(ans, card)

print(ans)