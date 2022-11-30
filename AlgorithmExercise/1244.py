## 스위치 켜고 끄기

# 남 - 스위치 번호가 자기가 받은 수의 배수이면 그 스위치 상태 바꿈

# 여 - 받은 수와 같은 스위치 번호를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아, 그 구간에 속한 스위치 상태를 모두 바꿈.

import sys
input = sys.stdin.readline

N = int(input())    # 스위치 개수

# 각 스위치 상태
switch = list(map(int, input().split()))

for i in range(int(input())):

    g, num = map(int, input().split())  # 성별, 받은 수
    
    # 남학생일 경우
    if g == 1:
        for j in range(N):
            if (j+1) % num == 0:   # 받은 수의 배수일 경우
                if switch[j] == 1:
                    switch[j] = 0
                else:
                    switch[j] = 1
    
    # 여학생일 경우
    else:

        if switch[num-1] == 1:
            switch[num-1] = 0
        else:
            switch[num-1] = 1

        for k in range(1, N//2):

            if num-1-k < 0 or num-1+k > N-1:
                break

            if switch[num-1-k] != switch[num-1+k]:
                break

            if switch[num-1-k] == 1:
                switch[num-1-k] = 0
            else:
                switch[num-1-k] = 1

            if switch[num-1+k] == 1:
                switch[num-1+k] = 0
            else:
                switch[num-1+k] = 1


# 한 줄에 20개씩 출력
if N > 20:
    if N%20 != 0:
        for m in range(N//20+1):
            if m == N//20:
                print(*switch[m*20:])
            else:
                print(*switch[m*20:m*20+20])
    else:
        for l in range(N//20):
            print(*switch[l*20:l*20+20])

else:
    print(*switch)