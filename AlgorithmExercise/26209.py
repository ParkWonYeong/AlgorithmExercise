## Intercepting Information

import sys
si = sys.stdin.readline

line = list(map(int, si().split()))
if max(line) > 1:
    print('F')
else:
    print('S')