from unidecode import unidecode


import os
from unidecode import unidecode

def sanitize_string(input_str):
    return unidecode(input_str).lower().replace(' ', '_').replace("'", "_").replace('"', "_").replace('.', "_")

# Main directory where the files are located
main_directory = './pages'

def rename_files(directory):
    for folder, subfolders, files in os.walk(directory):
        for file in files:
            current_path = os.path.join(folder, file)
            file_name, file_extension = os.path.splitext(file)

            # Create a new name without special characters
            new_name = sanitize_string(file_name)

            # Add the extension back
            new_name += file_extension

            # Create the new file path
            new_path = os.path.join(folder, new_name)

            # Rename the file
            os.rename(current_path, new_path)

    # Rename folders
    for folder, subfolders, files in os.walk(directory):
        for subfolder in subfolders:
            current_path = os.path.join(folder, subfolder)

            # Create a new folder name without special characters
            new_name = sanitize_string(subfolder)

            # Create the new folder path
            new_path = os.path.join(folder, new_name)

            # Rename the folder
            os.rename(current_path, new_path)

rename_files(main_directory)
