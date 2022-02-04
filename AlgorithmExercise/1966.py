## 1966

# 1. 현재 Queue 의 가장 앞에 있는 문서의 '중요도' 확인
# 2. 나머지 문서 중 현재 문서보다 중요도가 높은 것이 있으면,
#    현재 문서를 Queue의 가장 뒤에 재배치한다. 그렇지않다면 바로 인쇄한다.

from collections import deque
import sys
input = sys.stdin.readline

num = int(input())    # 테스트케이스의 수 case

for _ in range(num):
    # N: 문서의 개수
    # M: 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇번째인지
    N, M = map(int, input().split())
    imp = deque(list(map(int, input().split())))   # 중요도
    imp_ = [0 for i in range(N)]    # 위치를 저장할 리스트
    imp_[M] = 1                     # 궁금한 문서의 위치를 1로 저장한다
    count = 0
    while True:
        if imp[0] == max(imp):  # 중요도가 가장 높은 값을 찾는다.
            count += 1          # max값이면 1을 더해준다.
            if imp_[0] == 1:    # max값 = 궁금한 문서이면
                print(count)    # 바로 count값을 출력하고 끝낸다.
                break
            else:               # max값이 궁금한 문서가 아니라면
                imp.popleft()   # 그 요소를 삭제하고 앞으로 한칸씩 당긴다.
                imp_.pop(0)

        else:   # 그렇지 않을 경우맨 맨앞의 값을 맨 뒤에로 보낸다.
            imp.append(imp.popleft())
            imp_.append(imp_.pop(0))

# 32360KB, 100ms
