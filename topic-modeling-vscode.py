import math #import math module to get access to mathematical functions
import os #import operating system (allows you to navigate or manipulate directories)
import re #import regex module

os.chdir("/Users/averymatteo/Desktop/projects/") #use os.chdir to navigate to where College News issues are stored

inCorpus = "issues" #define inCorpus as issues
outCorpus = "60s-tm" #define outCorpus as the decade you want 

if os.path.exists(outCorpus) == False: #use comparison operator to test the existence of the folder
    os.mkdir(outCorpus) #create outCorpus folder (come back to 10 & 11 later)

filenames = [] #create a list
for root, dirs, files, in os.walk(inCorpus, topdown=False): 
# root: prints out directories only from what you specified (this case root is inCorpus)
# dirs: prints out sub-directories from root
# files: prints out all files from root and directories

    for name in files: #create for loop iterating through files
        if '196' in name: #search for files that start with 196
            filenames.append(os.path.join(root, name)) #add issues and 196 to list of files

for issue in filenames: #create for loop iterating through every issue
    f = open(issue, 'r', encoding='utf-8') #open and read the issue
    text = f.read() #set text equal to the issue that is read
    f.close() #close text file so it cannot be read or written. important to do to prevent data loss
    characters = len(text) #define characters as the entire length of the text
    chunks = math.floor(characters/500) 
  #chunks: defined as each 500 character chunk
  #math.floor: rounds the number down
    
# print(chunks)
# range(chunks)
    issue_name = issue[7:19] #issue_name defined as characters 7 through 19 in the file name, extracting the date (YYYY, MM, DD)
    start=0 #start at character 0
    stop=500 #stop at character 500

    for i in range(chunks): #come back
        slice = text[start:stop] #create slices in text at the start and stop marks indicated above
        start+=500 #start+ iterates through each successive set of 500 character chunks
        stop+=500 #stop+ tells loop to stop and restart at the end of the 500 characters
        newfile = outCorpus + "/" + issue_name + '-chunk' + str(i) + '.txt' #create new file name

f = open(newfile, "w") #open new file created on previous line
f.write(slice) #writes each piece of sliced text
f.close() #closes text file




