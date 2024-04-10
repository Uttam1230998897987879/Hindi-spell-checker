import re, collections, codecs ,os
import time
alphabet = '़ािीुूृॅेैॉोौ्ज़य़ँंःअआइईउऊऋएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरऱलवशषसह'
pattern = '['+alphabet+']+'
path = './'
file = codecs.open('merge.txt','r','utf-8')

def words(text): return re.findall(pattern,text) 

def traingrams(features):
    myfile = codecs.open(path+'myfile.txt','w+','utf-8')
    sum = 0
    model = collections.defaultdict(lambda: 0)
    for i in range(0,len(features)-1):
        myfile.write(features[i]+' ')
        f = features[i]+' '+features[i+1]
        model[f] += 1
        sum+= 1
    myfile.close()
    return model

d02g = {}

NWORDS = traingrams(words(file.read()))
for key in NWORDS:
	if NWORDS[key] > 0:
		d02g[key] = NWORDS[key]

d12g = {}

for key in NWORDS:
	if NWORDS[key] > 5:
		d12g[key] = NWORDS[key]
d22g = {}
for key in NWORDS:
	if NWORDS[key] > 10:
		d22g[key] = NWORDS[key]
d32g = {}
for key in NWORDS:
	if NWORDS[key] > 20:
		d32g[key] = NWORDS[key]


f0 = codecs.open('bi0.txt','w+','utf-8')
f0.write(str(d02g))

f1 = codecs.open('bi5.txt','w+','utf-8')
f1.write(str(d12g))

f2 = codecs.open('bi10.txt','w+','utf-8')
f2.write(str(d22g))

f3 = codecs.open('bi20.txt','w+','utf-8')
f3.write(str(d32g))


f1.close()
f2.close()
f3.close()
