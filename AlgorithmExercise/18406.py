## 럭키 스트레이트

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