import os
import tkinter as tk
from tkinter import messagebox, filedialog;

def find_unreal_projects(root_dir):
    """Find all Unreal Engine 5 projects in the given directory and subdirectories"""
    unreal_projects = []
    for root, dirs, files in os.walk(root_dir):
        if ".uproject" in files:
            unreal_projects.append(os.path.relpath(root, root_dir))
    return unreal_projects

def find_intermediate_dirs(project_dir):
    """Find all folders named 'Intermediate' in the given Unreal Engine project directory"""
    intermediate_dirs = []
    for root, dirs, files in os.walk(project_dir):
        if "Intermediate" in dirs:
            intermediate_dirs.append(os.path.relpath(root, project_dir))
    return intermediate_dirs

def find_derived_data_cache_dirs(project_dir):
    """Find all folders named 'DerivedDataCache' in the given Unreal Engine project directory"""
    derived_data_cache_dirs = []
    for root, dirs, files in os.walk(project_dir):
        if "DerivedDataCache" in dirs:
            derived_data_cache_dirs.append(os.path.relpath(root, project_dir))
    return derived_data_cache_dirs

def find_saved_dirs(project_dir):
    """Find all folders named 'Saved' in the given Unreal Engine project directory"""
    saved_dirs = []
    for root, dirs, files in os.walk(project_dir):
        if "Saved" in dirs:
            saved_dirs.append(os.path.relpath(root, project_dir))
    return saved_dirs

def get_all_dirs_to_delete(unreal_projects):
    """Find all intermediate, DerivedDataCache, and Saved folders in all Unreal Engine projects"""
    all_dirs_to_delete = []
    for project in unreal_projects:
        intermediate_dirs = find_intermediate_dirs(project)
        derived_data_cache_dirs = find_derived_data_cache_dirs(project)
        saved_dirs = find_saved_dirs(project)
        all_dirs_to_delete.extend(intermediate_dirs)
        all_dirs_to_delete.extend(derived_data_cache_dirs)
        all_dirs_to_delete.extend(saved_dirs)
    return all_dirs_to_delete

def delete_dirs_to_delete(dirs_to_delete):
    """Delete all directories in the given list"""
    for dir in dirs_to_delete:
        try:
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))

def main():
    """Main function of the tool"""
    root = tk.Tk()
    root.title("Unreal Engine Cleanup Tool")

    root_dir = tk.filedialog.askdirectory()
    unreal_projects = find_unreal_projects(root_dir)
    dirs_to_delete = get_all_dirs_to_delete(unreal_projects)
    msg = "The following directories will be deleted:\n"
    for dir in dirs_to_delete:
        msg += f"- {dir}\n"
    resp = messagebox.askyesno(title="Confirm", message=msg)
    if resp:
        for dir in dirs_to_delete:
            try:
                shutil.rmtree(dir)
            except OSError as e:
                print("Error: %s - %s." % (e.filename, e.strerror))
        messagebox.showinfo(title="Complete", message="All directories have been deleted.")
    else:
        messagebox.showinfo(title="Cancelled", message="No directories have been deleted.")
    root.destroy()

if __name__ == "__main__":
    main()

