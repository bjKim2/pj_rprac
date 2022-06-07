import requests
from bs4 import BeautifulSoup

url = 'http://www.cine21.com/search/?q=%EA%B3%B5%EC%A1%B0'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one('#content > div.culm2_area > div.culm2_l > ul.mov_list > li:nth-child(1) > p.name > a')
    print(title)
    ab = title.text
    bc = title.attrs
    print(bc["href"])

    print(bc["href"].split("=")[1])

    
    new_url = "http://www.cine21.com" +bc["href"]
    
else : 
    print(response.status_code)
    

response = requests.get(new_url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    
    title = soup.select_one('#actor_area > ul:nth-child(5) > li:nth-child(1) > img > p.name > a')
    print(title.text)

    
else : 
    print(response.status_code)