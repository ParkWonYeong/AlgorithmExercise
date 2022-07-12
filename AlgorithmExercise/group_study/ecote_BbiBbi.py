## 전보

# X에서 Y로 향하는 통로는 있지만, Y에서 X로 향하는 통로가 없다면
# Y는 X로 메시지를 보낼 수 없다.
# 똫나 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

# C라는 도시에서 위급 상황이 발생하여 최대한 많은 도시로 메시지를 보낸다.
# 각 도시 번호와 통로가 설치되어 있는 정보가 주어질 때,
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 몇 개이며
# 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인가?

# 전보

import sys
input = sys.stdin.readline

# N=도시의개수 / M=통로의개수 / C=메시지를보내는도시
n,m,c = map(int, input().split())

cnt,total = 0,0

for _ in range(m):
    # x,y=x에서y로 / z=소요시간
    x,y,z = map(int, input().split())

    if x == c:      # C 도시가 보내는 통로인 경우
        cnt += 1                # 도시 개수 count
        total = max(total, z)   # 걸리는 시간(최대시간)

print(cnt, end = ' ')
print(total)