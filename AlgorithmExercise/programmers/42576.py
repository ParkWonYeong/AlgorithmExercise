## 완주하지 못한 선수

def solution(participant, completion):
    
    # 알파벳 오름차순으로 정렬해서, 같은 i번째의 두 값이 일치하지 않으면 참가명단을 출력
    participant.sort()
    completion.sort()
    # completion 길이는 participant 길이보다 1 작으므로 out of range error 방지를 위해 추가로 append
    completion.append(0)
    
    i=0
    while 1:
        if participant[i] != completion[i]:
            answer = participant[i]
            break
        else:
            i += 1
            
    return answer



### Hash Solutin ###

def solution(participant, completion):

    # Key: hash한 값, Value : 각 선수의 이름

    hashDic = {}
    sum_H = 0
    
    # Hash : Participant의 dictionary 만들기
    # Participant의 sum(hash) 구하기
    for p in participant:
        hashDic[hash(p)] = p
        sum_H += hash(p)
    
    # sum(hash)에서 완주자 빼기
    for c in completion:
        sum_H -= hash(c)
    
    # 남은 값 = 완주하지 못한 선수의 hash 값
    return hashDic[sum_H]


# print(solution(["marina", "josipa", "nikola", "vinko", "filipa"]
# , ["josipa", "filipa", "marina", "nikola"]))