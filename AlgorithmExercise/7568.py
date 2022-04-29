## 7568

import sys

n = int(sys.stdin.readline())

student = []
ans = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    student.append((x,y))

for i in student:
    rank = 1    # 1등으로 시작해서 더 큰수를 만나면 +1씩 등수를 내린다.
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:     # 덩치가 더 큰 상대를 만난 경우
            rank += 1
    print(rank, end = ' ')

    ## 30840KB, 68ms