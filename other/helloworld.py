#list
s = [value**2 for value in range(1,11)]
print(s)
print("the first three items:",s[0:3])
print("the middle three items:",s[ int(len(s)/2)-2 : int(len(s)/2)+1])
print("the last three items:",s[-3:])

#元祖
triple = (1,2,3,4,5)
for i in triple:
	print(i)

triple = (7,8)
for i in triple:
	print(i)

#direction
alien = {'col':'green', 'points': 5, 'weight':5, 'lenth':5 }
del alien['points']
print(alien)
for key in alien.keys():
	print(key)
for value in set(alien.values()):
	print(value)
