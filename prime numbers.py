"""
var=100
prime=''
for n in range(2, var+1,1):
    flag='y'
    #print("n=",n)
    for x in range(2, n+1, 1):
        #print(" x=",x)
        if n % x == 0 and n != x:
            flag='n'
            break
    #print(">>flag=",flag)
    if flag == 'y':
        prime=prime+str(n)+', '
    
print("primes=",prime[:-2])
"""

"""another method           
from math import sqrt

def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(sqrt(x)) + 1):
		if x % i ==0:
			return False
	return True
"""


      

