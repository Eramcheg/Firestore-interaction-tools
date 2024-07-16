import os

# Specify the folder path where your files are located
folder_path = f'G:\\FIles\\OliverWeber\\furnitureCatalog'

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through each file
for filename in files:
    if filename.startswith('page_') and filename.endswith('.jpg'):
        # Extract the current number from the filename
        try:
            current_number = int(filename.split('_')[1].split('.')[0])
            # Calculate the new number by adding 127
            new_number = current_number - 49
            # Form the new filename
            new_filename = f"page_{new_number}.jpg"
            # Rename the file
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")
        except ValueError:
            print(f"Skipping {filename} as it does not match expected format")
    else:
        print(f"Skipping {filename} as it is not a .png file or does not start with 'page_'")