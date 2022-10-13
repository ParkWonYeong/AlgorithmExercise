## 가장 긴 팰린드롬

# 팰린드롬 체크
def check_palindrome(s):

    if len(s) % 2 == 0:  # 문자열 길이 짝수
        for i in range(len(s)//2-1):
            if s[i] != s[-1-i]:
                return False

    else:
        for i in range(0, len(s)//2):
            if s[i] != s[-1-i]:
                return False
    return True

# 이진탐색
def binary_search(s, start, end):
    global ans

    while start < end:
        mid = (start+end)//2
        check_s = s[start:end]

        if check_palindrome(check_s) == True:
            ans = max(len(check_s), ans)

        if len(check_s) > ans:
            binary_search(s, mid, end)
            binary_search(s, start, mid)

        return ans

def solution(s):
    global ans
    ans = 1
    return binary_search(s, 0, len(s)+1)