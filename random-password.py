small = []
big = [] 
numbers = [] 
special = []

smallletters = 'abcdefghijklmnopqrstuvwxyz'
bigletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
digits = '0123456789' 
special_char = '~`!@#$%&*()-=_+{}[]|:;"\',.<>/'

for i in smallletters:
	small.append(i)
for i in bigletters: 
	big.append(i) 
for i in digits: 
	numbers.append(i) 
for i in special_char: 
	special.append(i)

the_big_list = small+big+numbers+special

length = int(input("How many characters long password do you want? "))

if not length or length < 0:
	exit()

import random
password = ''

if length < 4:
	while True:
		password+=small[random.randint(0,len(small)-1)]
		length-=1
		if not length:
			break
		password+=big[random.randint(0,len(big)-1)]
		length-=1
		if not length:
			break
		password+=numbers[random.randint(0,len(numbers)-1)]
		length-=1
		if not length:
			break
		password+=special[random.randint(0,len(special)-1)]
		length-=1
		if not length:
			break	

	print(password)

elif length >=4:
	from_each_list = length//4
	remaining = length%4
	for i in range(0,from_each_list):
		password+=small[random.randint(0,len(small)-1)]
		password+=big[random.randint(0,len(big)-1)]
		password+=numbers[random.randint(0,len(numbers)-1)]
		password+=special[random.randint(0,len(special)-1)]

	if remaining and from_each_list:
		for i in range(0,remaining+1):
			password+=the_big_list[random.randint(0,len(the_big_list)-1)]

	print(password)