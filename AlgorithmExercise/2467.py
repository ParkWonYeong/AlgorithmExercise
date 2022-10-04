## 용액

n = int(input())
liquid = list(map(int, input().split()))

def binary_search(start, end):
    
    mix_liq = 1e9
    while start < end:
        
        liquid_a, liquid_b = liquid[start], liquid[end]
        cal = liquid_a + liquid_b
        
        if abs(cal) < mix_liq:
            ans1, ans2 = start, end
            mix_liq = abs(cal)
        
        if liquid_a * liquid_b > 0:           # 같은 종류의 두 용액 혼합
            cal = liquid_a - liquid_b
            if abs(cal) < mix_liq:
                ans1, ans2 = start, end
                mix_liq = abs(cal)
        
        if cal > 0:     # 양수이면서 큰 수일때
            end -= 1
        elif cal < 0:   # 음수이면서 큰 수일때
            start += 1
        else:           # 0이면 최소. 바로 종료한다.
            break

    return ans1, ans2, mix_liq

if liquid[0] >= 0:          # 주어진 용액이 전부 산성
    print(liquid[0], liquid[1])
elif liquid[-1] <= 0:        # 주어진 용액이 전부 알칼리성
    print(liquid[-2], liquid[-1])

else:
    liq_1, liq_2, mix = binary_search(0, n-1)
    print(liquid[liq_1], liquid[liq_2])



### 시간초과지만 답은 정확한 순차탐색 ###

import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
mix_liq = 1e9

for i in range(0, n-1):
    for j in range(i+1, n):
        liq_1, liq_2 = liquid[i], liquid[j]
        print(liq_1, liq_2)
        if liq_1*liq_2 != 0:
            if min(abs(liq_1+liq_2), abs(liq_1-liq_2)) < mix_liq:
                mix_liq = min(abs(liq_1+liq_2), abs(liq_1-liq_2))
                ans1, ans2 = liq_1, liq_2
        else:
            ans1, ans2 = liq_1, liq_2
            break

print(ans1, ans2)



### 아래는 정답처리되는 코드인데 왜 정답이 되는지 모르겠음.
### 테스트케이스 2부터 틀림.

import sys
input = sys.stdin.readline
 
N = int(input())
arr = list(map(int, input().split()))
 
left = 0
right = N-1
answerL = 0
answerR = 0
_min = sys.maxsize
while left < right:
    _sum = arr[left] + arr[right]
 
    if abs(_sum) < _min:
        answerL = left
        answerR = right
        _min = abs(_sum)
 
    if _sum > 0:
        right -= 1
    elif _sum < 0:
        left += 1
    else:
        break
 
print(arr[answerL], arr[answerR])