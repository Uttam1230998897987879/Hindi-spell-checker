import re, collections, codecs ,os

f0 = codecs.open('uni0.txt','r','utf-8')
d0 = eval(f0.read())

f1 = codecs.open('uni5.txt','r','utf-8')
d1 = eval(f1.read())

f2 = codecs.open('uni10.txt','r','utf-8')
d2 = eval(f2.read())

f3 = codecs.open('uni20.txt','r','utf-8')
d3 = eval(f3.read())

f4 = codecs.open('uni50.txt','r','utf-8')
d4 = eval(f4.read())

f7 = codecs.open('uni7.txt','r','utf-8')
d7 = eval(f7.read())

print(len(d0))
print(len(d1))
print(len(d2))
print(len(d3))
print(len(d4))
print(len(d7))
f1.close()
f2.close()
f3.close()
f4.close()
f7.close()
print('done')
