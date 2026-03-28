if __name__ == '__main__':
	N = int(input())
	list1=[]
	counter=0
	
	while counter < N:
		x=input().split()
		if len(x) == 3: #insert
			eval("list1." + x[0] + "(" + "int(" + x[1] + ")," + x[2] + ")")
		elif len(x) == 2: # remove, append
			eval("list1." + x[0] + "(" + x[1] + ")")
		elif x[0] == "print":
			eval('print(list1)')
		else: #sort, pop, reverse
			eval("list1." + x[0] + "(" + ")")
				
		counter += 1	