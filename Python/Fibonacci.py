def fibonacci (n):
    if n == 1:
        return 1
    else:
        return n + fibonacci(n-1)
print(fibonacci(88))

def fiblist(i):
    for z in range(1, i):
        print (fibonacci(z))
    return fibonacci(i)

print (fiblist(25))
