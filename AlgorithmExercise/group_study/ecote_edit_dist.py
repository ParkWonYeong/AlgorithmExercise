## 편집거리

# 두 개의 문자열 a,b가 주어진다.
a = input()
b = input()

# a를 편집하여 b로 만들기.

# 삽입(insert): 특정 위치에 문자 삽입
# 삭제(remove): 특정 위치에 문자 삭제
# 교체(Replace): 특정 위치에 문자 다른 문자로 교체


# 가로 문자열 b 길이, 세로 문자열 a 길이+1 (인덱스 0 포함)
dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    dp[i][0] = i

for j in range(1, len(b)+1):
    dp[0][j] = j

for k in range(1, len(a)+1):
    for l in range(1, len(b)+1):

        # 같으면 차를 0으로
        if a[k-1] == b[l-1]:
            dp[k][l] = dp[k-1][l-1]

        # 다르면 편집 최솟값에 +1(index값을 구하기 위해)
        else:
            dp[k][l] = min(dp[k-1][l-1], dp[k-1][l], dp[k][l-1]) + 1


print(dp[len(a)][len(b)])
