N=input()
NN=N.split(' ')
from itertools import permutations as per
K = (list(per(NN[0],int(NN[1]))))
K.sort()
for i in range(len(K)):
    print (''.join(K[i]))