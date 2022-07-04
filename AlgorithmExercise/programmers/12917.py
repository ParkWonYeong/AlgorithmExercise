## 12917

def solution(s):
    s = list(s)
    s1, s2 = [],[]
    answer = ''
    while s:
        if ord(s[-1]) >= 65 or ord(s[-1]) <= 90:
            s2 += s[-1]
            s.pop()
        else:
            s1 += s[-1]
            s.pop()
    s1.sort(reverse = True)
    s2.sort(reverse = True)
    s = s1+s2

    for i in range(len(s)):
        answer += s[i]
    return answer