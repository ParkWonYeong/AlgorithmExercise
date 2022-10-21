def solution(array, height):
    answer = 0
    for friend in array:
        if friend > height:
            answer += 1
    return answer