## 9093

import sys

for i in range(int(sys.stdin.readline())):
    s = list(sys.stdin.readline().rstrip().split()) # 단어가 공백마다 배열요소로 추가된다

    for j in s:
        print(j[::-1], end=' ')  # 공백을 주며 거꾸로 출력한다.

# 30860KB, 164ms