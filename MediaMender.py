import os

# Path to your directory where the files are located
folder_path = 'path/to/your/folder'

# Path to your notepad file containing the new names
notepad_path = 'path/to/your/notepad.txt'

# Read all the new names from the notepad file
with open(notepad_path, 'r') as file:
    new_names = file.read().splitlines()

# List all .mp4 files in the directory
files = [file for file in os.listdir(folder_path) if file.endswith('.mp4')]

# Make sure the number of .mp4 files matches the number of new names
if len(files) != len(new_names):
    print("Error: The number of .mp4 files and the number of new names do not match.")
else:
    # Loop through all files and rename them
    for file, new_name in zip(files, new_names):
        # Construct the old file path
        old_file_path = os.path.join(folder_path, file)

        # Construct the new file name by appending the original file name to the new name
        new_file_name = f"{file.split('.')[0]} - {new_name}.mp4"

        # Construct the new file path
        new_file_path = os.path.join(folder_path, new_file_name)

        # Check if the new file path already exists and modify it if necessary
        counter = 1
        while os.path.exists(new_file_path):
            new_file_path = os.path.join(folder_path, f"{new_file_name.split('.')[0]}_{counter}.mp4")
            counter += 1

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed "{file}" to "{new_file_name}"')

print("Renaming completed.")