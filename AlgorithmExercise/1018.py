### 체스판 다시 칠하기

# 8x8을 꺼내야 하니까 범위 내에서 모든 8x8을 반복문으로 추출(카피 이용)
# 그 부분을 조건에 맞게 다시 칠하기
# 다시 칠해야 하는 최소 개수니까 8x8=64, 완탐으로 칠한 수가 n이면 min(n, 64-n)
# 8x8 그래프 반복하면서 더 작은 최소 개수 나오면 갱신하기

n,m = map(int, input().split())
ans, cnt = 64, 0
chess = [list(map(str, input())) for k in range(n)]

for i in range(n-7):
    for j in range(m-7):
        # 받아온 8x8에서
        # 첫 칸이 흰색일 경우와 검은색일 경우 둘 중 작은 값을 고른다
        for k in range(i, i+8):
            for l in range(j, j+8):
                # 행과 열 인덱스 합이 짝수인 것과 홀수인 것끼리 일정한 색을 가짐
                # 합이 짝수일 때 'W'임을 가정하고, cnt와 64-cnt 중 작은 값으로 결정
                if (k+l)%2 == 0:
                    if chess[k][l] != 'W':
                        cnt += 1
                else:
                    if chess[k][l] != 'B':
                        cnt += 1
        ans = min(ans, cnt, 64-cnt)
        cnt = 0     ## 다음 그래프 계산을 위해 값 초기화

print(ans)

# 30840 KB, 100ms