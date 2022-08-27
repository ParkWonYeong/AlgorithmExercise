## 42626

# heapq 모듈: 이진트리 기반의 "최소 힙" 자료구조를 제공, Java에서 PriorityQueue 클래스와 유사.

# 빈 리스트를 생성후 heapq 모듈 함수 호출때마다 이 리스트를 인자로 넘김
# heapq 모듈을 통해 원소를 추가하거나 삭제한 리스트가 최소 힙
# 힙의 원소를 추가할 때는 heappush(리스트, 원소) 함수를 이용
# 힙의 원소를 제거할 때는 heappop(리스트). 가장 작은 원소를 삭제
# 기존 리스트를 힙으로 만들고싶으면 heapify(기존리스트)를 사용

# 단, heapify() 함수의 성능은 인자로 넘기는 원소 수에 비례(시간복잡도 O(N))

# 최대 힙을 만들려면 힙에 tuple을 원소로 추가/삭제하여
# 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용한다.
# 각 값에 대한 우선순위를 구한 후, (우선순위,값) 구조의 튜플을 추가/삭제한다.
# 이후 힙에서 값을 읽어올 때는 각 튜플의 [1]에 있는 값 본다.

# 참고: https://www.daleseo.com/python-heapq/

import heapq

def solution(scoville, K):
    answer = 0
    s = []
    # s에 target을 scoville의 요소로 삽입
    for target in scoville:
        heapq.heappush(s,target)
    
    while (s[0] < K):
        try:
            a = heapq.heappop(s)
            b = heapq.heappop(s)
            heapq.heappush(s, a+b*2)
            answer += 1
        except:
            return -1
    
    return answer