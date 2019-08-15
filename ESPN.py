import requests
from bs4 import BeautifulSoup

url = 'http://www.espncricinfo.com/rankings/content/page/211271.html'

def html_parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')
    return soup

table = html_parser(url).find_all('table',class_ = 'StoryengineTable')
div = html_parser(url).find_all('div',class_ = 'ciPhotoContainer')[0].find_all('h3')
print()
for i,r in enumerate(table):
    print(div[i].text,"\n")
    tr = r.find_all('tr')

    i = 0
    for t in tr:
        if i == 0:
            search = 'th'
        else:
            search = 'td'
        for c in t.findChildren(search):
            print("{:20}".format(c.text),end=" ")
        print()
        i += 1
    print("\n\n")
