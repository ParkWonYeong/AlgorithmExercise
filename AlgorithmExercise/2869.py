## 2869
import sys
a,b,v = map(int, sys.stdin.readline().split())
c = a-b
day, cnt = 0,0
while 1:
    cnt += a
    if cnt >= v:
        print(day)
        break
    cnt -= b
    day += 1

## 시간초과 발생

import sys
import math
a,b,v = map(int, sys.stdin.readline().split())
day = (v-b)/(a-b)           # v가 아닌 v-b인 이유는 정상에 올라간 뒤 밤에 미끄러지지 않음을 고려.
print(math.ceil(day))       # day의 소수점 절상.

## 32952KB, 72ms