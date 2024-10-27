import os
import shutil

def organize_files(directory):
    # Create a dictionary to map extensions to folders
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Archives": [".zip", ".rar", ".tar", ".gz"]
    }

    # Create folders for each file type
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to the correct folder
        _, extension = os.path.splitext(filename)
        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                shutil.move(file_path, os.path.join(directory, folder, filename))
                print(f"Moved {filename} to {folder} folder")
                break

# Run the organizer on your desired folder
organize_files("path/to/your/folder")
