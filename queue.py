'''
Bank queue with inputted names:
'''

names = []
for A in range(10):
	acceptedName = input("Enter a name: ")
	names.append(acceptedName)
 
'''
Pop Names
'''

print(" ")
 
for B in range(10):
	print(names.pop(0))

