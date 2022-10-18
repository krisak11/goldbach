# Importing math library.
import math
# Python program to get next prime number
# using sympy.nextprime() method
# python3 -m pip install sympy
# importing sympy module
# calling nextprime function on different numbers
# nextprime(7) returns 11
from sympy import *

def proofGBWrong(odd):
    ''' 
        Function checks if the parameter odd breaks GB's 1752 conjencture.

        Parameters
        -----------
        odd : int
            odd is an odd number of type int
        Returns
        -------
        bool 
            Returns False if odd number found that breaks Goldbach's rule.
    '''
    # odd = prime + 2* n^2, n>=0
    prime = 1
    n = 0 # integer n >= 0 (called a in goldbachs theorem).
    maximum_n = math.ceil(sqrt(odd/2))+1 # n <= maximum_n
    for n in range(maximum_n):
        #iterate over list of possible n's.
        prime = odd - 2*(n**2)
        if isprime(prime):
            #print(prime)
            #print(odd)
            return True # If GB's rule is not broken we return True
    return False # If GB's rule is broken we return False
# Testing proofGBWrong function
def testGB(nmax):
    print("--- Start of the search ---")
    for m in range(1,nmax):
        n = 2 * m + 1
        if proofGBWrong(n) == False:
            print("Counter-example :",n)
            break
    print("--- End of the search ---")
    return
testGB(10000)


def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
'''
#print(isprime(2))
#print(isprime(13))
#print(isprime(100))
 
# calling nextprime function on different numbers
#print(nextprime(7))
#print(nextprime(13))
#print(nextprime(2))
'''