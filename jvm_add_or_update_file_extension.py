import os
# The os module in Python is a built-in library that provides a way to interact with the operating system
# specifically for file and directory manipulation (like listing files, checking file types, renaming files, etc.).

# Define the directory you want to check
directory = "path_to_your_directory"  # Change this to your directory path

# Loop through the files in the directory
for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    # # Method 1: only update files without an existing extension
    # # Check if it's a file and doesn't have an extension
    # if os.path.isfile(file_path) and '.' not in filename:
    #     new_filename = filename + ".jpg"  # Add .jpg extension
    #     new_file_path = os.path.join(directory, new_filename)

    # Method 2: add and change file extensions
    # Check if it's a file and either doesn't have an extension or doesn't already have a .jpg extension
    if os.path.isfile(file_path) and ('.' not in filename or not filename.lower().endswith('.jpg')):
        # Add .jpg extension (removes current extension if any)
        new_filename = filename.split('.')[0] + ".jpg"
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file with the new extension
        os.rename(file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Print a completion note after the looping completes
print("\nFile renaming process completed.")
