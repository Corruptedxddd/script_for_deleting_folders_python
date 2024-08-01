import os
import shutil


def initial():

    input_menu=input("delete folder and evering in it (1)\nOnly peak in folder if its contains that folder anywhere (2)\n")
    if input_menu=='1':
        root_directory = input("folder to peak and delete ending with /\n")
        print_and_delete_sample_folders(root_directory)
    if input_menu == '2':
        root_directory = input("folder to peak and delete ending with /\n")
        print_subfolders(root_directory)
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


initial()