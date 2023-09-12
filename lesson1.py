from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.bbc.com/news')

soup = BeautifulSoup(response.content, 'html.parser')

h2_elements = soup.find_all('h2')

for h2_element in h2_elements:
    print(h2_element.get_text()) 