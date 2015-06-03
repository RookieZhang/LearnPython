#!usr/bin/python

zoo = ('wolf', 'elephant', 'penguin')
print 'number of animals in the zoo is', len(zoo)

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'animals brought from old zoo are', new_zoo[2]
print 'Last animals bought from old zoo is', new_zoo[2][2]
