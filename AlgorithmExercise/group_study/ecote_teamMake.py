## 팀 결성

# n: 0번부터 N번까지 총 N+1개의 팀이 존재
# m: 입력으로 주어지는 연산의 개수

import sys
input = sys.stdin.readline

n,m = map(int, input().split())


# 팀 합치기 연산은 '두 팀'을 합치는 연산
# 같은 팀 여부 확인 : 특정 두 학생이 같은 팀에 속하는지 확인

team_sum = []*100001

# 팀 합치기: [0, 해당 학생 속한팀, 해당 학생 속한팀]
# 같은 팀 여부 확인: [1, 해당 학생 속한팀, 해당 학생 속한 팀]
for _ in range(m):
    x,y,z = map(int, input().split())
    print(x, y, z)

    # 팀 합치기 연산
    if x == 0:
        print('x=0')
        for i in range(len(team_sum)):
            if (y in team_sum[i]) or (z in team_sum[i]):
                team_sum[i] += list(y,z)
                break
            # 새로운 학생일 경우
            else:
                team_sum[i+1] = list(y,z)
                break

    # 같은 팀 여부 확인 연산
    else:
        print('x=1')
        for j in range(len(team_sum)):
            if (y in team_sum[i]) and (z in team_sum[i]):
                print('YES')
                break
            else:
                print('NO')
                break


# 입력 예시

# 7 8

# 0 1 3
# 1 1 7     # 같은 팀 여부 확인
# 0 7 6
# 1 7 1     # 같은 팀 여부 확인
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1     # 같은 팀 여부 확인

# 출력
# NO
# NO
# YES

# [1,3]
# [7,6]
# [1,3,7,6]   # 3,7
# [4,2]
# [1,1]       # 같은 학생이 같은 팀에 속한다는 연산이 나올 수도 있음.