# File Organizer Script

## Overview

The `organize_files.py` script is a Python utility that organizes files within a specified directory based on their file types. It creates dedicated folders for various file categories such as images, documents, audio, videos, archives, and executables. Additionally, the script checks for and removes any empty folders that may remain after the organization process.

## Features

- Automatically organizes files into designated folders based on file extensions.
- Creates folders for different categories including:
  - Images
  - Documents
  - Audio
  - Videos
  - Archives
  - Executables
- Removes any empty folders left after organizing files.

## Requirements

- Python 3.x
- `os`, `shutil`, and `sys` modules (included in the standard Python library)

## Usage

### Option 1: Run the Python Script Directly

1. **Download the Script**: Clone or download the repository containing `organize_files.py`.

2. **Run the Script**: Use the command line to execute the script by providing the target directory path as an argument.

   ```bash
   python organize_files.py "path/to/your/directory"
   ```

   Replace `"path/to/your/directory"` with the path to the directory you want to organize.

3. **Example**:

   ```bash
   python organize_files.py "C:\Users\YourUsername\Downloads"
   ```

### Option 2: Run Using the Batch File

1. **Download the Batch File**: Save the provided `run_organize_files.bat` batch file to the same directory as `organize_files.py`.

2. **Run the Batch File**: Double-click on the batch file or run it from the command line, providing the target directory path as an argument:

   ```bash
   run_organize_files.bat "C:\path\to\target\directory"
   ```

3. **Example**:

   ```bash
   run_organize_files.bat "C:\Users\YourUsername\Downloads"
   ```

   If no directory path is provided, the batch file will prompt you for the correct usage.

## How It Works

1. The script first defines various file types and their corresponding folders.
2. It checks if the provided directory path is valid.
3. It creates necessary folders in the target directory.
4. It iterates through the files in the specified directory, moving them into their respective folders based on their extensions.
5. After organizing the files, it checks for and removes any empty folders left in the target directory.

## Contributing

If you would like to contribute to this project, feel free to submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Author

Created by [Christian Tiquis]
