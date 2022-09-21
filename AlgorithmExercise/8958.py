## OX 퀴즈

n = int(input())    # 테스트 케이스 개수

for i in range(n):

    quiz = input()
    score, cnt = 0,0

    for j in range(len(quiz)):

        if quiz[j] == 'O':
            cnt += 1
            score += cnt

        else:
            cnt = 0

    print(score)