## 정수 N개의 합을 구하는 함수 구현하기

def solve(a):
    ans = 0
    for i in a:
        ans += i
    return ans

# 혹은

def solve(a):
    return sum(a)