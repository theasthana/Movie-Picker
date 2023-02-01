#Creating a web scraper using python and BeautifulSoup.
#This will take the Top 250 Indian movies information from IMDB and create a script to suggest 5 movies randomly.

#Importing modules - BeautifulSoup, Requests, Random
from bs4 import BeautifulSoup
import requests
import random

#Database to stor movie information.
db = [] #It is a 2 dimentional array

try:
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    source = requests.get(url)
    source.raise_for_status()

    #Creating soup
    soup = BeautifulSoup(source.text, "html.parser")

    #fetching movies data and store it in db 'database'
    movies = soup.find("tbody", class_="lister-list").find_all("tr")

    for item in movies:
        name = item.find("td", class_="titleColumn").find("a").text
        rank = int(item.find("td", class_="titleColumn").get_text(strip=True).split(".")[0])
        year = int(item.find("td", class_="titleColumn").find("span").text.strip('()'))
        rating = float(item.find('td',class_="ratingColumn imdbRating").find('strong').text)
        db.append([name,year,rank,rating])
    

    #------------------------------
    #Generating suggestions of movies 
    suggestions = []
    db_len = len(db) - 1

    for i in range(5):
        num = random.randint(0,db_len)
        suggestions.append(db[num])
    
    
    #printing the suggestions
    print("\n\t Movie Picker")
    print("Here is our pick of movies which you can watch today.")
    print("-" * 60)
    print("\t Name \t Rank/Rating")
    print("-" * 60)


    for item in suggestions:
        print(" -> {}({})  ---  {}/{} \n".format(item[0], item[1], item[2], item[3]))
    
    print("-" * 60)
    print("Enjoy:) \n")

except Exception as e:
    print(e)

