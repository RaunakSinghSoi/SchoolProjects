#Date:9/12/2021
#version: Version 1.0
#T085
#MEMBERS:RAUNAK ,KATIE,WYLIE ,ISABELLA


from T085_load_data import load_dataset
def to_list(dictionary):
  z=[]
  kk=[]
  for line in dictionary:
    for l in range(len(dictionary[line])):
        dict={'generes':line}
        dictionary[line][l].update(dict)
    z.append(dictionary[line])
  for i in z:
    for j in i:
      kk.append(j)
  return kk
dictionary=load_dataset('Google_Books_Dataset.csv')

def sort_books_publisher(dictionary):
  """
  Returns a list where the dictionary is sorted by title.
  Author: Raunak
  Edited by: Raunak
  """    
  reader=to_list(dictionary)
  n=len(reader)
  for i in range(n):
      for j in range(0,n-i-1):
        if reader[j]['publisher']>reader[j+1]['publisher']:
          reader[j],reader[j+1]=reader[j+1],reader[j]
        if reader[j]['publisher']==reader[j+1]['publisher']:
          if reader[j]['title']>reader[j+1]['title']:
            reader[j],reader[j+1]=reader[j+1],reader[j]
                       
                 
                               
  return reader
             
def sort_books_ascending_rate(dictionary):
  """
  Returns a list where the dictionary is sorted by ascending rate.
  Author: Katie
  Edited by: Raunak
  
  
  """
  reader=to_list(dictionary)
  n=len(reader)
  for i in range(n):
    for j in range(0,n-i-1):
       
      if reader[j]['rating']>reader[j+1]['rating']:
        reader[j],reader[j+1]=reader[j+1],reader[j]
      if reader[j]['rating']==reader[j+1]['rating']:
        if reader[j]['rating']>reader[j+1]['rating']:
          reader[j],reader[j+1]=reader[j+1],reader[j]
           
     
                   
                 
                             
  return reader

def sort_books_descending_rate(dictionary):
  """
  
  Returns a list where the dictionary is sorted by descending rate.
  Author: Isabella
  Edited by: Raunak
  
  
  
  """
  reader=to_list(dictionary)
  n=len(reader)
  for i in range(n):
    for j in range(0,n-i-1):
      if reader[j]['rating']<reader[j+1]['rating']:
        reader[j],reader[j+1]=reader[j+1],reader[j]
  return reader

def sort_books_title(dictionary):
  """
  Returns a list where the dictionary is sorted by title.
  Author: Katie
  Edited by: Raunak
  """
  reader=to_list(dictionary)
  n=len(reader)
  for i in range(n):
    for j in range(0,n-i-1):
     
      if reader[j]['title']>reader[j+1]['title']:
        reader[j],reader[j+1]=reader[j+1],reader[j]
      if reader[j]['title']==reader[j+1]['title']:
        if reader[j]['title']>reader[j+1]['title']:
          reader[j],reader[j+1]=reader[j+1],reader[j]
                     
                 
                             
  return reader
 
       
     
def sort_books_pageCount(dictionary):
  """
  Returns a list where the dictionary is sorted by title.
  Author: Raunak
  Edited by: Raunak
  """  
  reader=to_list(dictionary)
  n=len(reader)
  for i in range(n):
      for j in range(0,n-i-1):
        reader[j]['page_count']=int(reader[j]['page_count'])
        reader[j+1]['page_count']=int(reader[j+1]['page_count'])
        if reader[j]['page_count']>reader[j+1]['page_count']:
          reader[j],reader[j+1]=reader[j+1],reader[j]
        if reader[j]['page_count']==reader[j+1]['page_count']:
          if reader[j]['title']>reader[j+1]['title']:
            reader[j],reader[j+1]=reader[j+1],reader[j]
                       
        reader[j]['page_count']=str(reader[j]['page_count'])
        reader[j+1]['page_count']=str(reader[j+1]['page_count'])                
                               
  return reader
             

def sort_books_category(dictionary):
  """
  Returns a list where the dictionary is sorted by title.
  Author: Raunak
  Edited by: Raunak
  """      
  z=to_list(dictionary)
  n=len(z)
  for i in range(n):
        for j in range(0,n-i-1):
            if z[j]['generes']>z[j+1]['generes']:
                z[j],z[j+1]=z[j+1],z[j]
            if z[j]['generes']==z[j+1]['generes']:
                if z[j]['title']>z[j+1]['title']:
                  z[j],z[j+1]=z[j+1],z[j]
  return z
