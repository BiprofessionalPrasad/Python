from itertools import combinations as com
S=input()
NN=S.split(' ')
for k in range(1,int(NN[1]),1):
	K = (list(com(NN[0],k)))
	for i in range(1,len(K)):
		print (''.join(K[i]))