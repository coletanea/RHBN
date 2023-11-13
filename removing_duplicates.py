import os
from bs4 import BeautifulSoup

main_directory = './pages/'

for subdir, _, files in os.walk(main_directory):
    for file in [f for f in files if f == 'index.html']:
        index_path = os.path.join(subdir, file)
        
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
            soup = BeautifulSoup(content, 'html.parser')
            
            unique_links = set()
            for li in soup.find_all('li'):
                link = li.find('a')
                if link:
                    href = link.get('href')
                    if href not in unique_links:
                        unique_links.add(href)
                    else:
                        li.decompose()

            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))

print("Concluído.")
