#!/usr/bin/python

class ShortInputException(Exception):
    '''a user-defined Exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = raw_input("Enter someting --> ")
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except EOFError:
    print '\bWhy did you do an EOF on me'
except ShortInputException, x:
    print "ShortInputException: The input was of length %d, was excepting at least %d" % (x.length, x.atleast)
else:
    print 'No exception was raised'

