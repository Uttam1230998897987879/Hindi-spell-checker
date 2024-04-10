import re
import collections
import codecs

alphabet = 'कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञर्‍श्रळँंः़ािीुूृॄॅेैॉोौ्अआइईउऊएऐओऔअंअःऍऑऋ'
pattern = '[' + alphabet + ']+'
path = './'

def words(text):
    return re.findall(pattern, text)

def traingrams(features):
    with codecs.open(path + 'myfile.txt', 'w+', 'utf-8') as myfile:
        model = collections.defaultdict(lambda: 1)
        for i in range(len(features) - 2):
            myfile.write(features[i] + ' ')
            f = features[i] + ' ' + features[i + 1] + ' ' + features[i + 2]
            model[f] += 1
    return model

file_path = 'merge.txt'
with codecs.open("D:\OneDrive\Desktop\Hindi spell-checker(code)\submission\merge.txt", 'r', 'utf-8') as file:
    NWORDS = traingrams(words(file.read()))

with codecs.open('tri0.txt', 'w+', 'utf-8') as f0:
    for key, value in NWORDS.items():
        if value > 0:
            f0.write(f'{key}: {value}\n')