## 외벽점검

import math
import itertools    # 순열을 위해서.

def solution(n, weak, dist):
    weakSize = len(weak)
    # 외벽 지점 0으로 돌아왔을때 공간의 길이를 더해서 계산을 용이하게한다.
    # ex) 외벽 길이가 12일때 10->1로 가는경우 3이 되도록 1을 13으로(+12)
    weak += [w + n for w in weak]
    ans = math.inf
    for start in range(weakSize):
        # 모든 지점에서 시작해보는 완전탐색을 한다.
        # dist에 대한 모든 순열을 다 만든다.(permutations 함수 이용)
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1         # 시작지점 1부터 확인한다.
            pos = start
            # 친구를 한명씩 쓰며 모든 취약지점이 방문되는지 확인
            for i in range(1, weakSize):
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]    # 다음지점까지 거리
                # 첫번째 친구(0번째 방)부터 방문 확인
                if diff > d[cnt-1]: # 모든 곳 미도달시
                    cnt += 1        # 친구 추가
                    pos = nextPos   # 그다음번째 친구가 시작할 위치
                    # 친구가 부족한 경우
                    if cnt > len(dist):
                        break
        
            if cnt <= len(dist):
                ans = min(ans, cnt)

    if ans == math.inf:     # 초기값이면(답을 못찾았으면)
        return -1
    
    return ans