import requests
from bs4 import BeautifulSoup


url = 'https://www.chavesnamao.com.br/tabela-fipe/honda-civic-sedan-ex-2.0-flex-16v-aut.4p/2017/codigo-fipe-014091-0/'

#my user agente

headers = {'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser') # parser é o analizador do conteudo do site
honda = soup.find_all('section', class_='result')

civic = honda[0]

marca = civic.find('di', class_='heading').get_text().strip()
preco = civic.find_all('h2', class_='d-block d-md-none Valor_Veiculo p price mb-4 mt-4 text-center ' )



print(marca)