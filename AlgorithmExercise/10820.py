## 10820

# 문자열 N개가 주어질 때, 포함된 소문자, 대문자, 숫자의 공백 수를 구하라.

import sys

while 1:
    n = sys.stdin.readline().rstrip('\n')   # 한줄씩 문자열 입력값을 받는다.

    if not n:       # 더이상 문자열이 출력되지 않을 경우
        break

    lower, upper, digital, space = 0,0,0,0
    for i in n:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            digital += 1
        elif i.isspace():
            space += 1

    print(lower, upper, digital, space)

# 30864KB, 68ms