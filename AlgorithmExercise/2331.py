## 2331

def seq(num,sq):
    D = [num]
  
    while 1:
      
        number = 0
        for s in str(D[-1]):
            number += int(s)**sq

        if number in D:
            while (D[-1] != number):
                D.pop()
            D.pop()
            break

        else:
            D.append(number)
    return len(D)

A,P = map(int, input().split())
print(seq(A,P))

# 30840KB, 68ms