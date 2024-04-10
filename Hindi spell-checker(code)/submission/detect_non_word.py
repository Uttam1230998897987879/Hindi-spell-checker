import re, collections, codecs ,os
import time
from load_unis import *
count=0
alphabet = '़ािीुूृॅेैॉोौ्ज़य़ँंःअआइईउऊऋएऐऑओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरऱलवशषसह'
pattern = '['+alphabet+']+'
def words(text): return re.findall(pattern,text) 

ofile = codecs.open('articles.txt','r','utf-8')
word_list = ofile.read()
total = len(word_list)
for word in word_list:
    if(word not in d7):
        count +=1
ofile.close()
print('---------------')
print(total)
print(count)