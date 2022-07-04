## 성적이 낮은순서대로 학생출력하기

import sys
input = sys.stdin.readline

n = int(input())

# 학생 이름, 성적이 공백 구분되어 입력된다.
chart = []
for i in range(n):
    chart.append(list(map(str, input().split())))
    chart[i][1] = int(chart[i][1])
# 성적이 낮은 순으로 출력하므로 chart[i][1]을 비교
chart.sort(key=lambda x: x[1])

for i in range(n):
    print(chart[i][0])