## 블로그

import sys
input = sys.stdin.readline

n,x = map(int, input().split())     # 블로그 시작한지 N일, 조회 할 X일

# 블로그 시작 1일차부터 N일차까지 하루 방문자 수
visitor = list(map(int, input().split()))
check = sum(visitor[:x])
max_visit = check
cnt = 1

for i in range(x,n):
    
    # 슬라이딩 윈도우
    check -= visitor[i-x]
    check += visitor[i]

    # 최댓값 찾기
    if check > max_visit:
        max_visit = check
        cnt = 1         # 최대값이 새롭게 갱신되었으면 cnt 값 1로 초기화
    
    elif check == max_visit:
        cnt += 1        # 똑같은 값이면 cnt 값 누적


# 최대 방문자 수 0이면 SAD
if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)