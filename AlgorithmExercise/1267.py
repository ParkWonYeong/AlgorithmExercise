## 1267
# 핸드폰 요금

# 1. 영식요금제(Y) - 30초 미만 10원씩 청구
# 2. 민식요금제(M) - 60초 미만 15원씩 청구

# 통화 시간 목록이 주어지면 어느 요금제를 사용하는 것이 저렴한지 출력
# 요금이 모두 같으면 영식 먼저 쓰고 민식 작성

n = int(input())        # N은 20보다 같거나 작은 수

# 통화시간은 10,000보다 작거나 같은 자연수
time = list(map(int, input().split()))

y_ans, m_ans = 0,0

# 각각의 요금 계산
for i in range(len(time)):      # 통화 개수만큼 반복하며 요금 계산

    # 30초 단위로 10원 할당(기본 10원으로 시작)
    y_ans += time[i] // 30 * 10 + 10

    # 60초 단위로 15원 할당(기본 15원으로 시작)
    m_ans += time[i] // 60 * 15 + 15


if y_ans < m_ans:
    print('Y', y_ans)

elif y_ans > m_ans:
    print('M', m_ans)

elif y_ans == m_ans:
    print('Y', 'M', y_ans)