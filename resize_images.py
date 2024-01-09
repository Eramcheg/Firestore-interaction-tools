import os

from PIL import Image

directory_path = "G:\\Main Catalog 2023 with Prices after corrections-bilder(1)"
save_path = "G:\\ResizedCatalog"
files = os.listdir(directory_path)
# Load the image you want to resize
for filename in files:
    image = Image.open(directory_path+ "\\"+filename)

    # Resize the image
    width = 800  # New width of the image
    height = 1104  # New height of the image
    resized_image = image.resize((width, height))

    # Save the resized image
    resized_image.save(save_path+"\\"+filename)