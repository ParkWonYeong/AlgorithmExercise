## 음료수 얼려먹기(bfs, dfs)

## 구멍이 0, 막혀있는 부분이 1
# 방문한 노드는 1로 정해준다. 게임개발 문제와 유사.

# 현재 정점에서 갈 수 있는 점들까지 들어가면서 탐색해야하므로 dfs 방식 사용
# dfs 방식은 재귀함수를 이용한다.

import sys
input = sys.stdin.readline

# 상하좌우 연결 가능한 '0'(구멍)이 있는지 체크.(dfs)
def dfs(x, y):
    global cnt
    if (x<0 or x>=n or y<0 or y>=m) or (ice[x][y]=='1'):  # 영역 밖이거나 방문한 곳
        return 0
    
    if ice[x][y] == '0':
        ice[x][y] = '1'           # 방문 표시
        # 상하좌우 탐색
        dfs(x,y-1)  # 상
        dfs(x,y+1)  # 하
        dfs(x-1,y)  # 좌
        dfs(x+1,y)  # 우
        return 1
    return 0


## main ##

n,m = map(int, input().split())     # n 세로, m 가로
cnt = 0                             # 음료수 채우는 횟수를 count 할 변수

# 얼음틀의 형태가 주어진다. (n x m 2차원 리스트)
ice = []
for _ in range(n):
    # int input으로 받으니 0부터 시작하는 경우 에러 발생.
    # 따라서 처음부터 string 값으로 받고, string 값으로 조건문을 건다.
    ice.append(list(map(str, input())))

for i in range(n):
    for j in range(m):
       if dfs(i,j) == 1:
        cnt += 1

print(cnt)
