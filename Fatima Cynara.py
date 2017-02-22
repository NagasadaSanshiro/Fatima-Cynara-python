'''
Created on Oct 11, 2015

@author: Zhongyi Yan
'''

import math
import os

def CalPrice( p, a, b, c, d, k ):
    priceArray = []
    for i in range(1, k+1):
        tmp1 = math.sin( a * i + b )
        tmp2 = math.cos( c * i + d )
        priceArray.append(p * ( tmp1 + tmp2 + 2 )) 
        #print("Scheibe!")
    return priceArray

def MaxDec( p ): 
    maxDec = 0
    maxVal = 0
    for i in range( len(p) ):
        maxDec = max( maxDec, maxVal - p[i] )
        maxVal = max( maxVal, p[i] )
        
    return maxDec

if os.path.exists('input.dat'):
    fileIn = open( 'input.dat' , 'r' )
    fileOut = open( 'output.dat', 'w+' )
    for line in fileIn:
        constantP,constantA,constantB,constantC,constantD,valK = map(int, line.split(' '))
        done = True
        if constantP < 1 or constantP > 1000:
            done = False
        if constantA < 0 or constantA > 1000:
            done = False
        if constantB < 0 or constantB > 1000:
            done = False
        if constantC < 0 or constantC > 1000:
            done = False
        if constantD < 0 or constantD > 1000:
            done = False
        if valK < 1 or valK > 1000000:
            done = False
        if not done:
            print("invalid constant or variable")  
        
        price = CalPrice( constantP, constantA, constantB, constantC, constantD, valK )
        fileOut.write('The largest decline is {0:.6f} \n ' .format(MaxDec(price)))
        #print('The largest decline is {0:.6f} ' .format(MaxDec(price)))
else:
    print("input file dosen't exist")


# done = False
# while not done: 
#     print('Enter constants p, which between 1 to 1,000')
#     constantP = int( input() )
#     if constantP >= 1 and constantP <= 1000:
#         done = True
# done = False

# while not done:
#     print('Enter constants a, which between 0 to 1,000')
#     constantA = int( input() )
#     if constantA >= 0 and constantA <= 1000:
#         done = True
# done = False

# while not done: 
#     print('Enter constants b, which between 0 to 1,000')
#     constantB = int( input() )
#     if constantB >= 0 and constantB <= 1000:
#         done = True
# done = False

# while not done: 
#     print('Enter constants c, which between 0 to 1,000')
#     constantC = int( input() )
#     if constantC >= 0 and constantC <= 1000:
#         done = True
# done = False

# while not done: 
#     print('Enter constants d, which between 0 to 1,000')
#     constantD = int( input() )
#     if constantD >= 0 and constantD <= 1000:
#         done = True
# done = False

# while not done: 
#     print('Enter constants k, which between 1 to 1,000,000')
#     valK = int( input() )
#     if valK >= 1 and valK <= 1000000:
#         done = True
# done = False

# price = CalPrice( constantP, constantA, constantB, constantC, constantD, valK )
# print('The largest decline is {0:.6f} ' .format(MaxDec(price)))

#print( price )
