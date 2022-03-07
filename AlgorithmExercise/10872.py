## 10872

import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)

else:
    mux = 1
    for i in range(n):
        mux *= (i+1)
    print(mux)

## 30860KB, 72ms