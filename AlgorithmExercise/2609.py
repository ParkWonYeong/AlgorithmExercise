## 2609

from math import gcd
import sys
x,y = map(int, sys.stdin.readline().split())

# 첫째줄에는 주어진 두 수의 최대공약수를 출력한다.
ans1 = gcd(x,y)
print(ans1)
# 둘째줄에는 주어진 두 수의 최소공배수를 출력한다.
ans2 = x*y//ans1    # 최소공배수는 두 수의 곱에 최소공배수를 나눈 값이다.
print(ans2)

# 32976KB, 68ms