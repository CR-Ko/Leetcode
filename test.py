
l = [1,2,3,4,5,'aa','bb']
print l
print l[0]
print l[1:4]
print l[:]
print l[:-2]
l.append(123)
print l
l.insert(0,'nn')
print l
l.extend(['a','b','c'])
print l

l.remove('c')
print l

l2 = [1,2,3,4]
for k in range(len(l2)-1,-1,-1):
 print k

