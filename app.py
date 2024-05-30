import os
import shutil
import sys
import tkinter as tk
from tkinter import messagebox, filedialog;

def find_unreal_projects(root_dir, progress_callback):
    """Find all Unreal Engine 5 projects in the given directory and subdirectories"""
    unreal_projects = []
    for i, (root, dirs, files) in enumerate(os.walk(root_dir), start=1):
        progress_callback(f"Scanning directory {os.path.relpath(root, root_dir)} ({i}/{len(list(os.walk(root_dir)))})")
        if ".uproject" in files:
            unreal_projects.append(os.path.relpath(root, root_dir))
    return unreal_projects

def find_intermediate_dirs(project_dir, progress_callback):
    """Find all folders named 'Intermediate' in the given Unreal Engine project directory"""
    intermediate_dirs = []
    for i, (root, dirs, files) in enumerate(os.walk(project_dir), start=1):
        progress_callback(f"Scanning directory {os.path.relpath(root, project_dir)} ({i}/{len(list(os.walk(project_dir)))})")
        if "intermediate" in dirs:
            intermediate_dirs.append(os.path.relpath(root, project_dir))
    return intermediate_dirs

def find_derived_data_cache_dirs(project_dir, progress_callback):
    """Find all folders named 'DerivedDataCache' in the given Unreal Engine project directory"""
    derived_data_cache_dirs = []
    for i, (root, dirs, files) in enumerate(os.walk(project_dir), start=1):
        progress_callback(f"Scanning directory {os.path.relpath(root, project_dir)} ({i}/{len(list(os.walk(project_dir)))})")
        if "DerivedDataCache" in dirs:
            derived_data_cache_dirs.append(os.path.relpath(root, project_dir))
    return derived_data_cache_dirs

def find_saved_dirs(project_dir, progress_callback):
    """Find all folders named 'Saved' in the given Unreal Engine project directory"""
    saved_dirs = []
    for i, (root, dirs, files) in enumerate(os.walk(project_dir), start=1):
        progress_callback(f"Scanning directory {os.path.relpath(root, project_dir)} ({i}/{len(list(os.walk(project_dir)))})")
        if "Saved" in dirs:
            saved_dirs.append(os.path.relpath(root, project_dir))
    return saved_dirs

def get_all_dirs_to_delete(unreal_projects, progress_callback):
    """Find all intermediate, DerivedDataCache, and Saved folders in all Unreal Engine projects"""
    all_dirs_to_delete = []
    for i, project in enumerate(unreal_projects, start=1):
        progress_callback(f"Scanning project {project} ({i}/{len(unreal_projects)})")
        intermediate_dirs = find_intermediate_dirs(project, progress_callback)
        derived_data_cache_dirs = find_derived_data_cache_dirs(project, progress_callback)
        saved_dirs = find_saved_dirs(project, progress_callback)
        all_dirs_to_delete.extend(intermediate_dirs)
        all_dirs_to_delete.extend(derived_data_cache_dirs)
        all_dirs_to_delete.extend(saved_dirs)
    return all_dirs_to_delete

def delete_dirs_to_delete(dirs_to_delete, progress_callback):
    """Delete all directories in the given list"""
    for i, dir in enumerate(dirs_to_delete, start=1):
        progress_callback(f"Deleting directory {dir} ({i}/{len(dirs_to_delete)})")
        try:
            shutil.rmtree(dir)
        except OSError as e:
            print(f"Error: {e.filename} - {e.strerror}")
    
def main():
    """Main function of the tool"""
    root = tk.Tk()
    root.title("Unreal Engine Cleanup Tool")

    root_dir = tk.filedialog.askdirectory()
    unreal_projects = find_unreal_projects(root_dir, lambda msg: print(msg))
    dirs_to_delete = get_all_dirs_to_delete(unreal_projects, lambda msg: print(msg))
    print(f"The following directories will be deleted:")
    for dir in dirs_to_delete:
        print(f"- {dir}")
    resp = input("y/n: ")
    if resp.lower() == 'y':
        delete_dirs_to_delete(dirs_to_delete, lambda msg: print(msg))
        print("All directories have been deleted.")
    else:
        print("No directories have been deleted.")
    root.destroy();

if __name__ == "__main__":
    main()
    

