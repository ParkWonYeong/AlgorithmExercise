## 캐릭터의 좌표

def solution(keyinput, board):
    
    local = [0,0]

    for i in range(len(keyinput)):
        if keyinput[i] == "up":
            local[1] += 1
            
        elif keyinput[i] == "down":
            local[1] -= 1
            
        elif keyinput[i] == "left":
            local[0] -= 1
            
        else:
            local[0] += 1
        
        if abs(local[0]) > board[0]//2:  # x좌표 초과 체크
            if local[0] < 0:            # 음수일 경우
                local[0] += 1
            else:                       # 양수일 경우
                local[0] -= 1
    
        if abs(local[1]) > board[1]//2:  # y좌표 초과 체크
            if local[1] < 0:
                local[1] += 1
            else:
                local[1] -= 1
    
    return local