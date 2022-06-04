## 2108

# N은 홀수
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

from collections import Counter
import sys
input = sys.stdin.readline

def finder(num):
    num_c = Counter(num).most_common()
    if len(num_c) > 1:
        if num_c[0][1] == num_c[1][1]:
            return num_c[1][0]
        else:
            return num_c[0][0]
    else:
        return num_c[0][0] 

## main ##
N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
num.sort()

print(round(sum(num)/N))    # 산술평균 출력
print(num[N//2])            # 중앙값 출력
print(finder(num))          # 최빈값 출력
print(num[-1]-num[0])       # 범위 출력

# 52260KB, 532ms
# 함수를 쓰지 않고 바로 Counter를 사용하는 것이 더 작은 메모리로 빠르게 처리할 수 있었음.