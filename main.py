import os
import shutil


def initial():

    input_menu=input("delete folder and evering in it (1)\nOnly peak in folder if its contains that folder anywhere (2)\nMove each file in the root directory into a new folder named after the file (3)\n")
    if input_menu=='1':
        root_directory = input("folder to peak and delete ending with /\n")
        print_and_delete_sample_folders(root_directory)
    if input_menu == '2':
        root_directory = input("folder to peak and delete ending with /\n")
        print_subfolders(root_directory)
    if input_menu == '3':
        root_directory = input("folder to peak and delete ending with /\n")
        move_files_to_named_folders(root_directory)
    else:
        print("Invalid Option")
        initial()

def print_subfolders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            subfolder_path = os.path.join(dirpath, dirname)
            print(subfolder_path)
def print_and_delete_sample_folders(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            subfolder_path = os.path.join(dirpath, dirname)
            print(subfolder_path)
            if dirname == 'Sample':
                try:
                    shutil.rmtree(subfolder_path)
                    print(f'Deleted: {subfolder_path}')
                except Exception as e:
                    print(f'Error deleting {subfolder_path}: {e}')
def move_files_to_named_folders(root_dir):
    """Move each file in the root directory into a new folder named after the file."""
    for item in os.listdir(root_dir):
        item_path = os.path.join(root_dir, item)
        if os.path.isfile(item_path):
            # Create a folder named after the file (without extension)
            folder_name = os.path.splitext(item)[0]
            folder_path = os.path.join(root_dir, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            # Move the file into the newly created folder
            new_file_path = os.path.join(folder_path, item)
            shutil.move(item_path, new_file_path)
            print(f'Moved: {item_path} to {new_file_path}')

initial()