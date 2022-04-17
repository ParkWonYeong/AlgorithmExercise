## 2805

# 오름차순으로 나열한 [M미터 >= 합(전체 나무 - H)] 면 종료한다.

import sys
input = sys.stdin.readline

n,m = map(int, input().split())     # n: 나무의 수, m: 원하는 나무의 총길이
tree = list(map(int, input().split()))
start, end = 1, max(tree)           # 이분탐색의 search range

while start <= end: 
  mid = (start+end)//2      # 반으로 댕강

  log = 0                   # 잘린 나무 총합
  
  for i in tree:
    if i >= mid:
      log += i-mid          # 각 잘린값 더한다.

  # 이건 위의 세 줄짜리 방식보다 빠른 방식. 코드 길이도 몇 줄 줄어들었다.
  log = sum(i-mid if i>=mid else 0 for i in tree)


  # log 값이 목표치보다 높거나 같습니까?
  if log >= m:       # Yes       
    start = mid + 1                     # start = mid+1
  else:              # No
    end = mid - 1                       # end = mid-1

print(end)