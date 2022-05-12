## 2460

# 기차 안에 사람이 가장 많을 때의 사람 수를 계산한다. 역은 10개이다.
# 단, 역에서 멈추면 기차를 탈 때 내린 사람이 모두 내린 후에 기차를 탄다.

riding = 0
ans = 0
for i in range(10):
    exto, into = map(int, input().split())
    riding -= exto
    riding += into
    ans = max(ans, riding)

print(ans)

# 30840KB, 72ms