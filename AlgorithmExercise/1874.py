## 1874

# stack: 자료를 넣는 입구(push), 자료를 뽑는 입구(pop)이 같아
# 제일 나중에 들어간 자료가 제일 먼저 나오는 LIFO 특성을 가지고있다.
# 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써,
# 하나의 수열을 만들 수 있다.

# 이때, 스택에 push하는 순서는 반드시 오름차순을 지킨다.
# 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들수 있는지
# 있다는 어떤 순서로 push와 pop 연산을 수행해야 하는지 알수있다.
# 이를 계산하는 프로그램을 작성하라.

# 문제에서 pop한 숫자가 제시된 숫자의 순서와 같으면 된다.
# 오름차순으로 push한다는 의미는,
# 8이라는 숫자를 줬을경우 1,2,3,4,5,6,7,8까지 push한 뒤
# 8을 pop하여 꺼내는 것이다. 그리고 다음 숫자를 받아 반복한다.

# 파이썬에서는 push에 해당하는 함수 append,
# pop은 그대로 pop으로, push와 poㅔ 함수를 내장하고 있다.
# pop()에 인자를 지정하지 않으면 스택처럼 가장 마지막에 들어온 인자를 꺼낸다.
# 따라서 첫번째 인자를 꺼내고싶으면 pop(0)으로 지정해주면 된다.

import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack = []
ans = []
NO = 0

for _ in range(n):
    num = int(input())  # 제시될 숫자값
    while count <= num:     # num값이 될 때까지
        stack.append(count) # 오름차순으로 push해준다.
        ans.append('+')
        count += 1
    
    if stack[-1] == num:    # stack에 push된 마지막 값이 num와 같다면
        stack.pop()         # pop한다.
        ans.append('-')
    else:           # stack의 TOP의 입력한 수가 아니면 스택만큼 append를 못한다.
        NO = 1
        break

if NO == 1:
    print("NO") # 불가능한 경우이므로 NO를 출력한다.

else:
    print("\n".join(ans))

# 33228KB, 156ms