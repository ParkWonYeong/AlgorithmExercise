## 2108

# N은 홀수
# 1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

from collections import Counter

def modefinder(num):
    num_c = Counter(num).most_common()
    if len(num_c) > 1:
        if num_c[0][1] == num_c[1][1]:
            print(num_c[1][0])
        else:
            print(num_c[0][0])
    else:
        print(num_c[0][0])    

N = int(input())
num = []

for i in range(N):
    num.append(int(input()))

print(round(sum(num)/N))    # 산술평균 출력
num.sort()
print(num[N//2])            # 중앙값 출력
print(modefinder(num))      # 최빈값 출력
print(num[-1]-num[0])       # 범위 출력