import urllib;
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as soup


url = urlopen('https://www.remitly.com/us/en/india')
page_html = url.read()

req_url= requests.get('https://www.remitly.com/us/en/india')

# print(req_url.text)
url.close()

page_soup = soup(page_html,'html.parser')

info_tag = page_soup.find_all('sup', attrs={'class':'f1sp9y5j'})
price = page_soup.find_all('h2',attrs= {'class':'fheif50'})

data_tag = page_soup.find_all('td', attrs= {'class':'f1smo2ix'})
print(price)
print(info_tag)
print(data_tag)
# print(page_soup)

