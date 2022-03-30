## 2720
# q = 25 cent, d = 10 cent, n = 5 cent, p = 1 cent

import sys
t = int(sys.stdin.readline())   # 테스트 케이스의 개수

cnt = [0]*4
coin = [25, 10, 5, 1]
for i in range(t):
    c = int(sys.stdin.readline())
    for j in range(4):
        cnt[j] = c//coin[j]     # 큰값부터 나누어 몫을 카운트에 저장
        c -= cnt[j]*coin[j]     # 남은 change
    print(cnt[0], cnt[1], cnt[2], cnt[3])

# 5585, 10162번과 유사
# 30860KB, 68ms