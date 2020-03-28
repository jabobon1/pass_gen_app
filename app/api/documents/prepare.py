import requests
from bs4 import BeautifulSoup

# link = 'http://wordsteps.com/vocabulary/words/136958/8000+Основных+английских+слов'
#
# r = requests
# res = r.get(link)

with open('words.html', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

words = soup.find_all('td', {'class': 'cword en'})
results = [i.text.strip() for i in words]
