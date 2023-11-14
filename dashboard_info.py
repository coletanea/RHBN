import os

base_directory = "./pages"
subdirectories = [d for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]
tag_count = len(subdirectories)

total_article_count = 0

for subdirectory in subdirectories:
    article_count = len([f for f in os.listdir(os.path.join(base_directory, subdirectory)) if f.endswith(".html") and f.lower() != "index.html"])
    total_article_count += article_count

print(f"contagem de subdiretórios: {tag_count}")
print(f"contagem total de artigos: {total_article_count}")
