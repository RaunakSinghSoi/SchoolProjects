#Date:9/12/2021
#version: Version 1.0
import csv
def load_dataset(filename)->{str:list}:

 csvfile = open(filename,'r') 
 reader=csv.DictReader(csvfile)
 library=list(reader)
 genres={}
 for genre in library:
    dict={'title':genre['title'],'author':genre['author'],'rating':genre['rating'],'publisher':genre['publisher'],'page_count':genre['page_count'],'language':genre['language']}
    genres[genre['generes']]=genres.get(genre['generes'],[])+[dict]
 dict = list(dict.fromkeys(dict))
 csvfile.close()
 
 return genres
#print(load_dataset("Google_Books_Dataset.csv"))
