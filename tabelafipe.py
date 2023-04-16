# imports

import requests
from bs4 import BeautifulSoup


url = 'https://tabelafipecarros.com.br/veiculo/7692/25/Honda/Civic/Civic+Sedan+EX+2.0+Flex+16V+Aut.4p/2017/Flex?utm_source=Carro&utm_medium=undefined&utm_campaign=ORGANIC'

#my user agente

headers = {'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser') # parser é o analizador do conteudo do site
honda = soup.find_all('div', class_='col-12 col-md-6')

civic = honda[0]

marca = civic.find('h1', class_='h2 title mb-3 pt-0').get_text().strip()
preco = civic.find_all('h2', class_=' d-none d-md-block Valor_Veiculo p price mb-0')
#teste = soup.find_all('h2' , class_='d-none d-md-block Valor_Veiculo p price mb-0')


print(preco)

 