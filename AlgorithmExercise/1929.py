## 1929

import sys
input = sys.stdin.readline

a,b = map(int, input().split())

if a < 2:
  a = 2

for i in range(a, b+1):
  check = False
  for j in range(2, int(i**0.5)+1):  # 해당 숫자의 제곱근까지 검사해도 소수가 판별됨.
    if i % j == 0:
      check = True
      break
  if check == False:        # 소수이면 print한다.
    print(i)