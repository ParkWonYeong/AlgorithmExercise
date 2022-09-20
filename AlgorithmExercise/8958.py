## OX 퀴즈

n = int(input())    # 테스트 케이스 개수

for i in range(n):
    quiz = input()
    score, cnt = 0,1
    for j in range(len(quiz)):
        
        if quiz[j] == 'O':
            score += cnt

        if j < (len(quiz)-1):
            if quiz[j+1] != 'O':
                cnt = 0
            else:
                cnt += 1
        else:
            cnt += 1
    print(score)