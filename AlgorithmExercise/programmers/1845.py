## 1845

def solution(nums):
    N = len(nums)
    numb = list(set(nums))  # 중복 제거
    if len(numb) >= N//2:
        return N//2
    else:
        return len(numb)