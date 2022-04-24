## 81301

def solution(s):
    return int(
        s.replace("zero", "0")
        .replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )



## dictionary를 이용한 풀이

dic = {
    "zero":"0",
    "one":"1",
    "two":"2",
    "three":"3",
    "four":"4",
    "five":"5",
    "six":"6",
    "seven":"7",
    "eight":"8",
    "nine":"9"
}

def solution(s):
    answer = s
    
    for key, value in dic.items():
        answer = answer.replace(key, value)
        
    return int(answer)