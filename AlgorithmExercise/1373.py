## 1373

import sys
# oct: 8진법
# input(),2의 ',2'는 2진법의 숫자로 받는다는 의미
# 답안에서는 숫자만을 출력하라고 했으므로 앞의 0x을 제거하기 위해 [2:]
print(oct(int(sys.stdin.readline(),2))[2:])