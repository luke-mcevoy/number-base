'''
Created on 10/11/18
@author:   Luke McEvoy
Pledge:    I pledge my honor I have abided by the Stevens Honor System

CS115 - Lab 6
'''
from cs115 import map, reduce

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    return True

#101010
'''
(A)if given an odd base 10 number, the least significant bit will always be 1
in base 2 representation
(B)if given an even base 10 number, the least signigicant bit will always be 0
in base 2 representation
'''
'''
when the least significant bit is cut, the original value is halfed and the
remainder is removed
'''

def numToBinary(n):
    if n==0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'



def binaryToNum(s):
    if len(s) == 0:
        return 0
    return (int(s[0]) * 2**(len(s)-1)) + binaryToNum(s[1:len(s)])
   


'''
def binaryToNums(s,x=0):
    Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    if s == 0:
        return 0
    z = len(s) - 1
    if z == 0:
        return 0
    else:
        L = [int(d) for d in str(s)]
    return [[L[z] * 2**x] + binaryToNums(s[:len(s)],x+1)]
    
def binaryToNum(s):
    if s == '':
        return 0
    #L = [int(s)]
    #print(len(s))
    L = [int(d) for d in str(s)]
    print(L)
    print(baseTwoList(len(s[0:]),0))
    return map(lambda x: x * L[0:], baseTwoList(len(s[0:]),0)) + L
    
    
    
def baseTwoList(n,x,a):
    if a < n:
        L = [baseTwoList(n, x+1, a+1)] + [2**x]
        return L
    return 0


Logic: match string (after converted) with the exponents and multiply them

Example:  1   0   1   0   1   ===>  16 + 8 + 4 + 2 + 1  ===>  31
         2^4 2^3 2^2 2^1 2^0
Tasks:
(1) Turn S from string to a list of ints
    Can be done with "int(s)"
(2) Map/match S & L to multipty as S[0]*L[0] and recurse S[1:]*L[1:]
(3) Add reduce the map/match

'''
            
def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    X = numToBinary(1 + binaryToNum(s))
    if len(X) < 8:
        return ((8-len(X))*'0' + X)
    elif len(X) > 8:
        return X[1:len(X)]
    return X

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n > -1:
        print(s)
        count(increment(s), n-1)
    return
'''
59 in ternary is 2012 because 3^3 * 2 = 54 and 59-54 = 5 \
5 can not incoportated to 3^2 but can be for 3^1 * 1 = 5-3 = 2 \
2 is subtracted by 3^0 * 2
Final answer is (3^3 * 2) + (3^2 * 0) + (3^1 * 1) + (3^0 * 2) = 2012
'''

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    elif n % 3 == 1:
        return numToTernary(n//3) + '1'
    elif n % 3 == 0:
        return numToTernary(n//3) + '0'
    elif n % 3 == 2:
        return numToTernary(n//3) + '2'

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    return (int(s[0]) * 3**(len(s)-1)) + ternaryToNum(s[1:len(s)])
