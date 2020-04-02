a = input("Enter word: ")

##c = ('a', 'e', 'i', 'o', 'u')
##d={}
##s=0
##for i in c:
##    j= a.count(i)
##    s+=j
##    d[i]=j
##print (s)
##print(d)

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
if 'a' in b:
    i = a.count('a')
    i1 += i
elif 'e' in b:
    ii = a.count('e')
    i2 += ii
elif 'i' in b:
    iii = a.count('i')
    i3 += iii
elif 'o' in b:
    iiii = a.count('o')
    i4 += iiii
elif 'u' in b:
    iiiii = a.count('u')
    i5 += iiiii

print (i1 + i2 + i3 + i4 + i5)
