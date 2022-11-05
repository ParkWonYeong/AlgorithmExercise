## 개미병사

# 서로 인접한 곳 불가, 최소 한 칸 떨어진 식량창고를 약탈
# 식량창고 N개에 대한 정보가 주어질 때 얻을 수 있는 식량의 최댓값

n = int(input())    # 식량창고의 개수(3<=N<=100)
eat = list(map(int, input().split()))     # 각 식량창고에 저장된 식량 개수(0<=K<=1000)

dp = [0]*100
dp[1] = max(eat[0], eat[1])

for idx in range(1, n):
    # 더 큰 값을 갱신
    
    # print('idx: ', idx)
    # print('dp[idx-1]:',dp[idx-1])
    # print('eat[idx]:', eat[idx])
    
    dp[idx] = max(dp[idx-1], dp[idx-2]+eat[idx])

print(dp[n-1])


### 개미병사(2회독)

n = int(input())    # 식량창고의 개수(3<=N<=100)
eat = list(map(int, input().split()))     # 각 식량창고에 저장된 식량 개수(0<=K<=1000)

dp = [0]*100
dp[1] = max(eat[0], eat[1])

for i in range(1, n):
    dp[i] = max(dp[i-1], dp[i-2]+eat[i])

print(dp[n-1])