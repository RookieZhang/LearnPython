#!/usr/bin/python

def printMax(x,y):
    '''Print the maximum of two numbers'''

    x = int(x)
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'


print printMax.__doc__
