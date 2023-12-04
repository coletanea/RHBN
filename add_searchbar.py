import os
from bs4 import BeautifulSoup

# Diretório principal
base_directory = "./pages"

# Código HTML da barra de pesquisa
searchbar_html = """
<section id="searchContainer" style="margin-top: 10px;">
    <div id="search">
        <input type="text" id="searchInput" placeholder="Digite a palavra a ser encontrada" class="blinking-cursor">
        <div>
            <button onclick="search()">Buscar</button>
            <button id="clear">Limpar</button>
        </div>
    </div>
    <div id="searchResults"></div>
</section>
"""

# Link para o CSS externo
css_link = '<link rel="stylesheet" href="../../styles/general.css">'

# Link para o script JS
js_script_link = '<script src="../../js/searchbar.js"></script>'

# Lista de subdiretórios
subdirectories = [
                   "nao_etiquetado",
                "educacao",
                "homossexualidades",
                "conjuracao_baiana",
                "mulheres_em_conflitos",
                "fim_da_guerra",
                "comida_e_modos_de_comer",
                "redemocratizacao",
                "feminismos",
                "antonio_vieira",
                "canudos",
                "drogas",
                "getulio_vargas",
                "trafico_de_escravos",
                "leopoldina",
                "primeira_guerra_mundial",
                "contestado",
                "descobrimentos",
                "o_golpe_de_1964",
                "o_golpe_de_1965",
                "o_golpe_de_1966",
                "o_golpe_de_1967",
                "revolucao_de_1932",
                "revolucao_de_1933",
                "revolucao_de_1934",
                "jesuitas",
                "princesa_isabel",
                "africa_brasil",
                "astrologia",
                "d_pedro_i",
                "italianos_do_brasil",
                "arqueologia",
                "batalhas",
                "sociedades_secretas",
                "fora_da_lei",
                "o_negocio_da_inconfidencia",
                "brasil_e_estados_unidos",
                "amantes",
                "profecias",
                "integralismo",
                "animais_de_estimacao",
                "atentados_politicos",
                "judeus",
                "cafe",
                "feiticaria",
                "napoleao",
                "escravidao",
                "republica",
                "franca",
                "independencia",
                "euclides_da_cunha",
                "arabes_no_brasil"
]

# Função para adicionar a barra de pesquisa ao arquivo HTML
def add_searchbar_to_html(file_path):
    # Verifica se o arquivo existe antes de tentar abri-lo
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

            # Verifica se a barra de pesquisa já foi adicionada
            if '<section id="searchContainer">' not in content:
                soup = BeautifulSoup(content, "html.parser")

                # Adiciona o link para o CSS externo na tag head
                head_tag = soup.head
                head_tag.insert(0, BeautifulSoup(css_link, "html.parser"))

                body_tag = soup.body

                # Adiciona a barra de pesquisa ao início do corpo do HTML
                body_tag.insert(0, BeautifulSoup(searchbar_html, "html.parser"))

                # Adiciona o link para o script JS antes do fechamento da tag </body>
                body_tag.append(BeautifulSoup(js_script_link, "html.parser"))

                # Salva as alterações no arquivo
                with open(file_path, "w", encoding="utf-8") as modified_file:
                    modified_file.write(str(soup))

# Itera sobre os subdiretórios
for subdir in subdirectories:
    subdir_path = os.path.join(base_directory, subdir)

    # Verifica se é um diretório
    if os.path.isdir(subdir_path):
        index_file_path = os.path.join(subdir_path, "index.html")
        
        # Verifica se o arquivo "index.html" existe no subdiretório
        if os.path.exists(index_file_path):
            # Adiciona a barra de pesquisa e os links ao arquivo "index.html"
            add_searchbar_to_html(index_file_path)

print("Automatização concluída com sucesso.")