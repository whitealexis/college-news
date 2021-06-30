#geopolitical entity (GPE) search and store for college news

import spacy #natural language processing, for named-entity recognition
import os #operating system, for access to its information
import csv #for reading and writing data to a csv file

nlp = spacy.load("en_core_web_trf") #load english pipeline with highest accuracy

#search for all GPEs in each college news issue
places = {} #create dictionary
rows = [] #create list
directory = r"C:\Users\arina\Desktop\projects\issues" #put directory path to your folder with all college news issues here
for filename in os.listdir(directory): #for every file in the folder, do these steps:
    if filename.endswith(".txt"): #if file ends in .txt (which all issue files should):
        newfilename = "issues/" + filename #add folder name to file name
        f = open(newfilename, "r", encoding = "utf-8") #open file
        cn_text = f.read() #read file
        doc = nlp(cn_text) #use pipeline on file
        for ent in doc.ents: #for every entity found in file, do these steps:
            if ent.label_ == "GPE": #if entity is a GPE:
                if ent.text in places.keys(): #if GPE's text (place name) already exists in dictionary:
                    places[ent.text] += 1 #increase count by 1
                else: #if GPE's text doesn't exist in dictionary:
                    places[ent.text] = 1 #add to dictionary with count of 1
data = [filename, places] #group file name and places in a list
rows.append(data) #put data into rows variable

#write csv file to store GPEs information
#use GUI to create and save an empty csv file
header = ["filename", "GPEs"] #name header cells
#put saved csv file name below in quotes
with open("csv-file-name.csv", "w", encoding = "utf-8", newline = '') as outfile: #open and write to csv file
    writer = csv.writer(outfile) #create csv writer
    writer.writerow(header) #write header row
    writer.writerows(rows) #write information rows