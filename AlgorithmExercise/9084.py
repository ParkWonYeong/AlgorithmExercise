## 9084

import sys

for _ in range(3):
    cnt = 0
    T = int(sys.stdin.readline())       # 테스트 케이스 개수
    N = int(sys.stdin.readline())       # 동전 N가지
    coin = list(map(int, sys.stdin.readline().split()))
    money = int(sys.stdin.readline())
    for i in coin:
        if money % coin == 0:
            cnt += 1


    print(cnt)