## 9613

import math
import sys

t = int(sys.stdin.readline())

i = 0
# 수의 개수 n, 그 다음에 n개의 개수이므로 n[0]을 뛰어넘고 GCD를 구한다.


# for 문을 이용한 반복문 짜기
for i in range(t):
    n = list(map(int, sys.stdin.readline().split()))
    ans = 0
    # 케이스 내에서 가능한 모든 쌍의 GCD를 구하여
    for j in range(1, len(n)):              # index 1번째부터 끝까지 시작
        for k in range(j+1, len(n)):        # j와 겹치지 않게 j보다 1 큰수부터 끝까지 시작
            ans += math.gcd(n[j], n[k])     # 그 합을 출력한다.
    print(ans)

# 32972KB, 72ms



# 별해: for 문을 전부 while문을 이용해서 반복문 짜기
while (i<t):
    n = list(map(int, sys.stdin.readline().split()))
    ans = 0
    # 케이스 내에서 가능한 모든 쌍의 GCD를 구하여
    j = 1
    while (j<len(n)):              # index 1번째부터 끝까지 시작
        k = j+1
        while (k<len(n)):        # j와 겹치지 않게 j보다 1 큰수부터 끝까지 시작
            ans += math.gcd(n[j], n[k])     # 그 합을 출력한다.
            k += 1
        j += 1
    print(ans)
    i += 1

# 32976KB, 68ms