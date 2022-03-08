## 17413

# sol 1. reverse()를 이용한다.
import sys
s = list(sys.stdin.readline().rstrip())

i,start = 0,0
for i in s:
    
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1

    # 'isalnum()': 문자열이 영어, 한글 혹은 숫자로 되어있으면 참.
    # 비슷한 경우로 isalpha()가 있다. 이 경우엔 영어, 한글일 경우에만 참이다.
    elif s[i].isalnum():    # 숫자나 알파벳을 만난 경우
        start = i
        while i < len(s) and s[i].isalnum():
            i += 1
        temp = s[start:i]   # <>를 제외한 숫자, 알파벳 범위에 있는 모든 문자를
        temp.reverse()      # reverse를 이용해 뒤집어준다.
        s[start:i] = temp
    
    else:                   # 공백인 경우
        i += 1              # 그냥 증가시킨다.

print("".join(s))

# 33208KB, 96ms


# sol 2. stack을 이용한다.

import sys

ans,stack = "",""
tag = False

for i in sys.stdin.readline().rstrip():

    # <, > 내의 문자열은 그대로 출력한다.
    if i == "<":
        tag = True
        ans += stack[::-1]
        stack = ""
        ans += i
        continue
    elif i == ">":
        tag = False
        ans += i
        continue

    # 공백이 나올 경우 스택에 담았던 문자열을 뒤집어 출력한다.
    elif i == " ":
        ans += stack[::-1] + " "
        stack = ""
        continue

    if tag:
        ans += i
    else:
        stack += i
print(ans+stack[::-1])

# 30864KB, 96ms