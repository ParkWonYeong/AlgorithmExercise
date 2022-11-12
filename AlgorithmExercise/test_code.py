from collections import deque

###### 조합 ######

M = 3
some_list = [1,2,3,4]

def dfs(comb: deque, depth: int):

    if len(comb) ==M:
        print('end')
        return

    elif depth == len(some_list):
        return

    comb.append(some_list[depth])
    print('(append)check comb, depth:', comb, depth)
    dfs(comb, depth+1)

    comb.pop()
    print('(pop)check comb, depth:')
    dfs(comb, depth+1)

dfs(deque(), 0)


### output ###
'''
(append)check comb, depth: deque([1]) 0
(append)check comb, depth: deque([1, 2]) 1
(append)check comb, depth: deque([1, 2, 3]) 2
end
(pop)check comb, depth:
(append)check comb, depth: deque([1, 2, 4]) 3
end
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([1, 3]) 2
(append)check comb, depth: deque([1, 3, 4]) 3
end
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([1, 4]) 3
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([2]) 1
(append)check comb, depth: deque([2, 3]) 2
(append)check comb, depth: deque([2, 3, 4]) 3
end
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([2, 4]) 3
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([3]) 2
(append)check comb, depth: deque([3, 4]) 3
(pop)check comb, depth:
(pop)check comb, depth:
(append)check comb, depth: deque([4]) 3
(pop)check comb, depth:

'''


###### 순열 ######

visited = [False] * len(some_list)
result = []

def dfs(perm: deque):
    if len(perm) == M:
        result.append(list(perm))
        print('end')
        return

    for i,val in enumerate(some_list):
        if visited[i]:
            continue
        perm.append(val)
        visited[i] = True
        print('(append)perm',perm)
        dfs(perm)

        perm.pop()
        print('(pop)perm', perm)
        visited[i] = False

dfs(deque())

### output ###
'''
(append)perm deque([1])
(append)perm deque([1, 2])
(append)perm deque([1, 2, 3])
end
(pop)perm deque([1, 2])
(append)perm deque([1, 2, 4])
end
(pop)perm deque([1, 2])
(pop)perm deque([1])
(append)perm deque([1, 3])
(append)perm deque([1, 3, 2])
end
(pop)perm deque([1, 3])
(append)perm deque([1, 3, 4])
end
(pop)perm deque([1, 3])
(pop)perm deque([1])
(append)perm deque([1, 4])
(append)perm deque([1, 4, 2])
end
(pop)perm deque([1, 4])
(append)perm deque([1, 4, 3])
end
(pop)perm deque([1, 4])
(pop)perm deque([1])
(pop)perm deque([])
(append)perm deque([2])
(append)perm deque([2, 1])
(append)perm deque([2, 1, 3])
end
(pop)perm deque([2, 1])
(append)perm deque([2, 1, 4])
end
(pop)perm deque([2, 1])
(pop)perm deque([2])
(append)perm deque([2, 3])
(append)perm deque([2, 3, 1])
end
(pop)perm deque([2, 3])
(append)perm deque([2, 3, 4])
end
(pop)perm deque([2, 3])
(pop)perm deque([2])
(append)perm deque([2, 4])
(append)perm deque([2, 4, 1])
end
(pop)perm deque([2, 4])
(append)perm deque([2, 4, 3])
end
(pop)perm deque([2, 4])
(pop)perm deque([2])
(pop)perm deque([])
(append)perm deque([3])
(append)perm deque([3, 1])
(append)perm deque([3, 1, 2])
end
(pop)perm deque([3, 1])
(append)perm deque([3, 1, 4])
end
(pop)perm deque([3, 1])
(pop)perm deque([3])
(append)perm deque([3, 2])
(append)perm deque([3, 2, 1])
end
(pop)perm deque([3, 2])
(append)perm deque([3, 2, 4])
end
(pop)perm deque([3, 2])
(pop)perm deque([3])
(append)perm deque([3, 4])
(append)perm deque([3, 4, 1])
end
(pop)perm deque([3, 4])
(append)perm deque([3, 4, 2])
end
(pop)perm deque([3, 4])
(pop)perm deque([3])
(pop)perm deque([])
(append)perm deque([4])
(append)perm deque([4, 1])
(append)perm deque([4, 1, 2])
end
(pop)perm deque([4, 1])
(append)perm deque([4, 1, 3])
end
(pop)perm deque([4, 1])
(pop)perm deque([4])
(append)perm deque([4, 2])
(append)perm deque([4, 2, 1])
end
(pop)perm deque([4, 2])
(append)perm deque([4, 2, 3])
end
(pop)perm deque([4, 2])
(pop)perm deque([4])
(append)perm deque([4, 3])
(append)perm deque([4, 3, 1])
end
(pop)perm deque([4, 3])
(append)perm deque([4, 3, 2])
end
(pop)perm deque([4, 3])
(pop)perm deque([4])
(pop)perm deque([])

'''


### 소용돌이 ###

N = 5
board = [[0]*N for _ in range(N)]

# 서,남,동,북
# dx = [0,1,0,-1]
# dy = [-1,0,1,0]

# 동,남,서,북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def check_grid():
    x = y = int(N/2)   # 배열의 중앙 좌표
    direction, move_cnt, num = 0,0,0,
    dist = 1

    while True:
        move_cnt += 1       # 움직인 횟수
        
        for _ in range(dist):   # dist만큼 direction 방향으로 이동
            nx = x+dx[direction]
            ny = y+dy[direction]
            print(nx,ny)

            # 종료 조건: 이동 좌표가 (0,-1)인 경우(배열의 길이가 홀수면 마지막 좌표는 (0,-1)이고 방향 서쪽)
            if nx == 0 and ny == N:
                return

            # 각 칸의 번호 및 증가 기록
            num += 1
            board[nx][ny] = num
            x,y = nx, ny

        if move_cnt == 2:   # 한 방향으로 2번 이동한 경우
            dist += 1   # 이동거리 1 증가
            move_cnt = 0    # 초기화
        direction = (direction+1) % 4     # 방향 변경

check_grid()

for row in board:
    print(row)