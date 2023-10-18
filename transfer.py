import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

df = pd.read_csv('./archive.csv')

for index, row in df.iterrows():
    nome = row['Name']
    url = row['URL']
    response = requests.get(url)

    if response.status_code == 200:
        
        conteudo_html = response.text
  
        soup = BeautifulSoup(conteudo_html, 'html.parser')
        
        div_artigo = soup.find('div', {'class': 'grid_3', 'id': 'article-full'})

        if div_artigo:
            
            h1_tags = div_artigo.find_all('h1')
            h2_tags = div_artigo.find_all('h2')
            p_autor = div_artigo.find('p', {'id': 'autor'})
            div_body = div_artigo.find('div', {'id': 'body', 'class': 'text'})

            
            conteudo_final = f"<title>{nome}</title>"
            
            for h1_tag in h1_tags:
                conteudo_final += str(h1_tag)
            
            for h2_tag in h2_tags:
                conteudo_final += str(h2_tag)
            
            if p_autor:
                conteudo_final += str(p_autor)
            
            if div_body:
                conteudo_final += str(div_body)

            conteudo_final += "</body></html>"
            
            with open(f'{nome}.html', 'w', encoding='utf-8') as arquivo:
                arquivo.write(conteudo_final)

            print(f'página criada para: {nome}')
        else:
            print(f'página não encontrada: {url}')
    else:
        print(f'erro ao tentar acessar: {url}')
