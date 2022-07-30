## 카드 정렬하기

# 두 묶음의 숫자카드에서 각 묶음의 카드 수 A, B
# 두 묶음을 합쳐 하나로 만드는데 A+B 번의 비교 필요.

import heapq

n = int(input())

# 효율적으로(최소로) 비교하려면?
# 합치고나서 정렬을 다시 갱신하고 또 합치고를 반복.
# ex) 20, 30, 40 => 50, 40 ->sort-> 40, 50

# 최소값을 꺼내는데 정렬이 필요하고, 시간초과가 나지않기위해 heapq 사용

cards = []
for i in range(n):
    data = int(input())
    heapq.heappush(cards, data) # card에 받은 카드 묶음수를 넣는다.

ans = 0
while len(cards) != 1:
    # 최소 묶음수의 카드를 차례로 두개 꺼내서 합쳐 하나로.
    one = heapq.heappop(cards)
    two = heapq.heappop(cards)

    sum_card = one+two
    ans += sum
    heapq.heappush(cards, sum_card)

print(ans)