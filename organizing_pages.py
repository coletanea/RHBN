import os
from bs4 import BeautifulSoup

# Diretório principal
main_directory = './pages/'

# Percorre os arquivos HTML dentro do diretório principal
for subdir, dirs, files in os.walk(main_directory):
    for file_name in files:
        if file_name.endswith('.html'):
            file_path = os.path.join(subdir, file_name)

            with open(file_path, 'r+', encoding='utf-8') as file:
                content = file.read()
                soup = BeautifulSoup(content, 'html.parser')

                # Encontra a tag <h1> e obtém o texto
                h1_tag = soup.find('h1')
                if h1_tag:
                    h1_text = h1_tag.get_text(strip=True)

                    # Atualiza a tag <title> com o conteúdo da tag <h1>
                    title_tag = soup.find('title')
                    if title_tag:
                        title_tag.string = h1_text
                        file.seek(0)
                        file.write(str(soup))
                        file.truncate()
                        print(f"Atualizado título em {file_path}")
                    else:
                        print(f"Tag <title> não encontrada em {file_path}")
                else:
                    print(f"Tag <h1> não encontrada em {file_path}")

print("Concluído.")
