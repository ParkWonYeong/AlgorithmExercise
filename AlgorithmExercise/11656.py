## 11656

import sys
s = sys.stdin.readline().rstrip()   # 문자열을 받는다.

suffix = []

for i in range(len(s)):
    suffix.append(s[i:])            # 문자열 S의 모든 접미사를 배열 suffix에 넣는다.

suffix.sort()                       # 사전순(오름차순)으로 정렬한다.

print('\n'.join(map(str, suffix)))

# 31840KB, 68ms