## 구명보트

from collections import deque

def solution(people, limit):

    boat = 0
    people.sort()       # 오름차순 정렬
    q = deque(people)

    while q:

        person = q.popleft()
        boat += 1

        # q에 남은 사람이 있으면 계속
        if len(q) != 0:

            for i in range(len(q)):
                sit_b = q.pop()

                if person + sit_b <= limit:     # 2인 탑승이 가능한 경우
                    break
                else:       # append하면 오른쪽에 가서 동일한 과정이 또 반복된다
                    q.appendleft(sit_b)

    return boat

print(solution([70, 50, 80, 50, 10, 90], 100))

# 테스트 정확도는 맞지만 효율성에서 모두 시간초과.
# deque로 pop, append 하는 대신 이진탐색?