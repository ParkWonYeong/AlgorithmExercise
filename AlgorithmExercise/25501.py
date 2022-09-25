## 재귀의 귀재

global cnt
cnt = 1

def recursion(s, l, r):
    
    global cnt

    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    
    else:
        cnt += 1
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

### main ###
n = int(input())

for i in range(n):
    s = input()
    print(isPalindrome(s), cnt)
    cnt = 1     # 초기값 반환