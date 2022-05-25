## 12973

def solution(s):
    stack = [0]     # stack에는 0만 존재.
    for i in s:
        if i == stack[-1]:  # 앞의 문자와 비교했을때 같은 문자인 경우
            stack.pop(-1)   # stack에서 빼준다.
        else:               # 앞의 문자와 같지 않으면
            stack.append(i) # stack에 쌓는다.
            
    if len(stack) == 1:     # 처음처럼 0만 존재할 경우
        return 1
    else:
        return 0