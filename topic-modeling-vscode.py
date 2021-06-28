import math #import math module to get access to mathematical functions
import os #import operating system (allows you to navigate or manipulate directories)
import re #import regex module

os.chdir("/Users/averymatteo/Desktop/projects/") #use os.chdir to navigate to where College News issues are stored

inCorpus = "issues" #define inCorpus as issues
outCorpus = "60s-tm" #define outCorpus as the decade you want 

if os.path.exists(outCorpus) == False: #use comparison operator to text the existence of the folder
    os.mkdir(outCorpus) #create outCorpus (come back to 10 & 11 later)

filenames = [] #create a list
for root, dirs, files, in os.walk(inCorpus, topdown=False): 
# root : prints out directories only from what you specified (this case root is inCorpus)
# dirs : prints out sub-directories from root
# files : prints out all files from root and directories

    for name in files: #create for loop iterating through files
        if '196' in name: #search for files that start with 196
            filenames.append(os.path.join(root, name)) #add issues and 196 to list of files

for issue in filenames: #create for loop iterating through every issue
    f = open(issue, 'r', encoding='utf-8') #open and read the issue
    text = f.read() #set text equal to the issue that is read
    f.close() #
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




