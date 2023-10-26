#Date:9/12/2021
#version: Version 1.0
#T085
#MEMBERS:RAUANK ,KATIE,WYLIE ,ISABELLA
#FUNCTION 1,5,9 :RAUNAK
#FUNCTION 2,6,10:WYLIE
#FUNCTION 3,7,11:KATIE
#FUNCTION 4,8,12:ISABELLA
#Edited by :Raunak
from T085_load_data import load_dataset
#Function 1
def print_dictionary_category(dictionary,category):
    """
    author:RAUNAK SINGH SOI
    edited by
    Returns number of books and titles under given category.
    >>>print_dictionary_category(dictionary,category)
    The category Information Technology has 1 books. This is the list of books in the category: [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', '"rating"': '4.6', '"publisher"': 'Crown Business', '"page_count"': '464', '"language"': 'English'}]
     1 books
    >>>print_dictionary_category("Google_Books_Dataset.csv",'Money Management')

    The category Money Management has 1 books. This is the list of books in the category: [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', '"rating"': '3.7', '"publisher"': 'Hachette UK', '"page_count"': '30', '"language"': 'English'}]
     1 books
    """    
    
    z=[]
     
    for line in dictionary:
        if category==line:
            k=len(dictionary[line])
            for i in range(k):
                z.append(dictionary[line][i]['title'])
    
    for line in dictionary:
        k=str(k) 
        z=str(z)
        return 'The category '+category+' has '+k+' books.'+"This is the list of books in the category: \n"+z
#FUNCTION 2
def add_book(dictionary1 : dict, book_details : list)-> dict:
    """
    author:Wylie Smith
    """
    book_properties = {"title", "author", "language", "publisher", "generes", "rating", "page_count"}
    newbook = {}
    category = book_details[4]
  
    addedbook = True
    current_list = dictionary1.get(category)
    if current_list == None:
        dictionary1.update({category:[]})
    for book in current_list:
        if book["title"] == book_details[0]:
            addedbook = False
    if addedbook ==True:
        for i in range(len(book_details)):
            if book_properties[i] != "generes":
                newbook.update({book_properties[i]:book_details[i]})
        new_list = current_list + [book_dict]
        dictionary1.update({category:new_list})
        print("The book has been added correctly!")
    else:
        print("There was an error adding the book.")
    return dictionary1

#Function 3
def remove_book(book,category):
    """
    author:Katie Stewart
    Returns dictionary with the requested book removed.
  
    >>>remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
    >>>The book has been removed correctly
    >>>remove_book('Pride and Prejudice', 'Fiction', 'Google_Books_Dataset.csv')
    >>>There was an error removing the book. Book not found.
    """    
    dictionary=load_dataset('Google_Books_Dataset.csv')
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])):
            if book in (dictionary[category][i]['title']):
                del[(dictionary[category][i])]
                print('Book removed succesfully')
            elif book not in (dictionary[category][i]['title']):
                print('There was an error removing the book. Book not found.')  
            return dictionary
#Function 4
def get_rate(dictionary,rating):
    """
    author:Isabella Gonzalo

    Returns a list of books with the specified rating
  
    >>> get_books_by_rating(dictionary,rating)
    >>> {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': '3.8', 'publisher': 'Penguin', 'pageCount': '272', 'category': 'Business', 'language': 'English'}
    """    
    
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])):
            if dictionary[category][i]['rating']=='':
                dictionary[category][i]['rating']='0'
            rating=int(float(rating))            
            for rating in range(rating,rating+1):
                if rating==int(float(dictionary[category][i]['rating'])):
                    z.append(dictionary[category][i])
    return z

#Function 5
def find_book(dictionary,title):
    """
    author:RAUNAK SINGH SOI
    Returns a boolean which determines whether given book is present in given dictionary.
    >>>find_book(dictionary,"The Malady and Other Stories: An Andrzej Sapkowski Sampler")
    The book has been found
    True
    >>>find_book("Google_Books_Dataset.csv","We")
    The book has been found
    True
 
    """    
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])):
            z.append((dictionary[category][i]['title']))
            
    return(bool(title in z))
