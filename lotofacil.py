from math import sqrt; from itertools import count, islice

__doc__ = """\
Library with functios to organize the list of numbers on the drawing column
"""

def freq_sum(result):
    '''
        Organize de the numbers
    '''
    # Create a list of integers with the draw
    result_as_integer = list(map(int,result.split('-')))
    #
    count = 0
    for i in result_as_integer:
        if i<=10:
            count+=i
    return count

def freq_1to10(result):
    '''
        Organize de the numbers
    '''
    # Create a list of integers with the draw
    result_as_integer = list(map(int,result.split('-')))
    #
    count = 0
    for i in result_as_integer:
        if i<=10:
            count+=1
    return count

def freq_11to20(result):
    '''
        Organize de the numbers
    '''
    # Create a list of integers with the draw
    result_as_integer = list(map(int,result.split('-')))
    #
    count = 0
    for i in result_as_integer:
        if i<=20 and i>10:
            count+=1
    return count

def freq_21to25(result):
    '''
        Organize de the numbers
    '''
    # Create a list of integers with the draw
    result_as_integer = list(map(int,result.split('-')))
    #
    count = 0
    for i in result_as_integer:
        if i>=21:
            count+=1
    return count



def organize_cresc(result):
    '''
        Organize de the numbers
    '''
    result_as_integer = list(map(int,result.split('-')))
    result_as_integer.sort()
    result_organized = '-'.join(str(e) for e in result_as_integer)
    return result_organized


def freq_even(result):
    '''
        Get a string separate with dash's -, split values,
        Return a absolute value with the number of even numbers
    '''
    result_as_integer = list(map(int,result.split('-')))
    
    freq_even = 0
    for n in result_as_integer:
        if n%2 == 0:
            freq_even+=1
    return(freq_even)

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))  

def freq_prime(result):
    '''
        Get a string separate with dash's -, split values,
        Return a absolute value with the number of prime numbers
    '''
    result_as_integer = list(map(int,result.split('-')))
    #print(result_as_integer)
    freq_prime = 0
    for n in result_as_integer:
        if is_prime(n) == True:
            freq_prime+=1
    return(freq_prime)
