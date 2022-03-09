## 1676

# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램

import sys
n = int(sys.stdin.readline())

ans,mux = 0,1
for i in range(n):
    mux *= (i+1)
mux = str(mux)
fac = ""
fac = mux[::-1]
for i in fac:
    if i != "0":
        ans += 0
        break
    else:
        ans += 1
        continue

print(ans)

# 30864KB, 72ms