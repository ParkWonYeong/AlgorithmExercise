## 두 배열의 원소 교체

import sys
input = sys.stdin.readline

# N, K가 공백으로 구분되어 입력
n,k = map(int, input().split())

# 배열 A의 원소들이 공백으로 구분되어 입력
A = list(map(int, input().split()))

# 배열 B의 원소들이 공백으로 구분되어 입력
B = list(map(int, input().split()))

A.sort()                    # 오름차순
B.sort(reverse = True)      # 내림차순

# A의 원소 중 가장 작은 값을 B의 원소 중 가장 큰 값으로 바꾼다.
# B를 출력할 필요는 없으므로 temp는 생략한다.
for i in range(k):
    A[i] = B[i]

print(sum(A))