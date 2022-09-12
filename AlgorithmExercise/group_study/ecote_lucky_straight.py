## 럭키 스트레이트

# 럭키 스트레이트의 조건
# 점수 N을 반으로 나누어 왼쪽 부분의 각자리수 합 = 오른쪽 부분의 각 자릿수 합을 더한 값

n = input()     # 항상 짝수 자릿수의 형태

idx = len(n)//2

cal1, cal2 = n[:idx], n[idx:]
ans1, ans2 = 0,0

for i in range(idx):
    ans1 += int(cal1[i])
    ans2 += int(cal2[i])

if ans1 == ans2:
    print("LUCKY")
else:
    print("READY")


## 럭키 스트레이트(2회독)

n = input()
mid = len(n)//2

score_a,score_b = n[:mid],n[mid:]
a,b = 0,0

for i in range(mid):
    a += int(score_a[i])
    b += int(score_b[i])

if a == b:
    print("LUCKY")
else:
    print("READY")