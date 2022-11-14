## 컨베이어 벨트 위의 로봇

from copy import deepcopy

N,K = map(int, input().split())
robots = []     # 로봇 위치 정보
belts = list(map(int, input().split()))
is_robot = [False for _ in range(len(belts))]   # 해당 index 위에 로봇이 있는지 없는지

# 로봇 회전
def rotate():
    global belts, is_robot, robots  # 컨베이어 벨트 및 벨트 위 로봇 회전
    
    # 벨트 회전
    n = belts.pop()
    belts.insert(1, n)
 
    # 로봇 회전
    new_robot = [] # 회전 후의 로봇 저장
    is_robot = [False for _ in range(len(belts))] # 로봇 존재 여부 초기화
    
    for belt_index in robots:
        next_belt_index = belt_index + 1 # 다음 칸으로 이동
        if next_belt_index < N: # 다음 칸이 N이하인 경우 새 로봇 배열에 추가 -> 다음 칸이 N인 경우 제외(내린것으로 판단)
            new_robot.append(next_belt_index)
            is_robot[next_belt_index] = True
        # index 값이 N이 되면 내리는 위치에 도착했으므로 회전 후 로봇 배열에 미포함

    robots = deepcopy(new_robot) # 기존 로봇 배열과 교환

# 로봇 이동
def move_robots():
    global is_robot, robots, belts

    new_robots = [] # 새로운 로봇 배열

    for belt_index in robots:
        next_index = belt_index + 1 # 다음 로봇 위치
        if is_robot[next_index] or belts[next_index] < 1: # 이동이 불가능한 경우(로봇이 있거나 내구도 1미만)
            new_robots.append(belt_index)
        else: # 이동이 가능한 경우
            belts[next_index] -= 1 # 다음 위치의 벨트 내구도 1 감소
            is_robot[belt_index] = False # 현재 위치에 로봇이 존재하지 않게됨
            if next_index != N: # 다음 위치가 N이 아닌경우에만(중요)
                new_robots.append(next_index) # 새로운 로봇 배열에 추가
                is_robot[next_index] = True
    
    robots = deepcopy(new_robots)

# 로봇 삽입
def insert_robot():
    global is_robot, robots
    if belts[1] != 0: # 1번째 벨트의 내구도가 0이 아닌경우
        robots.append(1) # 새로운 로봇 위치(1번째) 추가
        # 내구도 감소 및 로봇 존재 여부 기록
        belts[1] -= 1
        is_robot[1] = True

# 종료조건 확인
def is_finish():
    # 0의 개수가 K개 이상이 경우 True 아닌 경우 False 반환
    return belts.count(0) >= K

count = 0
while not is_finish():
    count += 1
    # 회전
    rotate()
    # 이동
    move_robots()
    # 삽입
    insert_robot()

print(count)