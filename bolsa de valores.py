import unicodedata
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

with open("dadosteste.txt", "r") as arquivo: 
  dados = arquivo.read()

dados= dados.split()
print(dados)

for i in range(len(dados)):
    link = "https://www.google.com.br/search?q={}".format(dados[i])
    #print(link)

    req = Request(link, headers={
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'
                        'Chrome/81.0.4044.138 Safari/537.36'})

    webpage = urlopen(req).read()
    #print(webpage)
    preco =[]
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html.parser')
        # print(soup)
        for item in soup.find_all('div', attrs={'class': 'wGt0Bc'}):  # dbsr
            valor = (item.find('span', attrs={'class': 'IsqQVc NprOob wT3VGc'}))
            valor = valor.text
            #print(valor)
            preco.append(valor)
print(preco)



























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































