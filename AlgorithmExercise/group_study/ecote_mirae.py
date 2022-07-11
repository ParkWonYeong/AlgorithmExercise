## 미래도시

# 1번부터 N번까지의 회사. 특정 회사끼리는 서로 도로로 연결됨.
# 회사끼리 연결된 도로를 이용하여 1만큼의 시간으로 양방향으로 이동 가능.

# K번 회사에서 소개팅 -> X번 회사에서 방문판매
# 1번 회사에서 출발하여 K번 회사 방문 후 X번 회사로 이동.(최소시간)
# 만약 X번 회사에 도달할 수 없다면 -1 출력

import sys
input = sys.stdin.readline

def search_load(now_location, want_to_go, linked):

    global cnt

    for i in range(len(linked)):
        if linked[i] == now_location:    # 현 위치에서 바로 갈 수 있는 방법 탐색
            if (linked[i][1] == want_to_go):
                print('go to {} from {}'.format(want_to_go, now_location))
                cnt += 1

    if want_to_go in linked[i]:    # 1에서 바로 못 가는 경우 우회 경로 탐색
            
        if linked[i] == want_to_go:
            search_load(now_location, linked[i][1], linked)
        else:
            search_load(now_location, linked[i][0], linked)


# n: 회사 개수 / m: 경로 개수
n,m = map(int, input().split())

linked = []
for _ in range(m):
    linked.append(list(map(int, input().split())))

x,k = map(int, input().split())     # K 회사 방문 후 X 회사

global cnt
cnt = 0

# 이동 시마다 함수를 호출하여 경로를 탐색한다.

# 1 -> k
search_load(1, k, linked)

# k -> x
search_load(k, x, linked)



## answer
if cnt < 2:
    print(-1)

else:
    print(cnt)



## input 예시
# <입력 예시 1>
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5
# <출력 예시 1>
# 3

# <입력 예시 2>
# 4 2
# 1 3
# 2 4
# 3 4
# <출력 예시 2>
# -1