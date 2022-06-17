## 42862

def solution(n, lost, reserve):

    student = []
    for i in range(n):
        student.append(i+1)
        
    # 여벌 도난 중복 제거
    for i in student:
        if (i in lost) and (i in reserve):   # 여벌 체육복 보유한 학생의 체육복이 도난 됐을 시
            lost.remove(i)
            reserve.remove(i)

    for j in student:
        if j in lost:   # 도난 당한 학생인 경우
            # 앞번에 빌려줄 학생이 있는지 확인
            if j-1 in reserve:
                lost.remove(j)
                reserve.remove(j-1)
            # 뒷번에 빌려줄 학생이 있는지 확인
            elif j+1 in reserve:
                lost.remove(j)
                reserve.remove(j+1)
    answer = n-len(lost)
    return answer