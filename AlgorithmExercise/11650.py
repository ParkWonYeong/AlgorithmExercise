## 11650

import sys
input=sys.stdin.readline

N=int(input())  # 점의 개수 N
dot=[]
for _ in range(N):
    dot.append(list(map(int, input().split())))

# lambda를 이용해 오름차순 중에서도 우선순위(x 다음 y)를 정해준다.
dot.sort(key=lambda x: (x[0], x[1]))

for i in range(N):
    print(dot[i][0], dot[i][1])

# 이와같은 코드로는 57780KB의 메모리와 416ms의 시간이 소요되었다.
# 위의 print 반복문을 아래와같이 쓸 수도 있다.(480ms로 조금 더 오래걸림)
for i in dot:
    print(i[0],i[1])