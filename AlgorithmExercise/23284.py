## 모든 스택 수열

from collections import deque
import sys
input = sys.stdin.readline

def recursion_func(stack: deque, num):

    print('num=',num)
    print('stack=',stack)
    print('visit=',visited)
    print('visitappend=', visited_append)

    if visited[M]:
        if len(result) == M:
            ans.append(list(result))
            print(*result)
        return

    if num<=M and not visited_append[num]:
        visited_append[num] = True
        stack.append(num)


    # pop
    if visited_append[num] and not visited[num]:
        visited[num] = True
        result.append(stack.pop())
    
    recursion_func(stack, num+1)



stack = []
result = []
ans = []
M = int(input())
visited = [False]*(M+1)
visited_append = [False]*(M+1)

recursion_func(stack, 1)



# input 3

# output
# 1 2 3     # push->pop->push->pop->push->pop
# 1 3 2     # push->pop->push->push->pop->pop
# 2 1 3     # push->push->pop->pop->push->pop
# 2 3 1     # push->push->pop->push->pop->pop
# 3 2 1     # push->push->push->pop->pop->pop

# sol1 : 재귀함수를 이용한 push, pop 반복>
# sol2 : 반복문을 이용한 push, pop 반복?