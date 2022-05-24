## 67256

def solution(numbers, hand):
    
    answer = ''
    leftpad, rightpad, midpad = [1,4,7], [3,6,9], [2,5,8,0]
    left, right = 10, 12                # [*, 0, #] = [10, 11, 12]

    for i in range(len(numbers)):
        temp = numbers[i]
        if numbers[i] == 0:
            temp = 11
            
        if numbers[i] in leftpad:       # 1,4,7인 경우
            answer += 'L'
            left = temp                 # 왼손가락 위치 갱신
            
        elif numbers[i] in rightpad:    # 3,6,9인 경우
            answer += 'R'
            right = temp                # 오른손가락 위치 갱신
            
        elif numbers[i] in midpad:      # 2,5,8,0인 경우

            # 거리 구하기
            dis_r = abs(right-temp)//3 + abs(right-temp)%3
            dis_l = abs(left-temp)//3 + abs(left-temp)%3
            
            if dis_r < dis_l:
                answer += 'R'
                right = temp
            elif dis_r > dis_l:
                answer += 'L'
                left = temp
            # 엄지손가락의 거리가 같다면 오른손잡이는 오른손, 왼손잡이는 왼손 사용.
            elif dis_r == dis_l:
                if hand == "right":
                    answer += 'R'
                    right = temp
                else:
                    answer += 'L'
                    left = temp
    
    return answer