## 12948

def solution(phone_number):
    if len(phone_number) == 4:
        return phone_number
    else:
        answer = ''
        for i in range(len(phone_number)-4):
            answer += '*'
        for j in range(len(phone_number)-4, len(phone_number)): 
            answer += phone_number[j]

        return answer