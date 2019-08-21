import requests 
from bs4 import BeautifulSoup

url = "https://thuoctienloi.vn/"
req_url = requests.get(url, timeout=20, stream=True)
soup = BeautifulSoup(req_url.text, 'html.parser')

header_menu = soup.find("div", "header-menu")
main_menu_drug = header_menu.div.div.find("div", "grid-col md-25")