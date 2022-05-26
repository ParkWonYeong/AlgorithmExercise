## 42883

def solution(number, k):
    
    temp = k
    num = [number[0]]
    
    for i in number[1:]:
        while (len(num)>0 and temp>0 and i>num[-1]):
            num.pop()
            temp -= 1
        num.append(i)
        print(temp, num)
        
    if temp>0:
        num = num[:-temp]
        print(num)
    
    answer = ''.join(num)

    return answer