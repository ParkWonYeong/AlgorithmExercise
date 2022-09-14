## 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    answer = -1     # 더 섭취해야 할 음식이 없으면 -1
    h = []

    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i+1))     # h 배열에 튜플의 형태로 (걸리는 시간, 음식번호) heappush

    food_num = len(food_times)  # 남은 음식 개수
    removed_food = 0

    while h:
        # 먹는 시간 = 남은양 * 음식개수
        t = (h[0][0] - removed_food) * food_num

        if k >= t:  # 방송이 중단되는 시간이 이미 다 먹은 후일때
            k -= t
            removed_food, trash = heapq.heappop(h)  # 끝난 음식 번호는 사용 안함
            food_num -= 1

        else:
            idx = k % food_num
            h.sort(key=lambda x:x[1])   # 음식 번호 순으로 정렬
            answer = h[idx][1]          # 다시 섭취를 시작할 음식 번호 갱신
            break

    return answer

print(solution([3,1,2],5))