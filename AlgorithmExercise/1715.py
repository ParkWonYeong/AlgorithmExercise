## 카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())    # 숫자 카드 묶음의 개수

card = []

for i in range(n):
    num = int(input())
    heapq.heappush(card, num)

if n == 1:          # 카드묶음이 하나일 때는 비교할 필요가 없다.
    print(0)

else:
    card.sort()     # 최소 값을 구하기 위해 오름차순 정렬
    ans = 0
    while len(card) != 1: 
        one = heapq.heappop(card)
        two = heapq.heappop(card)

        card_sum = one + two
        ans += card_sum
        heapq.heappush(card, card_sum)
        
    print(ans)