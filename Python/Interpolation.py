a = [4,5]
c = [2.2, 2.4]
# a.insert(1,2)
# print (a)
b = 4.5
def Interpolate(listWithKnownValue, knownValue, listWithUnknownValue):
	for i in range(len(a)):
		if b < a[0]:
			a.insert(0, b)
			c.insert(0, 0)
			# c[0] = c[i]
		elif b > a[len(a)-1]:
			a.insert(len(a), b)
			c.insert(len(a), 0)
			print(len(a))
			print(a)
		elif b < a[i+1] and b > a[i]:
			a.insert(i+1, b)
			c.insert(i+1, 0)
			c[i+1] = 0
			c[i+1] = c[i] - ((a[i]-a[i+1])*(c[i]-c[i+2]))/(a[i]-a[i+2])
			print (c[i+1])
	pass

Interpolate(a,b,c)
# print (a)
# print (c)