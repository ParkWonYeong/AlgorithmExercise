## 1978

# 소수: 1과 자기자신으로만 나누어 떨어지는 숫자.

n = int(input())    # 수의 개수 N
numbers = map(int, input().split())

cnt = 0
for i in numbers:
    error = 0
    if i > 1:
        for j in range(2,i):    # 2부터 i-1번째 숫자까지 나눈다.
            if i % j == 0:
                error += 1      # 나눈 몫이 0이 되는 숫자가 있으면 +1
        if error == 0:
            cnt += 1            # 소수인 경우 +1씩 카운트한다.

print(cnt)

# 30840KB, 76ms