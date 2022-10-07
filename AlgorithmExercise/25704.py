## 출석 이벤트

import sys
input = sys.stdin.readline

n = int(input())
p = int(input())

price = p

if n//5 > 0:
    price = min(p-500, price)
if n//10 > 0:
    price = min(p*0.9, price)
if n//15 > 0:
    price = min(p-2000, price)
if n//20 > 0:
    price = min(p*0.75, price)
if price < 0:
    price = 0

print(int(price))