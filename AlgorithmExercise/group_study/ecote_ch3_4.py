## 1이 될 때까지

import sys
input = sys.stdin.readline

n,k = map(int, input().split())
count = 0

while n != 1:
    sub_1 = n%k
    n -= sub_1
    n //= k
    count += 1+sub_1
    print('n= ', n)

print(count)