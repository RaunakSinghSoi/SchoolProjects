#Date:9/12/2021
#version: Version 1.0
#T085:Raunak,Wylie,Isabella,Katie
#Case1:Wylie
#Case2:Katie
#Case3:Isabella
#Case4:Raunak
#Refactored by :Raunak
#Quit function:Raunak
#execute(command):Raunak
#edited by Raunak
go_ahead_get=['g','G']#command to keep interface  going
keys_get= ['P','R','CR','A','C','CT']#valid keys.
go_ahead=['s','S']#command to keep interface  going
keys= ['P','R','PA','C','T']#valid keys.
list_ok=['l','L','a','A','r','R','f','F','nc','NC','CA','ca','cb','CB','s','S','g','G']

from T085_load_data import load_dataset

print('Command Line L)oad file','\nCommand Line A)dd book','\nCommand Line R)emove book','\nCommand Line F)ind book by title','\nCommand Line NC) Number of books in a category','\nCommand Line CA) Categories for an author','\nCommand Line CB) Categories for a book title','\nCommand Line G)et book','\n\tR)ate','A)uthor','P)ublisher','C)ategory','CT) Category and Title','CR) Category and Rate','\nCommand Line S)ort book' ,'\n\tT)itle','R)ate','P)ublisher','C)ategory','PA)ageCount','\nCommand line Q)uit')
dictloaded = False
count = 1
def case1(command:str):
 
 """
 Author:Wylie Smith
 Returns the requested action,hfor loaded file.
 >>>: l
What file do you wish to load?Google_Books_Dataset.csv
This dictionary has succesfully been loaded!
 """
 if command == 'L' :
  load_dict = input('What file do you wish to load?')
  current_dictionary = load_dataset(load_dict)
  return 'This dictionary has succesfully been loaded!'
def misc(ok):
  if ok == 'A':
   add_dict = input('What book info would you like to add?:')
   add_book(dictionary, add_dict)
   return 'The book info has been added!'
       
  if ok == 'R':
   if __name__ == "__main__":
    import T085_P2_search_modify_dataset 
    book = input('What book would you like to find?:')
    category = input('What category is this book in?:')
    return T085_P2_search_modify_dataset.rremove_book(book,category)
      
                  
       
  if ok == 'F':
   if __name__ == "__main__":
    import T085_P2_search_modify_dataset 
    dictionary=load_dataset('Google_Books_Dataset.csv')   
    title = input('What book would you like to find?:')
    return T085_P2_search_modify_dataset.find_book(dictionary, title)
       
       
  if command == 'Q':
       count = 0
       
       

#Raunak
def sort(key):
    """
 Author:Raunak Singh Soi
 Returns a sorted list for given key with book data as elements.
 >>>Enter key to sort dictionary: P
 [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': '112', 'language': 'English', 'generes': 'Economics'} .....etc 
    """ 
    if key=='P':
        if __name__ == "__main__":
            from T085_load_data import load_dataset
            import T085_P3_sorting
            dictionary=load_dataset('Google_Books_Dataset.csv')
            return T085_P3_sorting.sort_books_publisher(dictionary)
    if key=='T':
        if __name__ == "__main__":
            from T085_load_data import load_dataset
            import T085_P3_sorting 
            dictionary=load_dataset('Google_Books_Dataset.csv')
            return T085_P3_sorting.sort_books_title(dictionary) 
    if key=='R':
        if __name__ == "__main__":
            from T085_load_data import load_dataset
            import T085_P3_sorting 
            dictionary=load_dataset('Google_Books_Dataset.csv')
            return T085_P3_sorting.sort_books_ascending_rate(dictionary)   
    if key=='PA':
        if __name__ == "__main__":
            from T085_load_data import load_dataset
            import T085_P3_sorting 
            dictionary=load_dataset('Google_Books_Dataset.csv')
            return T085_P3_sorting.sort_books_pageCount(dictionary)   
    if key=='C':
        if __name__ == "__main__":
            from T085_load_data import load_dataset
            import T085_P3_sorting 
            dictionary=load_dataset('Google_Books_Dataset.csv')
            return T085_P3_sorting.sort_books_category(dictionary)
def case2(ok):
 """
 Author:Katie Stewart
 Returns book based on requested input.
 """ 
 if ok == 'NC':
  return 3
  
     
    
     
 if ok == 'CA':
  if __name__ == "__main__":
   import  T085_P2_search_modify_dataset 
   dictionary=load_dataset('Google_Books_Dataset.csv')
   author = input("What author would you like to investigate:")
   return T085_P2_search_modify_dataset.get_author_categories(dictionary,author)
         
     
    
     
 if ok == 'CB':
  if __name__ == "__main__":
   import  T085_P2_search_modify_dataset 
   dictionary=load_dataset('Google_Books_Dataset.csv')
   title = input("What title would you like to investigate: ")
   return T085_P2_search_modify_dataset.all_categories_for_book_title(dictionary,title)  
        
 
 
    
