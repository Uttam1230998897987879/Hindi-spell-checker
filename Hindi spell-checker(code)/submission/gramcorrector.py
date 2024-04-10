import re, collections, codecs ,os
import time
from load_unis import *
from load_bigs import *

alphabet = 'अआइईउऊएऐओऔअंअःऍऑऋँंः़ािीुूृॄॅेैॉोौ्कक़खख़गग़घङचछजज़झञटठडड़ढढ़णतथदधनपफफ़बभमयय़रलळवशषसहक्षत्रज्ञर्‍श्र'
tests1 = {}

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in d1)

def known(words): return set(w for w in words if w in d1)

def known2(words): return set(w for w in words if w in d1)

def correctg(gram):
    replacements = collections.defaultdict(lambda: 0)
    (word1,word2) = gram.split()
    w1s = known(edits1(word1)).union(known(word1))
    w2s = known(edits1(word2)).union(known(word2))
    for w1 in w1s:
         w = w1+' '+word2
         if w in d02g:
            replacements[w] = d02g[w]
    for w2 in w2s:
         w = word1+' '+w2
         if w in d02g:
            replacements[w] = d02g[w]
    return sorted(replacements,key=replacements.get,reverse=True)[:5]

def correct5(word):
    candidates = known([word]) or known(edits1(word)) or  known_edits2(word) or [word]
    return sorted(candidates,key=d12g.get, reverse=True)

            
def correct_sentence(sentencew):
   wordsw = sentencew.strip().split()
   #wordsc = sentencec.strip().split()
   for i in range(0,len(wordsw)-1):
      w = wordsw[i]+' '+wordsw[i+1]
      #wc = wordsc[i]+' '+wordsc[i+1]
      reps = correctg(w)
      if(w not in reps):
          return set(reps)

def testing(lines):
   n = 0
   bad = 0
   unknown = 0
   good = 0
   for i in range(0,len(lines)):
      if(i%2==0):
         if(correct_sentence(lines[i].replace('"',''),lines[i+1].replace('"',''))==True):
            good += 1
         else:
            bad+=1
   print(len(lines)/2 )
   print(good)
   print(bad)

