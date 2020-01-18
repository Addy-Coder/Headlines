import requests
from bs4 import BeautifulSoup
import sys


class News:
    def __init__(self, term):
        self.term = term
        self.url = "https://www.ndtv.com/topic/" + self.term

    def headline(self):
        html = requests.get(self.url)
        bsObj = BeautifulSoup(html.content, 'lxml')
        body = bsObj.findAll("p", {"class": ['header', 'fbld']})
        count = 0
        headlines = ''
        headlines_link = ''
        for i in body:
            if count < 5:
                tag = i.findChild()
                headlines_link = tag['href']
                headlines = tag.get_text()
                html2 = requests.get(tag['href'])
                soup = BeautifulSoup(html2.content, 'lxml')
                div = soup.findAll('p')

                count += 1
                print("----------------------------------------------------\n")
                print(headlines+"\n")
                print(div[1].get_text())
                print("\nTo read more please visit the link :\n")
                print(headlines_link)
                print("\n----------------------------------------------------")
            else:
                break
        

#term = sys.argv[1]
term = input("Enter : ")
today_headlines = News(term)
today_headlines.headline()

