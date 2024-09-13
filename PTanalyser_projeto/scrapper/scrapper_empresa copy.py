import os
import requests
from bs4 import BeautifulSoup

PROXY = os.getenv('PROXY') #Este é o proxy que vamos usar para fazer os pedidos
proxies = {
    "http": PROXY,
    "https": PROXY,
}

def scrape_empresa(url):
    response = requests.get(url, proxies=proxies) #Aqui estamos a fazer o pedido à página
    soup= BeautifulSoup(response.text, "html.parser") #Aqui estamos a criar um objeto BeautifulSoup
    #print(soup)
    info_total = soup.select('div.col-lg-8:not(.ethical_ad)') #Seleccao de todas as divs com a classe col-lg-8 e que não tenham a classe ethical_ad
    
    #print(nome_empresa(info_total))
    #descricao(info_total)  
    #rating(info_total)
    #print(tx_recomendacao(info_total))
    #print(salario_medio(info_total))
    #print(horas_trabalho(info_total))
    #dificuldade_entrevista(info_total)
    #tx_feedback(info_total)
    #industria(info_total)
    #trabalhadores(info_total)
    #print(website(info_total)) 
    #tecnologias(soup)
   

######################################## info inicial da empresa #########################################################################
def nome_empresa(info_total):
    nome_empresa=info_total[0].find("h1", class_="reduce-h1 text-default-xs").text.strip() #Encontramos aqui o nome da empresa
    return nome_empresa

def industria(info_total):
    industria=info_total[0].find_all("div", class_="center_mobile hidden-xs company_add_details")[0].text.strip().splitlines()
    #Encontramos aqui a industria da empresa e dividimos usando "line" como separador     
    return industria[0]

def trabalhadores(info_total):
    industria=info_total[0].find_all("div", class_="center_mobile hidden-xs company_add_details")[0].text.strip().splitlines()
    #Encontramos aqui a industria da empresa e dividimos usando "line" como separador     
    return industria[2]

def website(info_total):
    allUrls=info_total[0].find_all("div", class_="center_mobile hidden-xs company_add_details") #Aqui estamos a encontrar todas as divs com a classe center_mobile
    urls=allUrls[0].find_all('a', href=lambda href: href and '.com' in href) #Aqui estamos a encontrar todas as tags a que tenham .com no href 
    for url_tag in urls: #Aqui estamos a iterar sobre todas as tags a que encontramos 
        url = url_tag['href'] #Aqui estamos a obter o valor do atributo href
    return url

def descricao(info_total):
    descricao=info_total[0].find("div", class_="ellipsis center_mobile").text.strip() #Encontramos aqui a descricao da empresa
    return descricao

def rating(info_total):
    rating=info_total[0].select("div.text-center") #Aqui estamos a encontrar todas as divs com a classe text-center
    
    #Aqui estamos a dividir a string em duas partes, usando " / " como separador e a 
    #ficar com a primeira parte     
    rating=rating[0].text.strip().split("/", 1)[0] 
    return rating

#################################### Tecnologia ##################################################################################################
def tecnologias(soup):
    #find in info_total the dive in tags voffset2 tags_popover
    tag_container=soup.find("div", class_="wrapper-tags-reviews-answered-rate") #Aqui estamos a encontrar todas as divs com a classe voffset2 e tags_popover
    # Find all <a> tags within the <div> with class "tags voffset2 tags_popover"
    tag_div = tag_container.find('div', class_='tags voffset2 tags_popover')
    tag_links = tag_div.find_all('a')

    # Extract tag names and URLs
    tag_info = [(link.text, link['href']) for link in tag_links]

    # Extract tags from the button's data-content attribute
    button_content = soup.find('button', class_='btn btn-link button_plus')['data-content']
    button_soup = BeautifulSoup(button_content, 'html.parser')
    additional_tags = button_soup.find_all('a')

    # Add additional tags to tag_info list
    tag_info += [(tag.text, tag['href']) for tag in additional_tags]

    # Print tag names and URLs
    tag=[]
    for name in tag_info:
        tag.append(name[0])
    return tag
################################### Reviews de funcionários e candidatos #########################################################################
def tx_recomendacao(info_total):
    tx_recomendacao=info_total[0].find_all("p", class_="size-h2")[0].text.strip() #Encontramos aqui a taxa de recomendacao da empresa
    return tx_recomendacao


def salario_medio(info_total):
    salario_medio=info_total[0].find_all("p", class_="size-h2")[1].text.strip() #Encontramos aqui o salario medio da empresa
    return salario_medio

def horas_trabalho(info_total):
    horas_trabalho=info_total[0].find_all("p", class_="size-h2")[2].text.strip() #Encontramos aqui o horas medio da empresa
    return horas_trabalho

def dificuldade_entrevista(info_total):
    dificuldade_entrevista=info_total[0].find_all("p", class_="size-h2")[3].text.strip().split("/", 1)[0]  #Encontramos aqui a dificuldade da entrevista da empresa
    return dificuldade_entrevista

def tx_feedback(info_total):
    tx_feedback=info_total[0].find_all("p", class_="size-h2")[4].text.strip() #Encontramos aqui a taxa de feedback da empresa
    return tx_feedback

def investimento_tempo(info_total):
    investimento_tempo=info_total[0].find_all("p", class_="size-h2")[5].text.strip() #Encontramos aqui o investimento de tempo da empresa
    return investimento_tempo

if __name__ == '__main__':
    scrape_empresa("https://pt.teamlyzer.com/companies/axians-portugal")