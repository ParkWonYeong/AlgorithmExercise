## 10952

import sys
input = sys.stdin.readline
while 1:

    num1, num2 = map(int, input().split())
    if num1 == 0 & num2 == 0:
        break
    else:
        ans = num1+num2
        print(ans)

# 30864KB, 72ms