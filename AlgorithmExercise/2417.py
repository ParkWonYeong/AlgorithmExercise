## 2417
# 이분탐색을 이용해보자.

n = int(input())

start,end = 0,n

while start <= end:
    mid = (start+end) // 2      # 중간지점을 구한다
    
    if mid**2 < n:    # q^2 < n 으로 조건을 만족하지 못하는 경우
        start = mid+1   # start를 +1
    else:               # q^2 >= n 으로 조건을 만족한 경우
        end = mid-1     # end를 -1

print(start)