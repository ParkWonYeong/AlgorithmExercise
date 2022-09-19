## 평균

# 점수 중 최댓값 M을 고르고, 모든 점수를 (점수)/M*100으로 고친다.
# 모든 성적을 위의 방법대로 새롭게 계산했을 때 새로운 평균을 구하면?

n = int(input())    # 시험 본 과목의 개수 N
score_sum = 0
score = list(map(int, input().split()))

m = max(score)

for x in score:
    score_sum += x/m*100

print(score_sum/n)