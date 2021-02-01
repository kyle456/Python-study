def fibo(n):
    if n <= 1:
        return n
    return fibo(n-2) + fibo(n-1)

n = int(input())
i = 0
while(True):
    fibonacci = fibo(i)
    if fibonacci > n:
        break
    i += 1
    print(fibonacci, end=' ')
