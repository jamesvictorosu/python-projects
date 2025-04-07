
import os
# The os module in Python is a built-in library that provides a way to interact with the operating system
# specifically for file and directory manipulation (like listing files, checking file types, renaming files, etc.).

# Example 1: Renaming a Single File

# Specify the current file name and the new file name
# assumes the file is in the current working directory, if not, provide the full path
current_name = 'old_file.txt'
new_name = 'new_file.txt'

# Rename the file
os.rename(current_name, new_name)

print(f"File renamed from {current_name} to {new_name}")


# Example 2: Renaming All Files in a Directory

# Specify the directory containing the files
directory = '/path/to/your/directory'

# List all files in the directory
files = os.listdir(directory)

# Optional QA - list directory file names and total count
# Print the names of all files in referenced directory
# for filename in files:
#     print(filename)

# Count the total number of files
total_files = len(files)

# Print the total number of files
print(f"\nTotal number of files: {total_files}")

# Initialize a counter for renamed files
renamed_count = 0

# Loop through each file in the directory
for filename in files:
    # Skip hidden files (those starting with a dot)
    if filename.startswith('.'):
        continue
    # # Skip specific file types (non-case sensitive)
    # if filename.lower().endswith('.pdf'):  # Convert to lowercase for comparison
    #     continue

    # Construct the old file path
    old_file_path = os.path.join(directory, filename)

    # Only rename files (not directories)
    if os.path.isfile(old_file_path):
        # Create the new file name (ex. adding a prefix)
        new_filename = 'new_' + filename

        # Construct the new file path
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f"Renamed: {filename} -> {new_filename}")

        # Increment the renamed count
        renamed_count += 1

# Print the total number of renamed files
print(f"\nTotal number of renamed files: {renamed_count}")


# Example 3: Renaming All Files in a Directory with Incremental Numbers

# Specify the directory containing the files
directory = '/path/to/your/directory'

# List all files in the directory
files = os.listdir(directory)

# Optional QA - list directory file names and total count
# Print the names of all files in referenced directory
# for filename in files:
#     print(filename)

# Count the total number of files
total_files = len(files)

# Print the total number of files
print(f"\nTotal number of files: {total_files}")

# Initialize a counter to rename files incrementally
counter = 1
renamed_count = 0  # This counter will track the actual renamed files

# Loop through each file in the directory
for filename in files:
    # Skip hidden files (those starting with a dot)
    if filename.startswith('.'):
        continue
    # # Skip specific file types (non-case sensitive)
    # if filename.lower().endswith('.pdf'):  # Convert to lowercase for comparison
    #     continue

    # Construct the old file path
    old_file_path = os.path.join(directory, filename)

    # Only rename files (not directories)
    if os.path.isfile(old_file_path):
        # Get the file extension (e.g., '.txt', '.jpg')
        file_extension = os.path.splitext(filename)[1]
        # optional - set a specific file extension
        # file_extension = '.jpg'

        # Create the new file name with an incremental number
        new_filename = f"file_{counter}{file_extension}"

        # Construct the new file path
        new_file_path = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)

        print(f"Renamed: {filename} -> {new_filename}")

        # Increment the counter and renamed_count
        counter += 1
        renamed_count += 1

# Print the total number of renamed files
print(f"\nTotal number of renamed files: {renamed_count}")
