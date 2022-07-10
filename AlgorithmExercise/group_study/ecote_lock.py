## 자물쇠 열기

# 출처: https://school.programmers.co.kr/learn/courses/30/lessons/60059


### method 1
import sys
sys.setrecursionlimit(10**6)

# 재귀함수 방식 사용
def key_lock(x, y, rotation, key, lock):
    
    # key : 열쇠에 대한 2차원 배열정보(회전, 이동 가능)
    # lock : 자물쇠에 대한 2차원 배열정보
    
    # NxM 크기의 2차원 배열 check 생성
    hole = []
    check = [[] for _ in range(len(key[0])) for _ in range(len(key))]
    
    # 회전: 0도, 90도, 180도, 270도
    key_list = [key,
               list(map(list, zip(*reversed(key)))),
               list(map(lambda x: list(reversed(x)), reversed(key))),
               list(reversed(list(map(list, zip(*key)))))]
    
    m,n = len(key), len(lock)
    lock_extend = [[0]*3*n for _ in range(3*n)]
    
    # lock_extend: 가운데 lock 위치시키기
    for i in range(n):
        for j in range(n):
            if lock[i][j] == 0:
                lock_extend[i+n][j+n] = lock[i][j]
    
    # lock을 풀 수 있는지 판정(겹쳐보기)
    for i in range(m):
        for j in range(m):
            if lock[i][j] == 0:
                lock_extend[i+x][j+y] += key_list[rotation][i][j]
    
    # lock_extend에 속한 lock_list
    lock_list = list(map(lambda x: x[n:2*n], lock_extend[n:2*n]))

    # lock_list에 남은것이 1 뿐인 경우(lock을 풀수있으면)
    if set(sum(lock_list, [])) == {1}:
        return True
    
    else:
        # key, lock_list를 다 탐색한 경우
        if (x,y) == (2*n-1, 2*n-1):
            
            # 270도까지 회전해본 상태라면 lock을 풀수없음을 나타냄.
            if rotation == 3:
                return False
            
            else:
                x,y = 1,1
                # 재귀함수 호출
                return key_lock(x, y, rotation+1, key, lock)
            
        # key가 lock_list와 겹쳐진 마지막 열이라면 다음 행으로 이동
        elif x < 2*n-1 and y == 2*n-1:
            return key_lock(x+1, 0, rotation, key, lock)
        
        else:
            return key_lock(x, y+1, rotation, key, lock)
    
def solution(key, lock):
    answer = key_lock(1, 1, 0, key, lock)
    return answer




### method 2

def rotation(arr):
    n = len(arr)
    ret = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ret[j][n-i-1] = arr[i][j]
    
    return ret

# 자물쇠가 열리는지 check
def is_unlock(bg_size, lock, key, start_x, start_y, c_start, c_end):
    bg = [[0]*bg_size for i in range(0, bg_size)]

    # background에 key와 같은 좌표에 있는 해당 값들을 모아서 계산 진행
    for i in range(0, len(key)):
        for j in range(0, len(key)):
            bg[start_y+i][start_x+j] += key[i][j]
    
    # background에 key와 다른 좌표에 있는 값들을 모아 계산 진행
    for i in range(c_start, c_end):
        for j in range(c_start, c_end):
            bg[i][j] += lock[i - c_start][j - c_start]
            # lock + key = 1이 아니면 풀 수 없음
            if bg[i][j] != 1:
                return False
    
    return True

def solution(key, lock):
    lock_size = len(lock)
    center_start = len(key)-1   # 앞으로 만들 전체 background의 center 좌표
    center_end = center_start + lock_size
    # 한 cell씩 확인하기 위해서 7*7의 좌표 형태로 만든 background
    # background는 lock의 3배를 할 필요는 없다.
    # lock의 길이 + (key의 길이 - 1)*2로 하면 처음부터 겹치게 해서 값 비교 가능

    background_size = lock_size + (2*center_start)

    for _ in range(0,4):    # rotation
        for i in range(center_end): # start_x
            for j in range(center_end): # start_y
                if is_unlock(background_size, lock, key, i, j, center_start, center_end) is True:
                    return True
            key = rotation(key)
    
    return False

## 6, 8, 11, 14, 19, 38 오답

