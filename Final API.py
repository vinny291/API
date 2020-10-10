#All imports
import urllib.parse
import xml.etree.ElementTree as ET
import requests

#variables
main_api = "https://www.goodreads.com/search.xml?"
key = "########################" #Replace with your own Goodreads key
titlelist = []
bookidlist = []
authorlist = []
ratinglist = []
counter1 = 0

#User input
while True:
    term = input("What is the title of the book or author: ")
    if term == "quit" or term == "q":
        break

    #using variables to create a URL
    url = main_api + urllib.parse.urlencode({"key":key, "q":term})
    #Use URL to request data
    xml_data = requests.get(url)
    #structure xml_data
    root = ET.fromstring(xml_data.content)
    
    #Search the authors/title/bookid/rating of a book added to a list to display later 
    for titlebook in root.findall('./search/results/work/best_book/title'):
        titlelist.append(titlebook.text)

    for bookid in root.findall("./search/results/work/best_book/id"):
        bookidlist.append(bookid.text)

    for author in root.findall('./search/results/work/best_book/author/name'):
        authorlist.append(author.text)

    for rating in root.findall('./search/results/work/average_rating'):
        ratinglist.append(rating.text)
    
    #Display data from list whit invalid input catch
    if not authorlist:
        print("Dit is een ongeldige string")
    else:
        for x in bookidlist:
            print("Match:"+ str(counter1+1))
            print("===============BookID:" + bookidlist[counter1] + "==============")
            print("author: " + authorlist[counter1])
            print("Titel: " + titlelist[counter1])
            print("Rating: " + ratinglist[counter1])
            print("===================================="+ "="*len(bookidlist[counter1]))
            print("\n")
            counter1 += 1