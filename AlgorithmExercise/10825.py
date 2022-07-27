## 10825
## 국영수

n = int(input())
chart = []
for i in range(n):
    student = list(map(str, input().split()))
    student[1] = int(student[1])
    student[2] = int(student[2])
    student[3] = int(student[3])
    chart.append(student)

chart.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for j in range(n):
    print(chart[j][0])