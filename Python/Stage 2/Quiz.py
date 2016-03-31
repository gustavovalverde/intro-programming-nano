def isNone(x):
    if x is not None:
        print "not None"
    if x:
        print "it's there"

y = None
z = 1

print "Try 1, y is None:"
isNone(y)

print "Try 2, z is 1:"
isNone(z)
