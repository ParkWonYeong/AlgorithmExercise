## 14226

# 이미 화면에 이모티콘 1개를 입력한 상태.
# 3가지 연산
# 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다.

# 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다.
# 화면에 이모티콘을 붙여넣기 하면, 일부가 변형되지 않은 클립보드에 있는
# 복사된 이모티콘의 개수가 화면에 추가된다.

from collections import deque
import sys
input = sys.stdin.readline

s = int(input())    # S(2<=S<=1000)가 주어진다.

emti = [[-1]*(s+1) for _ in range(s+1)] # 화면과 클립보드 둘다 작업하기 위해 2차원배열을 만들어준다.

queue = deque()
queue.append((1,0))   # 화면 이모티콘 개수, 클립보드 이모티콘 개수
emti[1][0] = 0
while queue:
    # x = 화면 이모티콘 개수 , y = 클립보드 이모티콘 개수
    x, y = queue.popleft()

    # 1번 연산: (x,y) -> (x,x)
    if emti[x][x] == -1:   # 복사하고 시작한다.
        emti[x][x] = emti[x][y] + 1     # 연산에 걸린 1초를 더한다.
        queue.append((x,x))
    
    # 2번 연산: (x,x) -> (x+y, y)
    if x+y <= s and emti[x+y][y] == -1: # 화면+복붙할 이모티콘이 s보다 작을때
        emti[x+y][y] = emti[x][y] + 1   # 연산에 걸린 1초를 더한다.
        queue.append((x+y,y))
    
    # 3번 연산: (x,x) -> (x-1,y)
    if x >= 1 and emti[x-1][y] == -1:   # 화면에 나타난 이모티콘이 1개 이상일때
        emti[x-1][y] = emti[x][y] + 1   # 연산에 걸린 1초를 더한다.
        queue.append((x-1,y))

ans = emti[s][1]
for i in range(1,s+1):
    if emti[s][i] != -1:
        ans = min(ans,emti[s][i])  # 최솟값을 찾는다.
    
print(ans)

# 53060KB, 960ms