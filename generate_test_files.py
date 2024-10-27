import os
import random

def generate_test_files(file_count=15):
    # Define file extensions for each category
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Audio": [".mp3", ".wav"],
        "Videos": [".mp4", ".avi"],
        "Archives": [".zip", ".rar"],
        "Executables": [".exe", ".msi"]
    }

    # Get the directory of the script
    base_directory = os.path.dirname(os.path.abspath(__file__))
    base_directory = os.path.join(base_directory, "Test Files")

    # Function to find a unique folder name
    def get_unique_folder_name(base_path, base_name="test"):
        counter = 1
        while True:
            folder_name = f"{base_name}{counter}"
            folder_path = os.path.join(base_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)  # Create the folder if it doesn't exist
                print(f"Created folder: {folder_name}")
                return folder_path
            counter += 1

    # Get a unique folder path for the test files
    unique_folder_path = get_unique_folder_name(base_directory)

    # Generate the required number of empty files with random extensions
    counter = 1
    all_extensions = [ext for extensions in file_types.values() for ext in extensions]
    
    while counter <= file_count:
        ext = random.choice(all_extensions)
        category = [k for k, v in file_types.items() if ext in v][0].lower()
        filename = f"{category}_file_{counter}{ext}"
        file_path = os.path.join(unique_folder_path, filename)
        open(file_path, 'w').close()  # Creates an empty file
        print(f"Created file: {filename}")
        counter += 1

# Specify the directory to generate the test files
generate_test_files(file_count=99)
