import requests
from bs4 import BeautifulSoup
import re

url = "https://www.infomoney.com.br/ultimas-noticias/"
regex = r'<a href="(.+?)"\s+title="(.+?)">'

# Faz a requisição HTTP GET à página da InfoMoney
response = requests.get(url)

# Analisa o conteúdo HTML retornado
soup = BeautifulSoup(response.text, "html.parser")

# Encontra todos os elementos HTML que contêm as notícias
news_items = soup.find_all("div", class_="row py-3 item")

# Percorre os elementos HTML e extrai os títulos e links das notícias
for item in news_items:
    # Extrai o título da notícia
    sub_item = str(item.find("a"))

    match = re.search(regex, sub_item)

    if match:
        # obter o valor do href
        href = match.group(1)
        print(f'href: {href}')

        # obter o valor do title
        title = match.group(2)
        print(f'title: {title}')
    else:
        print('Não foi encontrado nenhum match')

    print("-"*50)