#Isabella
def get(key):
  """Returns a book list of the desired book data
 
  >>> :G
  Enter Command: CR
  Category: Fantasy
  Rate: 4
  ['The Malady and Other Stories: An Andrzej Sapkowski Sampler',
  'The Name of the Wind: The Kingkiller Chronicle:, Book 1',
  'Mistborn Trilogy: The Final Empire, The Well of Ascension,
  The Hero of Ages', 'A Feast for Crows (A Song of Ice and Fire, Book 4)',
  'The Tower of the Swallow: Witcher 6', 'A Game of Thrones:
  The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings,
  A Storm of Swords, A Feast for Crows, A Dance with Dragons
  (A Song of Ice and Fire)', 'The Way Of Shadows: Book 1 of the Night Angel',
  'The Lord of the Rings: The Fellowship of the Ring, The Two Towers,
  The Return of the King', 'The Weight of Honor (Kings and Sorcerers--Book 3)',
  'Night of the Bold (Kings and Sorcerers--Book 6)',
  'The Vagrant (The Vagrant Trilogy)', 'We',
  'Prince of Thorns (The Broken Empire, Book 1)',
  "Chronicle of the Unhewn Throne: (The Emperor's Blades,
  The Providence of Fire, The Last Mortal Bond)",
  'The Painted Man (The Demon Cycle, Book 1)']

  >>> :G
  Enter Command: P
  Publisher: Penguin
  {'The Magic of Thinking Big', 'Getting Things Done: The Art of
  Stress-Free Productivity', 'The Infinite Game', 'Boy Erased: A Memoir',
  'No One Is Too Small to Make a Difference'}

  >>> :G
  Enter Command: A
  Author: Barbara Allan
  The author "Barbara Allan" has written the following books:
        1- Antiques Roadkill: A Trash 'n' Treasures Mystery
        2- Antiques Con
        3- Antiques Chop
        4- Antiques Knock-Off
       
  """
 
  #Gets function for get book by rate
  if key == 'R':
    if __name__ == "__main__":
      import T085_P2_search_modify_dataset
      from T085_load_data import load_dataset
      dictionary=load_dataset('Google_Books_Dataset.csv')
      rating=input("Desired Rating: ")
      return T085_P2_search_modify_dataset.get_rate(dictionary,rating)
     
  #Gets function for get book by author   
  if key == 'A':
    if __name__ == "__main__":
      import T085_P2_search_modify_dataset
      from T085_load_data import load_dataset
      dictionary=load_dataset('Google_Books_Dataset.csv')
      author=input('a: ')
      return T085_P2_search_modify_dataset.get_books_by_author(author,dictionary)            
 
  #Gets function for get book by publisher       
  if key == 'P':
    if __name__ == "__main__":
      from T085_load_data import load_dataset
      import T085_P2_search_modify_dataset
      publisher = input('Publisher: ')
      dictionary =load_dataset('Google_Books_Dataset.csv')
      return T085_P2_search_modify_dataset.get_books_by_publisher(dictionary,publisher) 
 
  #Gets function for get book by category     
  if key == 'C':
    if __name__ == "__main__":
      from T085_P2_search_modify_dataset import load_dataset
      import T085_P2_search_modify_dataset
      category = input('Category: ')
      dictionary = load_dataset('Google_Books_Dataset.csv') 
      return T085_P2_search_modify_dataset.get_books_by_category(category,dictionary)
 
  #Gets function for get book by category and title   
  if key == 'CT':
    if __name__ == "__main__":
      from T085_load_data import load_dataset
      import T085_P2_search_modify_dataset
      category = input('Category: ')
      title = input('Title: ')
      dictionary = load_dataset('Google_Books_Dataset.csv') 
      return T085_P2_search_modify_dataset.check_category_and_title(dictionary,category,title)
       
  #Gets function for get book by category and rate          
  if key == 'CR':
    if __name__ == "__main__":
      from T085_load_data import load_dataset
      import T085_P2_search_modify_dataset
      category = input('Category: ')
      rating = input('Rate: ')
      dictionary = load_dataset('Google_Books_Dataset.csv') 
      return T085_P2_search_modify_dataset.get_book_by_category_and_rate(dictionary,category,rating)              

 
def execute(command):
   """
   Author:Raunak Singh Soi
   Runs respective code for given command.
   """
   if command!='L':
    return '"No file loaded"' 
   while command=='L':
     print(case1(command))
     break
   ok=input(': ').upper()
   if ok =='A':
      return misc(ok)
   if ok =='F':
      return misc(ok)   
   if ok =='R':
      return misc(ok)
   if ok == 'CA':
      return case2(ok)         
   if ok == 'CB':
      return case2(ok)         
   if ok == 'NC':
      return case2(ok)    
   if ok =='S':
        key = input("Enter key to sort books: ")
        if key in keys:
            return sort(key)
        elif key not in keys:
         return 'No such key,Please try again'
        
   if ok =='G':
        key = input("Enter key to get books: ")
        if key in keys_get:
            return get(key)
        elif key not in keys_get:
         return 'No such key,Please try again'
         
     
          
     
     
     
     
#Raunak
command=input(": ").upper()#initial command
if command not in list_ok:
    print('"No such command"')
    
while command.upper() !='Q' and command.upper() in list_ok :#loop to keep interface going
     print(execute(command))
     print('Command Line L)oad file','\nCommand Line A)dd book','\nCommand Line R)emove book','\nCommand Line F)ind book by title','\nCommand Line NC) Number of books in a category','\nCommand Line CA) Categories for an author','\nCommand Line CB) Categories for a book title','\nCommand Line G)et book','\n\tR)ate','A)uthor','P)ublisher','C)ategory','CT) Category and Title','CR) Category and Rate','\nCommand Line S)ort book' ,'\n\tT)itle','R)ate','P)ublisher','C)ategory','PA)ageCount','\nCommand line Q)uit')
     command=input(": ").upper()
while command.upper()=='Q':#quits the loop
    break
while command!='Q' and command in list_ok:#keeps interface going
   print(execute(command))
         
         
         
     
     
     
     
     

