## 모험가 길드

# 모험가 N명이 공포도 측정
# 공포도가 높을수록 위기 대처능력 저하
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성된 그룹 참여
# 여행을 떠날 수 있는 그룹의 값은?

# max를 이용해서 그만큼 빼고 팀을 나눈다

from collections import deque

n = int(input())
scared = deque(map(int, input().split()))
team = 0        # 팀의 개수

while scared:

    if max(scared) >= len(scared):  # 한팀으로 될 경우
        team += 1
        break
    else:   # 공포도 최대값 < 인원수
        x = max(scared)
        team += 1
        for i in range(x):
            scared.popleft()

print(team)