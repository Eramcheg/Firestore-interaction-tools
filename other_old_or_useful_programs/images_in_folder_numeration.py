import os

directory_path = "G:\\Main Catalog 2023 with Prices after corrections-bilder(1)"
files = os.listdir(directory_path)
print(files)
i =1
for filename in files:
        # Create the new name for the file
        new_name = f"{i}.jpg"
        i+=1

        # Get the full paths of the original and new names
        old_path = os.path.join(directory_path, filename)
        new_path = os.path.join(directory_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)