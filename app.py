import os
import shutil
from tqdm import tqdm
from tkinter import Tk, filedialog

def select_directory():
    Tk().withdraw()
    directory = filedialog.askdirectory()
    return directory

def scan_directories(base_path, search_terms):
    matching_dirs = []
    for root, dirs, files in tqdm(os.walk(base_path), desc="Scanning directories"):
        for dir_name in dirs:
            if any(term.lower() in dir_name.lower() for term in search_terms):
                matching_dirs.append(os.path.join(root, dir_name))
    return matching_dirs

def delete_directories(directories):
    for dir_path in tqdm(directories, desc="Deleting directories"):
        shutil.rmtree(dir_path)

def get_search_terms(option):
    file_map = {
        '1': 'unity-file-list.txt',
        '2': 'unreal-file-list.txt',
        '3': 'godot-file-list.txt'
    }
    file_path = file_map.get(option)
    if not file_path or not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    print("Select the base directory for the cleanup operation:")
    base_directory = select_directory()
    
    if not base_directory:
        print("No directory selected. Exiting.")
        return
    
    print("Choose the type of project to clean:")
    print("1. Unity")
    print("2. Unreal")
    print("3. Godot")
    option = input("Enter the number corresponding to your choice: ").strip()
    
    search_terms = get_search_terms(option)
    if not search_terms:
        print("Invalid option or no search terms found. Exiting.")
        return
    
    matching_dirs = scan_directories(base_directory, search_terms)
    
    if not matching_dirs:
        print("No directories found matching the search terms.")
        return
    
    print("The following directories match your search terms:")
    for dir_path in matching_dirs:
        print(dir_path)
    
    confirm = input("Do you want to delete these directories? (y/n): ").strip().lower()
    
    if confirm == 'y':
        delete_directories(matching_dirs)
        print("Directories deleted successfully.")
    else:
        print("Operation canceled.")

if __name__ == "__main__":
    main()
