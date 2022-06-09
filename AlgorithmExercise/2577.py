## 2577

a = int(input())
b = int(input())
c = int(input())

m = str(a*b*c)
print(m)

cnt = [0]*10
for i in range(len(m)):
    if m[i] == '0':
        cnt[0] += 1
    elif m[i] == '1':
        cnt[1] += 1
    elif m[i] == '2':
        cnt[2] += 1
    elif m[i] == '3':
        cnt[3] += 1
    elif m[i] == '4':
        cnt[4] += 1
    elif m[i] == '5':
        cnt[5] += 1
    elif m[i] == '6':
        cnt[6] += 1
    elif m[i] == '7':
        cnt[7] += 1
    elif m[i] == '8':
        cnt[8] += 1
    elif m[i] == '9':
        cnt[9] += 1

for i in cnt:
    print(i)

# 30840KB, 68ms