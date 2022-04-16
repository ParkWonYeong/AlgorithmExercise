## 11866

# queue : FIFO(선입선출)
queue = [4,5,6]
queue.append(7)
queue.pop(0)        # 첫번째로 들어온 값(4) 뺌
queue.pop(0)        # 두번째로 들어온 값(5) 뺌
# 최종 남는건 6,7

# 요세푸스: 1번부터 N번까지 N명의 사람이 앉아있고, 순서대로 K번째 사람 제거
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속한다.
# 이 과정은 N명의 사람들이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 N, K - 요세푸스 순열이라고 한다.
# 예를 들어 (7,3) 요세푸스 순열은 <3,6,2,7,5,1,4>이다.

from collections import deque

n,k = map(int, input().split())

queue = deque([])
for i in range(1, n+1):
    queue.append(i)

ans = []
answer = '<'
while queue:
    
    for i in range(k-1):
        queue.append(queue[0])
        queue.popleft()
    ans.append(queue.popleft())

answer += ', '.join(map(str, ans))
answer += '>'
print(answer)