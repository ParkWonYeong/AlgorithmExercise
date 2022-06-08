## 1316

cnt = 0

N = int(input())
for _ in range(N):
    stack = []
    word = input()
    for i in range(len(word)):
        if word[i] not in stack:
            stack.append(word[i])
        else:
            if word[i] != 0 and word[i] == word[i-1]:
                stack.append(word[i])
            else:
                break
    print(stack)
    if len(stack) == len(word):
        cnt += 1

print(cnt)

# 30840KB, 68ms