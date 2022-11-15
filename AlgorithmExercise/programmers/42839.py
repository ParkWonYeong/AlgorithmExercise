from itertools import permutations

def solution(numbers):
    arr = set()
    cnt = 0
    
    for i in range(1, len(numbers)+1):
        check_list = list(permutations(numbers, i))
        for j in range(len(check_list)):
            check_num = ''
            for k in range(len(check_list[j])):
                check_num += check_list[j][k]
            if int(check_num) > 1:
                arr.add(int(check_num))
            
    for l in arr:
        
        if l == 2 or l == 3:
            cnt += 1
            
        elif l >= 4:
            check_s = True
            
            for m in range(2, l):
                if l%m == 0:
                    check_s = False
                    break
                    
            if check_s:
                cnt += 1

    return cnt