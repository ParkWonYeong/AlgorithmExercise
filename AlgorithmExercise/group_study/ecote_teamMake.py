## 팀 결성

# n: 0번부터 N번까지 총 N+1개의 팀이 존재
# m: 입력으로 주어지는 연산의 개수

import sys
input = sys.stdin.readline

# 소속 팀이 있는지 확인
def find(team, x):

    if team[x] != x:        # 특정 팀에 속한 학생인 경우
        team[x] = find(team, team[x])   # 어느 팀인지 찾는다

    return team[x]


# 팀 합치기
def merge(team, i, j):
    # 두 학생이 어느 팀 소속인지 찾는다.
    i = find(team, i)
    j = find(team,j)

    # 더 작은 수로 팀을 합친다.
    if i>j:
        team[i] = j
    else:
        team[j] = i


#### main ####
n,m = map(int, input().split())

team = [i for i in range(n+1)]

for _ in range(m):
    x,a,b = map(int, input().split())

    # 팀 합치기 연산
    if x == 0:
        merge(team,a,b)

    # 같은 팀 여부 확인 연산
    elif x == 1:
        if find(team,a) == find(team,b):    # 같은 티
            print("YES")
        else:
            print("NO")


# 입출력 예시

# 입력
# 7 8
# 0 1 3
# 1 1 7     # 같은 팀 여부 확인
# 0 7 6
# 1 7 1     # 같은 팀 여부 확인
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1     # 같은 팀 여부 확인

# 출력
# NO
# NO
# YES

# [1,3]
# [7,6]
# [1,3,7,6]   # 3,7
# [4,2]
# [1,1]       # 같은 학생이 같은 팀에 속한다는 연산이 나올 수도 있음.