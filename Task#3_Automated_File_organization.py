import os
import shutil

# Define the directory to organize
directory_to_organize = "E:\sample" #here I'm using my this directory you can use the different directory just customize the path

# Define the mapping of file types to folders
file_type_folders = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp'],
    'Archives': ['.zip', '.tar', '.gz', '.rar'],
    'Videos': ['.mp4', '.avi', '.mov', '.mkv'],
}

# Create folders if they don't exist
for folder in file_type_folders:
    folder_path = os.path.join(directory_to_organize, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move files into corresponding folders
for filename in os.listdir(directory_to_organize):
    file_path = os.path.join(directory_to_organize, filename)
    if os.path.isfile(file_path):
        for folder, extensions in file_type_folders.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(directory_to_organize, folder, filename))
                print(f"Moved {filename} to {folder}")
                break

print("File organization completed.")
