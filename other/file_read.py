with open('cicrl.txt') as file_object:
	#contents = file_object.read()
	#print(contents.rstrip())

	#for line in file_object:
		#print(line.rstrip())
	
	#存贮在列表中再打印
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	print(line.rstrip())

print(pi_string)

birthday = input("what is your birthday:")
if birthday in pi_string:
	print("in")
else:
	print("not in")