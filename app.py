import os
import shutil
from tqdm import tqdm
from tkinter import Tk, filedialog

def select_directory():
    Tk().withdraw()  # We don't want a full GUI, so keep the root window from appearing
    directory = filedialog.askdirectory()  # Show an "Open" dialog box and return the path to the selected folder
    return directory

def scan_directories(base_path, search_term):
    matching_dirs = []
    for root, dirs, files in tqdm(os.walk(base_path), desc="Scanning directories"):
        for dir_name in dirs:
            if search_term.lower() in dir_name.lower():
                matching_dirs.append(os.path.join(root, dir_name))
    return matching_dirs

def delete_directories(directories):
    for dir_path in tqdm(directories, desc="Deleting directories"):
        shutil.rmtree(dir_path)

def main():
    print("Select the base directory for the cleanup operation:")
    base_directory = select_directory()
    
    if not base_directory:
        print("No directory selected. Exiting.")
        return
    
    search_term = input("Enter the search term to match directories: ")
    matching_dirs = scan_directories(base_directory, search_term)
    
    if not matching_dirs:
        print(f"No directories found matching the term '{search_term}'.")
        return
    
    print("The following directories match your search term:")
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
