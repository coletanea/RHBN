import os
from bs4 import BeautifulSoup
from unidecode import unidecode

main_directory = './pages'


def sanitize_string(input_str):
    result = unidecode(input_str).lower()
    result = result.replace(' ', '_')
    result = result.replace("'", "_").replace('"', "_")
    result = result.replace('?', "")
    result = result.replace(',', '')
    result = result.replace('-', '_')
    return result

def process_body_links(body_content, subdir):
    soup = BeautifulSoup(body_content, 'html.parser')

    # Update href attributes in <a> tags within <body>
    for a_tag in soup.find_all('a', href=True):
        old_href = a_tag['href']
        file_name, _ = os.path.splitext(old_href)
        new_href = f"./{sanitize_string(file_name)}.html"
        a_tag['href'] = new_href

    return str(soup)

def process_index_html(index_path, subdir):
    with open(index_path, 'r', encoding='utf-8') as index_file:
        index_content = index_file.read()

    # Find and modify links within <body>
    body_start = index_content.find('<body>')
    body_end = index_content.find('</body>') + len('</body>')
    if body_start != -1 and body_end != -1:
        body_content = index_content[body_start:body_end]
        modified_body = process_body_links(body_content, subdir)
        index_content = index_content.replace(body_content, modified_body)

        # Save the modified content back to the file
        with open(index_path, 'w', encoding='utf-8') as index_file:
            index_file.write(index_content)

def process_classification_directories(directory):
    for subdir, _, files in os.walk(directory):
        for file in files:
            if file == 'index.html':
                index_path = os.path.join(subdir, file)
                process_index_html(index_path, subdir)

# Process classification directories
process_classification_directories(main_directory)