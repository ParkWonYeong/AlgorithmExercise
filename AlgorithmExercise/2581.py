## 2581

#### 앞에서 풀었던 문제 ####
# 1978의 풀이.
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

# 2581: 1978의 변형문제
# 자연수 M과 N이 주어졌을 때 M 이상 N 이하의 소수인 것들을 모두 찾아서
# 이들 소수의 합, 최솟값을 한줄씩 출력

m = int(input())
n = int(input())
num = []
sum = 0
for i in range(m, n+1):         # m에서 n까지
    error = 0
    if i > 1:
        for j in range(2,i):
            if i % j == 0:
                error += 1
        if error == 0:
            num.append(i)
            sum += i
num.sort()

if sum == 0:
    print(-1)
else:
    print(sum)
    print(num[0])

# 30840KB, 4620ms