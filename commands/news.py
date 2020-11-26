import json, requests

def get_news():
    import requests            
    
    search_news = input("Enter the keyword for searching news or leave it in blank for default: ")
    limit = input("Introduce the number of news that you want to see (max = 100): ")
    main_url = f"https://newsapi.org/v2/top-headlines?q={search_news}&country=us&apiKey=xxxx"

    if(len(search_news) == 0):
        main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=xxxx"
    else:
        pass

    if(len(limit) == 0):
        limit = 10
    else:
        limit = int(limit)

    # fetching data in json format 
    open_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(0, limit):
          
        try:
            print(i + 1, results[i])
        except IndexError:
            print(f"Whoops, there isn't {limit} about {search_news}, but you have all of this ^^")
            break
  
    #to read the news out loud for us                
  
# Driver Code 
if __name__ == '__main__': 
      
    # function call 
    print(" ")
    print(get_news())  