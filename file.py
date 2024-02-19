import os
def list_files_folder(folder_paths):
    try:
        for folder in folder_paths:
            files = os.listdir(folder)
            print(f"files in {folder_paths}):")
            for file in files:
                print(file)
            print()
    except FileNotFoundError:
        print(f"file not found in {folder_paths}")
    except PermissionError:
        print(f"user dosen't have accessto this {folder_paths}")
    except Exception as e:
        print(f"an unexpected error occuredin this {folder_paths}")
folder_paths = input("enter thr list of folders:" ).split()
list_files_folder(folder_paths)
