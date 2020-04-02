a = []
i = 0
while i != 5:
    if i <=2:
        b = i
        a.append(b)
    else:
        b = a[i-1] * 2
        a.append(b)
    i = i+1
print(a)        
