import os
import shutil
import sys
import logging

def setup_logging(log_file):
    # Set up logging configuration.
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
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

    # Create parent folder for target directory
    parent_path = os.path.join(directory, "Organized")
    os.makedirs(parent_path, exist_ok=True)
        
    # Create folders for each file type in the target directory
    for folder in file_types.keys():
        folder_path = os.path.join(parent_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Initialize a list to hold unorganized files
    unorganized_extensions = set()

    # Move files into respective folders based on extension
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to the corresponding folder
        _, extension = os.path.splitext(filename)
        moved = False  # Flag to track if file was moved

        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                shutil.move(file_path, os.path.join(parent_path, folder, filename))
                print(f"Moved {filename} to {folder} folder")
                logging.info(f"Moved {filename} to {folder} folder")
                moved = True
                break

        if not moved:
            if extension == "":
                unorganized_extensions.add("<No Extension>")
            else:
                unorganized_extensions.add(extension.lower())
                
    # Log unorganized files if any
    if unorganized_extensions:
        for ext in sorted(unorganized_extensions):
            logging.info(f"Unorganized file extension: {ext}")

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
            parent_path = os.path.join(directory_path, "Organized")
            os.makedirs(parent_path, exist_ok=True)
            log_file_path = os.path.join(parent_path, 'organized_files.log')
            setup_logging(log_file_path)  # Set up logging
            organize_files(directory_path) # Organize files
            remove_empty_folders(parent_path)  # Remove empty folders
        else:
            print(f"The specified path does not exist: {directory_path}")
