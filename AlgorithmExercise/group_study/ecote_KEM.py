## 국영수

import sys
input = sys.stdin.readline

score = []
n = int(input())     # 반 학생 수
for i in range(n):
    score.append(list(map(str, input().split())))
    # 이룸, 국, 영, 수
    
# 우선순위 1: 국어점수 감소하는 순서(내림차순)
# 우선순위 2: 영어점수 증가하는 순사(오름차순)
# 우선순위 3: 수학점수 감소하는 순서(내림차순)
# 우선순위 4: 이름이 사전순으로 증가하는 순서(오름차순)
score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in range(n):
    print(score[j][0])