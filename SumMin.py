import sympy
import random
from sympy import *
import matplotlib.pyplot as plt

#Returns min|+-primes[0]+-primes[1]+-...+-primes[len(primes) - 1]| and the list
#with the appropriate sign +- for each element. 
def minSum(primes):
    n = len(primes)
    if n == 1:
        return 2
    else:
        S = primes[n - 1] - primes[n - 2]
        newSet = primes
        newSet[n - 2] = -primes[n - 2]
        i = 3 
        while i <= n:
            if S == 0:
                S = S + primes[n - i]
            elif abs(S - primes[n - i]) <= abs(S + primes[n - i]):
                S = S - primes[n - i]
                newSet[n - i] = -primes[n - i]
            else:
                S = S + primes[n - i]
            i = i + 1
        return abs(S)
    #print("MIN:",abs(S))
    #print(newSet)

#Returns the sum |+-primes[0]+-primes[1]+-...+-primes[len(primes) - 1]| that gives the min.
def actualSum(primes):
    n = len(primes)
    S = primes[n - 1] - primes[n - 2]
    newSet = primes
    newSet[n - 2] = -primes[n - 2]
    i = 3 
    while i <= n:
        if S == 0:
            S = S + primes[n - i]
        elif abs(S - primes[n - i]) <= abs(S + primes[n - i]):
            S = S - primes[n - i]
            newSet[n - i] = -primes[n - i]
        else:
            S = S + primes[n - i]
        i = i + 1
    #return abs(S)
    #print("MIN:",abs(S))
    return newSet

def adjustedSum(primes):
    defaultSum = actualSum(primes)
    if defaultSum[0] == -2:
        i = 0
        adjustedSum = []
        while i < len(defaultSum):
            adjustedValue = -1 *defaultSum[i]
            adjustedSum.append(adjustedValue)
            i = i + 1
        return adjustedSum
    else:
        return defaultSum

def averageSum(primes):
    return sum(primes)/len(primes)
    

#Gives a list of the first n primes (least to greatest).
def primeList(n):
    i = 1
    j = 0
    primes = []
    if n == 1:
        return [2]
    else:
        while i <= n:
            if sympy.isprime(j):
                primes.append(j)
                j = j + 1
                i = i + 1
            else:
                j = j + 1
        return primes


#Returns a list of ++, --, +-, or -+ which correspond to adjecent elements of
#the parameter
def signsList(primes):
    signs = []
    i = 0
    if len(primes) % 2 == 0:
        while i < len(primes):
            if primes[i] < 0 and primes[i + 1] < 0:
                signs.append('--')
            elif primes[i] > 0 and primes[i + 1] > 0:
                signs.append("++")
            elif primes[i] > 0 and primes[i + 1] < 0:
                signs.append("+-")
            else:
                signs.append("-+")
            i = i + 2
    else:
        while i < len(primes) - 1:
            if primes[i] < 0 and primes[i + 1] < 0:
                signs.append('--')
            elif primes[i] > 0 and primes[i + 1] > 0:
                signs.append("++")
            elif primes[i] > 0 and primes[i + 1] < 0:
                signs.append("+-")
            else:
                signs.append("-+")
            i = i + 2
        if(primes[len(primes) - 1] > 0):
            signs.append("+")
        else:
            signs.append("-")
        
    return signs

#Return the difference sum1 - sum2 (as a string) where
# sum1 is the sum of all the primes assigned a "+"
# and sum2 is the sum of all the primes assigned a "-".
def difference(primes):
    i = 0
    sum1 = 0
    sum2 = 0
    while i < len(primes):
        if(primes[i] > 0):
            sum1 = sum1 + primes[i]
        else:
            sum2 = sum2 + primes[i]
        i = i + 1
    sum1 = str(sum1)
    sum2 = str(abs(sum2))
    sum = f"{sum1} - {sum2}"
    return sum

#Returns the "final sum", sum1 - sum2 with all the terms shown, that gives Pn.
def finalSum(primes):
    i = len(primes) - 1
    sum1 = []
    sum2 = []
    while i >= 0:
        if(primes[i] > 0):
            sum1.append(primes[i])
        else:
            sum2.append(primes[i])
        i = i - 1
    i = 0
    first = str(sum1[0])
    second = str(abs(sum2[0]))
    while i < len(sum1) - 1:
        first = first + f" + {str(sum1[i + 1])}"
        i = i + 1
    i = 0
    while i < len(sum2) - 1:
        second = second + f" + {str(abs(sum2[i + 1]))}"
        i = i + 1
    return f"({first}) - ({second})"

#Returns the number of minsums of 0, 1, and 2 up to a certain number, n, of primes. 
def counter(n):
    i = 1
    zero = 0
    one = 0
    two = 0
    other = 0
    primes = primeList(i)
    while i <= n:
        v = minSum(primes)
        if v == 0:
            zero = zero + 1
        elif v == 1:
            one = one + 1
        elif v == 2:
            two = two + 1
        else:
            other = other + 1
        i = i + 1
        primes.append(prime(i))
    return f"Zeroes: {zero}\nOnes: {one}\nTwos: {two}\nOther: {other}"

#Returns the sum of the first n primes. This is the (capital) sigma function.
def sigma(n):
    primes = primeList(n)
    sum = 0
    i = 0
    while i <= len(primes) - 1:
        sum = sum + primes[i]
        i = i + 1
    return sum


while True:
    n = int(input("Number of primes: "))
    print(primeList(n))
    print("Pn =",minSum(primeList(n)))
    #print(actualSum(primeList(n)))
    #print("Average of terms(Pn): m = ",averageSum(adjustedSum(primeList(n))))
    #print(adjustedSum(primeList(n)))
    #print(signsList(actualSum(primeList(n))))
    #print(signsList(actualSum(primeList(n))), sep =', ')
    #print(difference(actualSum(primeList(n))))
    #print(finalSum(actualSum(primeList(n))))
    #print(counter(n))
    #print("∑(n) = ",sigma(n))
    
    '''
    #plotting the points S
    X = []
    Y = []
    #v = 1
    #v = len(actualSum(primeList(n)))
    plt.ylabel('Pn')
    plt.xlabel('n')
    x = 1
    while x <= n:
        y = minSum(primeList(x))
        Y.append(y)
        X.append(x)
        x = x + 1  
    
    #while v <= n:
        #v = v + 1
        #color='none', linestyle = 'dashed', linewidth = 20,
        #marker = 'o', markersize = 8, markerfacecolor = 'blue', markeredgecolor = 'blue'
   
    
    #giving a title to my graph
    plt.plot(X, Y)
    plt.title('Pn vs. n')
    #function to show the plot
    plt.grid()
    plt.show()    
    '''
    
    
