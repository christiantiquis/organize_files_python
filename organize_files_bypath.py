import os
import shutil
import sys

def organize_files(directory):
    # Define file types and corresponding folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".pkg", ".apk"],
    }

    # Create folders for each file type in the target directory
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into respective folders based on extension
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to the corresponding folder
        _, extension = os.path.splitext(filename)
        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                print(f"Moved {filename} to {folder} folder")
                break

def remove_empty_folders(directory):
    # Remove empty folders in the specified directory.
    for foldername in os.listdir(directory):
        folder_path = os.path.join(directory, foldername)
        # Check if it's a directory
        if os.path.isdir(folder_path):
            # Remove folder if it's empty
            if not os.listdir(folder_path):
                shutil.rmtree(folder_path)
                print(f"Removed empty folder: {folder_path}")

if __name__ == "__main__":
    # Check if the path argument is provided
    if len(sys.argv) < 2:
        print("Please provide the target directory path.")
    else:
        directory_path = sys.argv[1]
        if os.path.isdir(directory_path):
            organize_files(directory_path) # Organize files
            remove_empty_folders(directory_path)  # Remove empty folders
        else:
            print(f"The specified path does not exist: {directory_path}")
