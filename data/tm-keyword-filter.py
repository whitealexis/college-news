import math # math library used to identify number of files needed
import os 
import re

os.chdir("/Users/averymatteo/Desktop/projects/") # set working directory as folder containing issues folder

inCorpus = "issues" # corpus input: folder for the text files you read
outCorpus = "60s-tm" # corpus output: folder for text files you write

if os.path.exists(outCorpus) == False: # checks to see if your out folder exists
    os.mkdir(outCorpus)

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
    chunks = math.floor(characters/500) # number of chunks
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

