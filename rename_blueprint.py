import os
import re
import shutil
import sys

# Get downloads folder and target folder from text file
def read_selected_paths_from_file():
    try:
        with open("selected_paths.txt", "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                download_folder_text = lines[0].strip().replace("Download Folder: ", "")
                new_folder_text = lines[1].strip().replace("New Folder: ", "")
                return download_folder_text, new_folder_text
    except FileNotFoundError:
        pass
    return None, None

# Get Title from every blueprint file, check if it already exists in target folder, rename, and copy to new folder
def main():

    download_folder_text, new_folder_text = read_selected_paths_from_file()

    if download_folder_text is None or new_folder_text is None:
        print("Please select both folders before running the script.")
        return

    downloads_folder = os.path.expanduser(f"{download_folder_text}")
    path = f"{new_folder_text}"
    directory = os.listdir(downloads_folder)

    print (path)
    for f in directory:
        if "blueprint" in f:
            old_file_name = os.path.join(downloads_folder, f)
            try:
                # Find blueprint Title in JSON
                with open(old_file_name) as x:
                    title = x.readlines()
                    pattern = r'"name": "([^"]+)"'
                    match = re.search(pattern, title[1])

                    if match:
                        name = match.group(1)
                        finished_name = re.sub(r'[^a-zA-Z]', "", name)

                        new_file_name = os.path.join(path, f'{finished_name}.json')

                        # Only creates new file if a file with the same name does not exist in source folder
                        if os.path.exists(new_file_name) == False:

                            new_file =  shutil.copy(old_file_name, path)

                            os.rename(new_file, new_file_name)
                        else:
                            print(f"{new_file_name} already exists")
            except Exception as e:
                print(f"Failed to process {f}: {str(e)}")
            
    print("Processing completed.")

if __name__ == "__main__":
    main()
