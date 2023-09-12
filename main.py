import tkinter as tk
from tkinter import filedialog
import subprocess

# Function to set the download folder variable
def select_download_folder():
    global download_folder
    download_folder = filedialog.askdirectory()
    download_folder_label.config(text=f"Download Folder: {download_folder}")
    save_paths_to_file()

# Function to set the new folder variable
def select_new_folder():
    global new_folder
    new_folder = filedialog.askdirectory()
    new_folder_label.config(text=f"New Folder: {new_folder}")
    save_paths_to_file()

# Function to run the script using the selected folders
def run_script():
    global download_folder, new_folder
    if download_folder and new_folder:
        # Replace 'your_script.py' with the actual filename of your script
        script_filename = 'rename_blueprint.py'
        command = ['python', script_filename, download_folder, new_folder]
        subprocess.run(command)
    else:
        print("Please select both folders before running the script.")

# Function to save selected paths to a file
def save_paths_to_file():
    global download_folder, new_folder
    with open("selected_paths.txt", "w") as file:
        file.write(f"Download Folder: {download_folder}\n")
        file.write(f"New Folder: {new_folder}")

# Initialize variables
download_folder = ""
new_folder = ""

# Try to load saved paths from the file
try:
    with open("selected_paths.txt", "r") as file:
        lines = file.readlines()
        download_folder = lines[0].strip().replace("Download Folder: ", "")
        new_folder = lines[1].strip().replace("New Folder: ", "")
except FileNotFoundError:
    pass

# Create the main tkinter window
root = tk.Tk()
root.title("Folder Selection Interface")

# Create buttons and labels
download_button = tk.Button(root, text="Select Download Folder", command=select_download_folder)
new_folder_button = tk.Button(root, text="Select New Folder", command=select_new_folder)
run_button = tk.Button(root, text="Run Script", command=run_script)
download_folder_label = tk.Label(root, text=f"Download Folder: {download_folder}")
new_folder_label = tk.Label(root, text=f"New Folder: {new_folder}")

# Arrange widgets in the window
download_button.pack()
new_folder_button.pack()
run_button.pack()
download_folder_label.pack()
new_folder_label.pack()

# Start the tkinter main loop
root.mainloop()
