def dynFibo(n):
    
    f = [0 for _ in range(n+1)]
    f[1] = 1
    
    # Fibonacci 수열
    for i in range(2, n+1):
        f[i] = f[i-1]+f[i-2]

    return f