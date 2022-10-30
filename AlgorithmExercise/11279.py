## 최대 힙
# 튜플을 원소로 추가하거나 삭제하면
# 튜플 내 맨 앞에 있는 값을 기준으로 최소 힙이 구성됨
# => 최대 힙을 만들려면 각 값에 대한 우선순위를 구하고
# (우선순위, 값) 구조의 튜플을 힙에 추가하거나 삭제하기.
# 이후 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값 취하기

import sys
import heapq
input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    x = int(input())

    if x > 0 :
        heapq.heappush(arr, (-x, x))  # 우선순위, 값
    elif x == 0:
        if len(arr) == 0:
            a = 0
        else:
            a = heapq.heappop(arr)[1]

        print(a)