## 2164

# 정석

from collections import deque

n = int(input())
card = deque()

for i in range(n):
    card.append(i+1)

while (len(card) != 1):
    card.popleft()
    card.append(card.popleft())

print(card[0])

# 매우 느림. for 문으로 1~50만에 달하는 숫자를 반복해야해서 그렇다.
# 49284KB, 280ms



### 별해 ###
# 1은 우선 버리게 되므로 2부터 생각해봄.
# 순서대로 버리면 전부 홀수를 버리고 짝수가 오름차순으로 정렬되는 구간이 생김
# n이 짝수면 버리는 것부터 시작하고, n이 홀수면 뒤로 보내는 것부터 시작한다.
# 반으로 갈라질 때마다 숫자의 간격이 2의n승 배수만큼 차이가 난다.

n = int(input())
mag = 2

i = 0
while 1:
    if n < 3:
        print(n)
        break

    mag *= 2
    if mag >= n:
        # 입력값보다 작은 2의 n제곱의 가장 큰 수를 구하고, n과 그 값의 차를 두배 한 값.
        print((n - (mag//2)) * 2)
        break

# 30840KB, 68ms