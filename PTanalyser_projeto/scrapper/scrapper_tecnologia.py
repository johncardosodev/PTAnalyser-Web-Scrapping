import os
import requests
from bs4 import BeautifulSoup

#Este é um script para descobrir todas as tecnologias que existem no site para adicionar na base de dados.

PROXY = os.getenv('PROXY') #Este é o proxy que vamos usar para fazer os pedidos
proxies = {
    "http": PROXY,
    "https": PROXY,
}

import requests
def scrape_quotes(url):
    response = requests.get(url, proxies=proxies)
    soup = BeautifulSoup(response.text, features="html.parser")
    
    stack_container = soup.find_all("div", class_="form_field")[3]
    options = stack_container.find_all("option")
    for option in options:
        print(option.text)
    #stack= stack_container.find_all("option")
    #print(stack)


if __name__ == '__main__':
    scrape_quotes("https://pt.teamlyzer.com/companies/")