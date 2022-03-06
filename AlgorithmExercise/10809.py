## 10809

# 알파벳 소문자로만 이루어진 문자열 s
# 각각의 알파벳에 대해 단어에 포함되어 있는 경우에는 처음 등장하는 위치,
# 포함되어 있지 않은 경우는 -1을 출력하라.

import sys
input = sys.stdin.readline

s = str(input().strip())
alpha = 'abcdefghijklmnopqrstuvwxyz'    # ['a','b','c',...'z']와 같이 배열로 두는 것보다 문자열이 처리속도가 더 빠르다.

for i in alpha: # 알파벳 수(26개)만큼 반복해준다.
    if i in s:              # 문자열 내에 해당 알파벳이 있는 경우
        print(s.index(i), end = ' ')   # 해당 문자열의 index를 출력한다.
    else:                   # 문자열 내에 해당 알파벳이 없는 경우
        print(-1, end = ' ')           # -1을 출력한다.

# 30864KB, 68ms