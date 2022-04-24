## 2747

n = int(input())

num=[0]*2
num[0],num[1] = 0,1

for i in range(2, n+1):
    num.append(num[i-1] + num[i-2])
    
print(num[n])

# 30840KB, 68ms