#Function 6
def get_books_by_author(author, dictionary )->list:
  
    """
    author:WYLIE SMITH
    
    """
    lst_title=[]
  
    print('The author "' + author + '" has written the following books:')
    count= 1
    for category in dictionary.keys(): #dict with title as a key but also author
        for book in dictionary.get(category):
            if book.get('author') == author:
                title= book.get('title')
                if title not in lst_title: #to prevent repetition
                    print('\t', str(count) , '- ' , title , sep='')
                    lst_title.append(title)
                    count += 1
    return lst_title 


#Function 7
def get_books_by_publisher(dictionary,publisher):
    """
    author:KATIE STEWART
    Returns a list of books’ titles for the given publisher’s name.
  
    >>>get_books_by_publisher(dictionary,'AMACOM')
    >>>{'Personal Success (The Brian Tracy Success Library)', 'Management (The Brian Tracy Success Library)', 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'Marketing (The Brian Tracy Success Library)', 'Business Strategy (The Brian Tracy Success Library)'}
  
    """    
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])):
            if publisher in (dictionary[category][i]['publisher']):
                z.append(dictionary[category][i])
            
    return z
#Function 8
def check_category_and_title(dictionary,category,title):
    """
    author:Isabella Gonzalo
    Checks if a rate has the specified book.
  
    >>>check_category_and_title(dictionary,Fantasy, We)
    The category Fantasy has the book tile:  ['We']
    >>>check_category_and_title(Fiction, Antiques Roadkill:
       A Trash 'n' Treasures Mystery)
    The category Fiction has the book tile: 
    ["Antiques Roadkill: A Trash 'n' Treasures Mystery"]

    """    
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])):
            dict={category:dictionary[category][i]['title']}
            z.append(dict)
        if {category:title}in z:
                return 'Yes the book is present under given category'
        else:
                return 'Error,please try again.'
    

#Function 9
def all_categories_for_book_title(dictionary,title):
    """
    author:RAUNAK SINGH SOI
    Returns all categories under which the book is listed.
    >>>all_categories_for_book_title(dictionary,"The Malady and Other Stories: An Andrzej Sapkowski Sampler")
    ['Fiction', 'Fantasy', 'Adventure']
    >>>all_categories_for_book_title("Google_Books_Dataset.csv","We")
    ['Fiction', 'Fantasy']
    """    
    z=[]
    for line in dictionary:
        for i in range(len(dictionary[line])):
            if title == (dictionary[line][i]['title']):
                z.append(line)
    
    return z
#FUNCTION 10

def get_books_by_category(category:str, dictionary:dict )->list:
    """
    author:WYLIE SMITH
    """
    lst_titleCat=[]
  
    print('\n', 'The category "' + category + '" contains the following books:')
    count= 1
    for generes in dictionary:
        if category == generes:
            title= dictionary.get(category)
            if title not in lst_titleCat: #to prevent repetition
                print('\t', str(count) , '- ' , title , sep='')
                lst_titleCat.append(title)
                count += 1
    return lst_titleCat     

#Function 11
def get_book_by_category_and_rate(dictionary,category,rating):
    """
    Returns a list of book titles for the given category and rate interval.
    
    >>>get_book_by_category_and_rate('Adventure', 4, 'Google_Books_Dataset.csv')
    >>>['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']

    """
    z=[]
    for line in dictionary:
        for i in range(len(dictionary[line])):
            if category == line and rating in (dictionary[category][i]['rating']):
                z.append(dictionary[category][i]['title'])   
    return z
#Function 12
def get_author_categories(dictionary,author):
    """
    Returns a list of categories for the given author
    
    >>>get_author_categories(dictionary,author)
    The author “Blake Pierce” has published books under the following 
    categories: 
    1- Fiction
    2- Thrillers
    3- Mystery
    4- Detective
    """
    z=[]
    for category in dictionary:
        for i in range(len(dictionary[category])): 
            if author in dictionary[category][i]['author']:
                z.append(category)
    z=set(z)
    for i in range(len(z)):
        i=str(i+1)
    return z
    
