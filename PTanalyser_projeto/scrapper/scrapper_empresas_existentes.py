import requests
from bs4 import BeautifulSoup

with open('companies.txt', 'a', encoding="utf-8") as f:

#Este loop irá correr todas as empresas existentes da pagina 1 a 756.
#Assim descobrimos o index de cada empresa no site ptAnalyser para percorrar depois toda a informaçao 
    for i in range(1, 756):
        URL = "https://pt.teamlyzer.com/companies/?page=" + str(i)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        result= soup.find_all("h3", class_="voffset0")
        for r in result:
            #add the company name and the company link to a file
            f.write(r.a.get_text() + " - " + r.a['href'] + "\n")
            #print(r.a.get_text())
            #print(r.a['href'])
f.close()

