import requests
from bs4 import BeautifulSoup
import re

regex = r'<a href="(.+?)"\s+title="(.+?)">'

url = "https://www.infomoney.com.br/?infinity=scrolling"

payload={'page': '1',
'currentday': '22.03.23',
'order': 'DESC',
'scripts[0]': 'jquery',
'scripts[1]': 'jquery-core',
'query_args[pagename]': 'ultimas-noticias',
'query_args[post_type][0]': 'guide',
'query_args[post_type][1]': 'post',
'query_args[posts_per_page]': '10',
'query_args[post_type][2]': 'page',
'query_args[post_type][3]': 'colunistas',
'query_args[post_type][4]': 'patrocinados',
'query_args[post_type][5]': 'especiais',
'query_before': '2023-03-22 20:38:02',
'last_post_date': '2023-03-22 18:17:24',
'query_args[post_type][6]': 'web-story'}


response = requests.request("POST", url, data=payload)
json = response.json()
soup = BeautifulSoup(json["html"], "html.parser")

news_items = soup.find_all("div", class_="row py-3 item")

for i, item in enumerate(news_items):
    # Extrai o título da notícia
    sub_item = str(item.find("a"))
    print(i)

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
