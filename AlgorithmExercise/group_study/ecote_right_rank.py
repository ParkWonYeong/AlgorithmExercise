## 정확한 순위

import sys
input = sys.stdin.readline

INF = int(1e9)
# N명의 학생에 대해 두 학생끼리의 성적을 M번 비교한다.
n,m = int(input().split())

rank = [[INF]*(n+1) for _ in range(n+1)]
# 각 간선 정보받기
for _ in range(m):
    low_score, high_score = int(input().split())
    rank[low_score][high_score] = n             # 꼴찌로 만들어놓고 값 갱신하기

## 플로이드 워셜 알고리즘 ##
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            rank[i][j] = min(rank[i][j], rank[i][k] + rank[k][j])

# Count Right Rank person

