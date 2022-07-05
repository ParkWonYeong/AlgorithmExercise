## 부품찾기(이진탐색)

def binary_search(arr, target):
    start = 0
    end = len(arr)-1
    
    while (start <= end):
        mid = (start+end) // 2

        if arr[mid] == target:  # 답을 찾았을 경우
            return 'yes'
        elif (arr[mid] > target):   # 아직 더 큰 경우
            end = mid-1
        else:                       # 더 작은 경우
            start = mid+1

    return 'no'

import sys
input = sys.stdin.readline

# 가게 부품 개수 N
n = int(input())

# 공백으로 구분하여 N개의 부품 번호입력(1 이상 1,000,000 이하)
num = list(map(int, input().split()))
num.sort()      # 오름차순 정렬

# 손님이 요청한 부품 개수 정수 M 입력
m = int(input())

# 공백으로 구분하여 손님이 요청한 M개의 부품번호 입력(1 이상 1,000,000 이하)
want = list(map(int, input().split()))
want.sort()     # 오름차순 정렬

answer = []
# 출력: 첫째줄에 공백으로 구분하여 각 부품이 존재하면 'yes', 없으면 'no'
for i in range(len(want)):
    answer.append(binary_search(num, want[i]))

print(*answer)