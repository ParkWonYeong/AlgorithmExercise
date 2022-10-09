## 균형잡힌 세상

# while 1:
#     s = input()
#     cnt1, cnt2 = 0,0
#     check = 0
#     if s == '.':
#         break

#     for i in s:
        
#         if (cnt1<0 or cnt2<0) or (check==1 and i==']') or (check==2 and i==')'):
#             break

#         if i == '(':
#             check = 1
#             cnt1 += 1
#         elif i == '[':
#             check = 2
#             cnt2 += 1
#         elif i == ')':
#             check = 0
#             cnt1 -= 1
#         elif i == ']':
#             check = 0
#             cnt2 -= 1
        
#     if cnt1==0 and cnt2==0 and check==0:
#         print("yes")
#     else:
#         print("no")

### => 반례 ([(([])[]))] 
# 괄호의 개수와 현재 턴에 대해서만 계산했기 때문에 통과 못함
# stack을 이용하여 모든 턴에 대해 계산해야함

from collections import deque

while 1:
    s = input()
    if s == '.':
        break
    stack = deque([])
    check = 1
    
    for i in s:
        if i=='(' or i=='[':
            stack.append(i)
        elif i==')':
            if not stack or stack[-1]=='[':
                check = 0
                break
            elif stack[-1]=='(':
                stack.pop()
        elif i==']':
            if not stack or stack[-1]=='(':
                check = 0
                break
            elif stack[-1]=='[':
                stack.pop()

    if check and len(stack)==0:
        print('yes')
    else:
        print('no')