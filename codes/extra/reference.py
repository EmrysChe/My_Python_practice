oldlist = ['one','two','three','four']
newlist = oldlist

del newlist[0]

print('oldlist is', oldlist)
print('newlist is', newlist)

print('{0:*^40}'.format("*"))

newlist2 = oldlist[:]

del oldlist[0]

print('oldlist is', oldlist)
print('newlist2 is', newlist2)