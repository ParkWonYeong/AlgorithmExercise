## 42842

import math

def solution(brown, yellow):
    
    # yellow의 가로길이는 전체에서 세로 두줄 뺀 -2
    # yellow의 세로길이는 전체에서 가로 두줄 뺀 -2
    # brown은 가로 두줄, 세로 두줄에서 겹친 가장자리 4칸 뺀 값.
    
    # yellow = (x-2)*(y-2)
    # brown = 2(x+y) - 4
    # x+y = brown//2 + 2
    
    tile = brown//2 + 2
    x = math.ceil(tile/2)
    
    while x < tile:
        # x+y = brown//2+2 = tile
        y = tile - x
        check = (x-2)*(y-2)
        
        if check == yellow:
            answer = [x,y]
            break
        x += 1
        
    return answer