## 1712

# A: 고정비용, B: 가변비용(한 대 당) / C: 책정한 노트북 가격 비용
# 손익분기점: C*(판매량) > A+B*(판매량) 이 되는 지점

import sys

a,b,c = map(int, sys.stdin.readline().split())

i = 0                   # 판매하는 노트북 수
while 1:
    if b>=c:            # B가 C보다 크면 손익분기점이 존재하지 않는다.
        print(-1)
        break
    elif c*i > a+b*i:   # 커지는 지점에서 i를 출력해준다.
        print(i)
        break
    else:
        i += 1

## 반복문에 돌린 결과 시간초과. 따라서 식을 쓰기로 함.

import sys

a,b,c = map(int, sys.stdin.readline().split())

# 손익분기점이 있는 경우와 없는 경우로 나눠 바로 조건문으로 들어간다.

if b>=c:
    print(-1)

# c*n=a+b*n
# c*n-b*n=a
# n(c-b)=a
# n=a/(c-b)
else:
    n = a//(c-b)    # 정수여야하므로 몫을 구한다.
    # 두 값이 같은 지점을 찾았으므로 이익이 발생하기 위해선 이보다 한 대 더 있어야하니 출력은 +1.
    print(n+1)