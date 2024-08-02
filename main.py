import os
import shutil
import re


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
    if input_menu == '4':
        root_directory = input("folder to peak and delete ending with /\n")
        organize_files(root_directory)
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


def organize_files(directory_path):
    # Prompt user to select pattern format
    print("Select the pattern format:")
    print("1. 01x01")
    print("2. 1x01")
    print("3. 01x1")
    print("4. 1x1")
    print("5. S01E01")

    pattern_type = input("Enter the number corresponding to the pattern: ").strip()

    # Get the regex pattern based on user input
    if pattern_type == "1":
        pattern = re.compile(r"(\d{2})x(\d{2})")
    elif pattern_type == "2":
        pattern = re.compile(r"(\d)x(\d{2})")
    elif pattern_type == "3":
        pattern = re.compile(r"(\d{2})x(\d)")
    elif pattern_type == "4":
        pattern = re.compile(r"(\d)x(\d)")
    elif pattern_type == "5":
        pattern = re.compile(r"S(\d{2})E(\d{2})")
    else:
        print("Invalid input. Please run the script again and select a valid option.")
        return

    # List to store matched files with their season and episode numbers
    matched_files = []

    # Iterate over all files in the directory
    for filename in os.listdir(directory_path):
        match = pattern.search(filename)
        if match:
            season = int(match.group(1))
            episode = int(match.group(2))
            matched_files.append((season, episode, filename))

    # Sort the files by season and episode numbers
    sorted_files = sorted(matched_files, key=lambda x: (x[0], x[1]))

    # Create folders for each season and move the episodes
    for season, episode, filename in sorted_files:
        season_folder = os.path.join(directory_path, f"Season {season:02}")

        # Create the season folder if it doesn't exist
        if not os.path.exists(season_folder):
            os.makedirs(season_folder)

        # Move the episode file to the season folder
        src_path = os.path.join(directory_path, filename)
        dest_path = os.path.join(season_folder, filename)
        shutil.move(src_path, dest_path)
        print(f"Moved {filename} to {season_folder}")

    # Remove only the episode files from the root folder that were moved
    for _, _, filename in sorted_files:
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Deleted {filename} from root folder")

initial()