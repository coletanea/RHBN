import os
from unidecode import unidecode

def sanitize_string(input_str):
    result = unidecode(input_str).lower()
    result = result.replace(' ', '_')
    result = result.replace("'", "_").replace('"', "_")
    result = result.replace('.', "_")
    result = result.replace(',', '')
    result = result.replace('-', '_')
    return result

main_directory = './pages'

def rename_files(directory):
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            current_path = os.path.join(folder, file)
            file_name, file_extension = os.path.splitext(file)
            new_name = sanitize_string(file_name)
            new_name += file_extension
            new_path = os.path.join(folder, new_name)
            os.rename(current_path, new_path)

    for folder, subfolders, files in os.walk(directory):
        for subfolder in subfolders:
            current_path = os.path.join(folder, subfolder)
            new_name = sanitize_string(subfolder)
            new_path = os.path.join(folder, new_name)
            os.rename(current_path, new_path)

rename_files(main_directory)
