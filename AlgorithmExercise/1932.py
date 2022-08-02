## 1932
## 정수삼각형

# 위층부터 시작해서 아래 있는 수(대각선 왼쪽 또는 오른쪽)

import sys
input = sys.stdin.readline

n = int(input())        # 1<=n<=500

# 자기자신 인덱스 또는 -1번째 인덱스와 합할 수 있다.
triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))

# 위에서부터 차례로 더해내려간다.
for i in range(1, n):

    for j in range(len(triangle[i])):
        
        # 왼쪽 끝인 경우 본인 인덱스만 더할 수 있다.
        if j == 0:
            triangle[i][j] += triangle[i-1][j]

        # 오른쪽 끝인 경우 +1 인덱스만 더할 수 있다.
        elif j == len(triangle[i])-1:
            triangle[i][j] += triangle[i-1][j-1]

        else:
            triangle[i][j] = max(triangle[i-1][j-1]+triangle[i][j] , triangle[i-1][j]+triangle[i][j])
 
print(max(triangle[-1]))


### IDEA: 더해내려가는 방식(탑다운)

# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15
# 2 7 4 4
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15
# 20 25 20 19
# 4 5 2 6 5

# 7
# 10 15
# 18 16 15
# 20 25 20 20
# 24 30 27 26 24

# max(마지막 줄) = 30