## 네번째점

dot_x, dot_y = [], []

for i in range(3):
    x,y = map(int, input().split())
    dot_x.append(x)
    dot_y.append(y)

for k in range(3):
    check_x = dot_x.count(dot_x[k])
    check_y = dot_y.count(dot_y[k])
    
    if check_x < 2:
        x = dot_x[k]
    
    if check_y < 2:
        y = dot_y[k]

print(x,y)