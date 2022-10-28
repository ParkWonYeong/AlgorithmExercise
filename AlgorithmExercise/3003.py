## 킹, 퀸, 룩, 비숍, 나이트, 폰

import sys
input = sys.stdin.readline

# king 1, queen 1, rook 2, bishop 2, knight 2, pawn 8

ans = []
king, queen, rook, bishop, knight, pawn = map(int, input().split())

ans.append(1 - king)
ans.append(1 - queen)
ans.append(2 - rook)
ans.append(2 - bishop)
ans.append(2 - knight)
ans.append(8 - pawn)

print(*ans)