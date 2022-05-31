## 12933

def solution(n):
    n = str(n)
    ans = []
    for i in n:
        print(i)
        ans.append(i)
    ans.sort(reverse = True)
    answer = ''
    for j in range(len(ans)):
        answer += ans[j]
    return int(answer)