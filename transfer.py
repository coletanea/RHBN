import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

df = pd.read_csv('./archive.csv')

if not os.path.exists('pages'):
    os.mkdir('pages')

template_path = './pages/template.html'

for index, row in df.iterrows():
    nome = row['Name']
    etiqueta = row['Etiquetas']

    etiqueta_dir = etiqueta.lower().replace(' ', '_') if not pd.isna(etiqueta) else 'nao_etiquetado'

    etiqueta_path = os.path.join('pages', etiqueta_dir)
    if not os.path.exists(etiqueta_path):
        os.mkdir(etiqueta_path)

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

            nome_pagina = nome.lower().replace(' ', '_')

            with open(template_path, 'r', encoding='utf-8') as template_file:
                template = template_file.read()

            template = template.replace('{{titulo}}', nome)
            template = template.replace('{{subtitulo}}', '') 
            template = template.replace('{{autor}}', str(p_autor))

            if div_body:
                conteudo_final = str(div_body)
                template = template.replace('{{conteudo}}', conteudo_final)

                caminho_arquivo = os.path.join(etiqueta_path, f'{nome_pagina}.html')

                with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.write(template)

                print(f'página criada para: {nome} ({etiqueta})')
        else:
            print(f'página não encontrada: {url}')
    else:
        print(f'erro ao tentar acessar: {url}')
