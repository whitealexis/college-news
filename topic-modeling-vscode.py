import math
import os
import re

os.chdir("/Users/averymatteo/Desktop/projects/")

inCorpus = "issues"
outCorpus = "60s-tm"

if os.path.exists(outCorpus) == False:
    os.mkdir(outCorpus)
from nltk import corpus

filenames = []
for root, dirs, files, in os.walk(inCorpus, topdown=False):
    for name in files:
        if '196' in name:
            filenames.append(os.path.join(root, name))

for issue in filenames:
    f = open(issue, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    characters = len(text)
    chunks = math.floor(characters/500)
 # print(chunks)
# range(chunks)
    issue_name = issue[7:19]
    start=0
    stop=500

    for i in range(chunks):
        slice = text[start:stop]
        start+=500
        stop+=500
        newfile = outCorpus + "/" + issue_name + '-chunk' + str(i) + '.txt'

f = open(newfile, "w")
f.write(slice)
f.close()




