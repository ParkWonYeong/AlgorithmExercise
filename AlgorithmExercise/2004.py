## 2004

# 팩토리얼을 구현해서 0의 개수를 찾으면 답은 맞겠지만 시간초과가 일어남.
# 끝자리가 0이라는 것은 10의 배수일 경우.
# 10 = 2x5 이며, 2와 5의 짝이 맞아야 10이 되므로 2 개수와 5 개수 중 더 작은 수가 10의 개수

import sys
input = sys.stdin.readline

n,m = map(int, input().split())

# 해당 숫자(i)에 들어간 숫자(target) 개수 구하기
def cnt_num(i,target):
    cnt = 0
    while i != 0:       # 더이상 나눌 target 값이 없는 경우 종료
        i //= target    # target으로 나눠서 i의 몫이 0이 아니면 개수를 +1
        cnt += i
    return cnt

# combination에서 nCm = n!/(m!(n-m)!)
cnt_5 = cnt_num(n,5) - cnt_num(m,5) - cnt_num(n-m,5)
cnt_2 = cnt_num(n,2) - cnt_num(m,2) - cnt_num(n-m,2)

ans = min(cnt_5, cnt_2)
print(ans)

# 30864KB, 72ms