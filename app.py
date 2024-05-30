import os
import shutil
from tqdm import tqdm
from tkinter import Tk, filedialog

def select_directory():
    Tk().withdraw()
    directory = filedialog.askdirectory()
    return directory

def scan_directories(base_path, search_terms, ignore_terms):
    matching_dirs = []
    for root, dirs, files in tqdm(os.walk(base_path), desc="Scanning directories"):
        dirs[:] = [d for d in dirs if d not in ignore_terms]  # Modify dirs in-place to skip ignored directories
        for dir_name in dirs:
            if any(term.lower() == dir_name.lower() for term in search_terms):
                matching_dirs.append(os.path.join(root, dir_name))
    return matching_dirs

def delete_directories(directories):
    for dir_path in tqdm(directories, desc="Deleting directories"):
        shutil.rmtree(dir_path)

def get_terms(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]

def filter_top_level_directories(directories):
    directories = sorted(directories, key=len)  # Sort directories by length
    filtered_dirs = []
    for dir_path in directories:
        if not any(dir_path.startswith(existing_dir + os.sep) for existing_dir in filtered_dirs):
            filtered_dirs.append(dir_path)
    return filtered_dirs

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
    
    file_map = {
        '1': ('unity-file-list.txt', 'unity-ignore-list.txt'),
        '2': ('unreal-file-list.txt', 'unreal-ignore-list.txt'),
        '3': ('godot-file-list.txt', 'godot-ignore-list.txt')
    }
    
    if option not in file_map:
        print("Invalid option. Exiting.")
        return
    
    search_file, ignore_file = file_map[option]
    search_terms = get_terms(search_file)
    ignore_terms = get_terms(ignore_file)
    
    if not search_terms:
        print("No search terms found. Exiting.")
        return
    
    matching_dirs = scan_directories(base_directory, search_terms, ignore_terms)
    matching_dirs = filter_top_level_directories(matching_dirs)
    
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
