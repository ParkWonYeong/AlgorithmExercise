## 정확한 순위

import sys
input = sys.stdin.readline

INF = int(1e9)
# N명의 학생에 대해 두 학생끼리의 성적을 M번 비교한다.
n,m = map(int, input().split())

rank = [[INF]*(n+1) for _ in range(n+1)]

# 본인->본인은 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            rank[a][b] = 0


# 각 간선 정보받기
for _ in range(m):
    low_score, high_score = map(int, input().split())
    rank[low_score][high_score] = n             # 꼴찌로 만들어놓고 값 갱신하기



## 플로이드 워셜 알고리즘 ##
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            rank[i][j] = min(rank[i][j], rank[i][k] + rank[k][j])


# Count Right Rank person
ans = 0
for a in range(1, n+1):
    cnt = 0
    
    for b in range(1, n+1):
        # 간선을 통해 두 학생간 양방향으로 이동이 가능하다 = 성적 비교가 가능하다
        # 성적 비교가 가능할 때마다 count +1
        if (rank[a][b] != INF) or (rank[b][a] != INF):
            cnt += 1
        
    if cnt == n:    # 통틀어 전체순위를 명확하게 알수있는 학생이면
        ans += 1    # 인원에 추가

print(ans)