import re, collections, codecs ,os

f0 = codecs.open('bi0.txt','r+','utf-8')
d02g = eval(f0.read())

f1 = codecs.open('bi5.txt','r+','utf-8')
#d12g = eval(f1.read())

f2 = codecs.open('bi10.txt','r+','utf-8')
#d22g = eval(f2.read())

f3 = codecs.open('bi20.txt','r+','utf-8')
#d32g = eval(f3.read())


f1.close()
f2.close()
f3.close()

print('done')
