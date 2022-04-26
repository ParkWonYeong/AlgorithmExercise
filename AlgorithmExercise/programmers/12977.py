## 12977

nums = list(map(int, input().split(',')))

def solution(nums):
    answer = 0
    
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                cnt = 0
                num = nums[i]+nums[j]+nums[k]     # 3개의 수를 더한다.
                
                for l in range(2, num):     
                    if num % l == 0:            # 소수 X
                        cnt += 1

                if cnt == 0:                    # 소수 O
                    answer += 1                 # 경우의 수로 추가.

    return answer

print(solution(nums))