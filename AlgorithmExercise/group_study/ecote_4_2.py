N = int(input())    # 0 <= N <= 23

# 하나라도 3이 포함되는 경우의 수 출력

cnt = 0
for i in range(0,N+1):
    if str(i) not in '3':   # 3이 들어가지 않는 시
        cnt += 690
        # print(i, '3안들어감')
    else:                   # 3이 들어가는 시
        cnt += 3600
        # print(i, '3들어감')

print(cnt)

# 00~59까지 3이 들어가는 경우는
# 3, 13, 23, 30,31,32,33,34,35,36,37,38,39, 43, 53
# 이렇게 15가지.
# 분 단위에 3이 안들어가면 초 단위에서 15가지 경우의 수가 존재.
# 따라서 60분동안 (60-15)*15+15 = 690가지 경우의 수가 존재한다.

# 시에 3이 들어가는 경우는 초 단위로 모두 경우의 수가 추가된다.
# 1분은 60초, 60분은 3600초가 된다. 따라서 3600을 더해준다.

### 정석 코드 ###
H = int(input())

count = 0
for h in range(H+1):    # hour(H시 59분 59초까지 세어야 하므로 H+1)
    for m in range(60): # minute
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count += 1

print(count)