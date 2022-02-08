## 10816

import sys
input=sys.stdin.readline

N=int(input())
num_sang=list(map(int, input().split()))

M=int(input())
num_M=list(map(int, input().split()))

# dictionary를 사용한다
# 상근이가 가진 숫자카드와 개수를 dictionary에 담는다.
dic={}
for i in num_sang:
    if i in dic:
        dic[i] += 1     # 앞서 나온것과 중복되는 카드숫자면 장수 추가
    else:
        dic[i] = 1      # 중복되는 카드숫자가 아니면 그냥 한 장

for i in num_M:
    if i in dic:
        print(dic[i], end = ' ')
    else:
        print(0, end = ' ')