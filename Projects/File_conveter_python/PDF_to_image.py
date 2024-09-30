
import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path

def pdf_to_image(pdf_file, output_dir):
    # Convert PDF pages to images
    images = convert_from_path(pdf_file)
    
    # Save each image to the output directory
    image_paths = []
    for page_num, img in enumerate(images):
        img_path = os.path.join(output_dir, f"page_{page_num + 1}.png")
        img.save(img_path, 'PNG')
        image_paths.append(img_path)
    
    return image_paths

pdf_file = "./SQL_connectivity_in_Python1.pdf"
output_dir = "./SQL_connectivity_in_Python1_images"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    
# Convert PDF to images and get the list of image paths
image_paths = pdf_to_image(pdf_file, output_dir)

# Print the paths of the generated images
for img_path in image_paths:
    print(img_path)



# import os
# from PyPDF2 import PdfReader
# from pdf2image import convert_from_path

# def pdf_to_image(pdf_file,output_dir):
#     images =[]
#     with open(pdf_file,'rb') as f:
#         reader = PdfReader(f)
#         for page_num, _ in enumerate(reader.pages):
#             img_path = os.path.join(output_dir,f"page_{page_num}.png")
#             images.append(img_path)
#         return images

# pdf_file = "./SQL connectivity in Python1.pdf"
# output_dir = "./SQL connectivity in Python1.pdf"

# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
    
# pdf_to_image(pdf_file,output_dir)