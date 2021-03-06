## 11653

import sys

n = int(sys.stdin.readline())

# 소인수분해 마칠 때까지(n이 해당 소인수로 전부 나눠져서 1이 될 때까지) 반복문을 돌린다.
while n != 1:
    # 소인수 '2'부터 하나씩 나눠본다.
    for i in range(2, n+1): # 나눠지면 해당 수를 출력하고 n을 나눠준다.
        # 해당 수는 반복을 거듭할 때마다 1씩 증가한다.
        if(n%i==0): # 나머지가 0일때까지(해당 숫자로 나눌 수 없을 때까지) 나눈다.
            print(i)
            n = n//i
            break   # break는 반복문 내에서 종료하는 것이므로 또다시 조건을 만족할 때까지 반복문은 진행된다.

# 30864KB, 1064ms