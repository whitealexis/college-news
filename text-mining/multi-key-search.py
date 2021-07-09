"""
Date: 25 June 2021
Modified from cn-keyword-search.py

Keyword search: 
    - Uses regular expressions to search the corpus for one or more keywords
    - Creates a csv file for each issue the word is found in (NB: row per keyword instance)

"""

# import  statements 
import re #regular expressions, checks if a string matches a regular expression
import os #operating system, accesses its information
import csv #provides classes for reading and writing data to a csv file


#######################################################################

# defines regex objects for each of your given keywords
keyrex = [
        ['May Day', r'may(\s?)day'], # for each word, create a list with one regular expression and one display keyword
        ['Lantern Night', r'lantern\snight']
            ]

# defines function that searches a given piece of text for a given regex and returns a count of how many times that keyword appears
def countkeys(regex, text): # this function requires two variables: a regular expression and a longer string
    keyword_list = re.findall(regex, text, flags=re.IGNORECASE) #find all keyword instances, regardless of capitalization, in text
    keywordcount = len(keyword_list) # count keyword instances found
    return keywordcount # output of the function is

def get_contexts(keyword, text, chars):
    n = 0 # Generates a list of passages that include the keyword
    context_passages = []
    for instance in re.finditer(keyword, text[n:], flags=re.IGNORECASE):
        startindex, endindex = instance.span()
        if startindex > chars:
            startcontext = startindex - chars 
        else:
            startcontext = 0
        if startindex + chars > len(text) - 1:
            endcontext = len(text) - 1
        else:
            endcontext = startindex + chars
        context = cn_text[startcontext:endcontext] 
        n = endindex
        cleantext = context.replace('\n', ' ')
        context_passages.append(cleantext)
    return context_passages
    
########################################################################## 

rows = [] #create a list 
directory = "/Users/amcgrath1/college-news/issues/" #put directory path to your folder with all college news issues here after r and in quotes

for filename in os.listdir(directory): #for every file in the folder, do these steps:
    if filename.endswith(".txt"): #if file ends in .txt (which all should - to avoid processing hidden files)
        date = filename[2:12] # slice the filename to get date yyyy-mm-dd
        year, month, day = date.split('-') # splits the date into year, month, day
        filepath = directory + filename #add folder name to file name in order to get the full filepath
        f = open(filepath, "r", encoding = "utf-8") #open file
        cn_text = f.read() #read file into a string
        for key in keyrex:
            word = key[0] # display keyword
            regex = key[1] # regular expression for keyword
            passages = get_contexts(regex, cn_text, 200) # calls function above
            for passage in passages:
                data = [filename, date, year, month, word, passage] #group file name (minus issues/ and .txt parts), date, keyword, and keyword count in a list
                rows.append(data) #put data into rows variable

#write csv file to store keyword information
#use GUI to create and save an empty csv file
header = ["filename", "date", "year", "month", "keyword", "count"] #name header cells
#put saved csv file name below in quotes
with open("multisearch.csv", "w", encoding = "utf-8", newline = '') as outfile: #open and write to csv file
    writer = csv.writer(outfile) #create csv writer
    writer.writerow(header) #write header row
    writer.writerows(rows) #write information rows

"""
Next steps:
- Get keyword contexts

"""