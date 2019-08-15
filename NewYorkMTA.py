import requests
from bs4 import BeautifulSoup
import csv
url = "http://web.mta.info/developers/turnstile.html"

def html_parser(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    return soup
anchor = html_parser(url).find('div',class_ = "span-84 last").find_all('a')

# Saving data into the csv file

filname = open('NY MTA.csv','w+',newline='',encoding='utf-8')
try:
    writer = csv.writer(filname)
    writer.writerow(("Date","Links"))
    for i in anchor:
        hr = i['href']
        uri = 'http://web.mta.info/developers/' + hr
        writer.writerow((i.text,uri))
except IOError as e:
    print(e)
else:
    print('Congratulations ! NewYork MTA has been scrapped in NY MTA sucessfully...')
finally:
    filname.close()