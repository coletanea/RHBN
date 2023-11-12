import os
from bs4 import BeautifulSoup

def get_title(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        title_tag = soup.find('title')
        return title_tag.text if title_tag else None

main_directory = './pages/'


html_files = {}

for subdir in os.listdir(main_directory):
    subdir_path = os.path.join(main_directory, subdir)
    if os.path.isdir(subdir_path):
        for file_name in os.listdir(subdir_path):
            if file_name.endswith('.html'):
                file_path = os.path.join(subdir_path, file_name)
                title = get_title(file_path)
                if title:
                    
                    if title in html_files:
                        # Remove o arquivo duplicado
                        os.remove(file_path)
                        print(f"Removido arquivo duplicado: {file_path}")
                    else:
                        # Adiciona o título e o caminho ao dicionário
                        html_files[title] = file_path

# Atualiza as tags <title> nos arquivos HTML restantes
for title, file_path in html_files.items():
    with open(file_path, 'r+', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        title_tag = soup.find('title')
        if title_tag:
            title_tag.string = title
            file.seek(0)
            file.write(str(soup))
            file.truncate()
            print(f"Atualizado título em {file_path}")

print("Concluído.")
