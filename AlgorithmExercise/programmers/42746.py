## 42746

def solution(numbers):
    numbers = list(map(str, numbers))

    # 네번째 자릿수부터 정렬 변화 X(0 이상 1000 이하 숫자들로 주어지기 때문)
    numbers.sort(key = lambda x:x*3, reverse = True)
    answer = str(int(''.join(numbers)))
    return answer