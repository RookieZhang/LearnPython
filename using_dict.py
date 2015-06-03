#!/usr/bin/python

ab ={
    'Swaroop'    :     'swaroop@byteofpython.info',
    'Larry'      :     'larry@wall.org',
    'Matsumto'   :     'matz@ruby-lang.org',
    'Sparmmer'   :     'spammer@hotmail.com'
}

print "Swaroop's address is %s" % ab['Swaroop']

ab['Guido'] = 'guido@pyhton.org'

del ab['Sparmmer']

print '\nThere are %d contacts int the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)

if 'Guido' in ab:
    print "\nGuido's address is %s" % ab['Guido']
