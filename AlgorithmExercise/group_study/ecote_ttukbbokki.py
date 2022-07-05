## 떡볶이 떡 만들기

import sys
input = sys.stdin.readline

# 떡의 개수 n, 요청한 떡의 길이 m
n,m = map(int, input().split())

# 떡의 개별 높이(m보다 작은 길이는 잘리지 않고, 긴 떡은 잘린다)
rice = list(map(int, input().split()))

# 요청한 총 길이가 m일 때 적어도 m만큼의 떡을 얻기 위해
# 절단기에 설정할 수 있는 "높이"의 최댓값은?
start, end = 0, max(rice)

while (start <= end):
    mid = (start+end)//2
    total = 0               # 목표치
    
    for i in rice:
        if i >= mid:
            total += i-mid  # 각각 잘린 떡의 길이 더하기

    # 위는 다음 한 줄로도 표현 가능하다.
    # total = sum(i-mid if i>=mid else 0 for i in rice)
    
    if total >= m:  # 목표치보다 높거나 같은 경우
        start = mid+1
    else:           # 목표치보다 낮은 경우
        end = mid-1

print(end)