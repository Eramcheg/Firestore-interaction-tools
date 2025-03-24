# from pdf2image import convert_from_path
# import os
# from PIL import Image
# import fitz  # PyMuPDF
# from pdf2image import convert_from_path
#
# from pdf2image import convert_from_path
# from PIL import Image
#
# def extract_and_compress_images_from_pdf(pdf_path, output_folder, quality=85):
#     images = convert_from_path(pdf_path)
#
#     for page_number, image in enumerate(images):
#         # Adjust the filename to include the specified starting page number offset
#         image_filename = f"{output_folder}/page_{page_number + 1 + 207}.jpg"  # Using JPG for better compression
#         # Compress and save the image
#         image.save(image_filename, 'JPEG', quality=quality)
#
# # Usage example:
# pdf_file_path = "../agents app/catalogs/Showcase & Display Spirits 2024.pdf"
# output_folder_path = "G:\\Files\\OliverWeber\\furnitureCatalog2024"
# extract_and_compress_images_from_pdf(pdf_file_path, output_folder_path, quality=85)
import fitz  # PyMuPDF
from PIL import Image


def pdf_page_to_image(pdf_path, page_number, target_width, target_height):
    doc = fitz.open(pdf_path)
    page = doc.load_page(page_number)  # page numbers start from 0

    # Calculate zoom based on the target dimensions and actual page size
    page_width, page_height = page.rect.width, page.rect.height
    zoom_x = target_width / (page_width)  # Dividing by 2 because we'll split the image
    zoom_y = target_height / page_height
    zoom = max(zoom_x, zoom_y)  # Ensure we cover both dimensions

    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom))
    img_path = f'output_page_{page_number}.png'
    pix.save(img_path)
    return img_path


import os  # For path operations


def split_and_rescale_image(img_path, target_width, target_height, page_number, output_folder_path):
    img = Image.open(img_path)
    width, height = img.size

    # Calculate image names based on page number
    left_img_num = page_number * 2 + 219
    right_img_num = page_number * 2 + 1 + 219

    # Construct file paths for the output images
    img_left_path = os.path.join(output_folder_path, f'page_{left_img_num}.jpg')
    img_right_path = os.path.join(output_folder_path, f'page_{right_img_num}.jpg')

    # Crop, resize, and save images
    img_left = img.crop((0, 0, width / 2, height)).resize((target_width, target_height), Image.ANTIALIAS)
    img_right = img.crop((width / 2, 0, width, height)).resize((target_width, target_height), Image.ANTIALIAS)

    img_left.save(img_left_path, quality=85)
    img_right.save(img_right_path, quality=85)

    return img_left_path, img_right_path

def save_image(img_path, target_width, target_height, page_number, output_folder_path):
    img = Image.open(img_path)
    width, height = img.size

    # Calculate image names based on page number
    # Construct file paths for the output images
    img_full_path = os.path.join(output_folder_path, f'page_{page_number+1}.jpg')

    img.save(img_full_path, quality=75)

    return img
# Assuming each target image needs to be 1654x2339
pdf_path = "catalogs/Catalog SPRING 2025 WITH price PRINT.pdf"
for i in range(291, 302):
    page_number = i - 291  # This is already correct, starting from 0
    target_width, target_height = 1654, 2339
    output_folder_path = "G:\\Files\\OliverWeber\\SpringCatalog2025"

    # Convert PDF page to image with adjusted zoom
    img_path = pdf_page_to_image(pdf_path, page_number, target_width, target_height)  # Removed the +1 here
    img = save_image(img_path, target_width, target_height, page_number, output_folder_path)  # Ensure consistency in how page numbers are handled
    # Split the image into two, rescale if necessary, and specify the output folder and numeration
    # left_img_path, right_img_path = split_and_rescale_image(img_path, target_width, target_height, page_number,
    #                                                         output_folder_path)

    # print(f"Left image saved as: {left_img_path}")
    # print(f"Right image saved as: {right_img_path}")