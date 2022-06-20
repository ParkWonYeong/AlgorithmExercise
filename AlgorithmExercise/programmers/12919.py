## 12919

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = str(i)
            answer = "김서방은 "+num+"에 있다"
            return answer