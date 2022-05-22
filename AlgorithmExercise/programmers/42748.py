## 42748

def solution(array, commands):
    answer = []
    i = 0
    while 1:
        try:
            arr = array[(commands[i][0]-1):(commands[i][1])]
            arr.sort()
            answer.append(arr[commands[i][2]-1])
            i += 1
        except:
            return answer