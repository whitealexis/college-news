#geopolitical entity (GPE) search and store for college news

import spacy #natural language processing, for named-entity recognition
#import os #operating system, for access to its information
import csv #for reading and writing data to a csv file

nlp = spacy.load("en_core_web_trf", disable=["attribute_ruler", "lemmatizer"]) #load english pipeline with highest accuracy, disable unecessary components

#search for all GPEs in each college news issue

rows = [] #create list
filebatch = ["cn1965-11-05.txt", "cn1968-10-18.txt"] 
filebatchtext = []
for file in filebatch:
    f = open(file, "r", encoding = "utf-8") #open file
    cn_text = f.read() #read file
    filebatchtext.append(cn_text)
    f.close()
docs = list(nlp.pipe(filebatchtext))
for doc in docs:
    places = {} #create dictionary
    for ent in doc.ents: #for every entity found in file, do these steps:
        if ent.label_ == "GPE": #if entity is a GPE:
            cleantext = ent.text.replace("\n", " ")
            if cleantext in places.keys(): #if GPE's text (place name) already exists in dictionary:
                places[cleantext] += 1 #increase count by 1
            else: #if GPE's text doesn't exist in dictionary:
                places[cleantext] = 1 #add to dictionary with count of 1
    i = docs.index(doc)
    filename = filebatch[i]
    for key in places:
        data = [filename, key, places[key]]
        rows.append(data)

#write csv file to store GPEs information
header = ["filename", "GPE", "count"] #name header cells
#put desired csv file name below in quotes
with open("csv-file-name.csv", "w", encoding = "utf-8", newline = '') as outfile: #create, open and write to csv file
    writer = csv.writer(outfile) #create csv writer
    writer.writerow(header) #write header row
    writer.writerows(rows) #write information rows