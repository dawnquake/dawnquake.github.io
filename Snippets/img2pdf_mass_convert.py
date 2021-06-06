from PIL import Image, ImageEnhance
import glob
import os
from natsort import natsorted, ns

file_list = natsorted(glob.glob("*.jpeg"))
print(file_list) ## Checking that the file list is correct
output_filename = "output.pdf" ## Filename for output
image0 = Image.open(file_list[0])

rest_image_list = []

for index in range(1, len(file_list)):
    image = Image.open(file_list[index])

    ## Here are some typical applicable
    # image = image.resize((600, 849))
    
    # left = 40
    # top = 40
    # right = 560
    # bottom = 809
    # image = image.resize((600, 849))
    
    # factor = 1
    # enhancer = ImageEnhance.Contrast(image)
    # image_mod = enhancer.enhance(factor)
    # print(image_mod.size)
    # Here, image_mod is the output
    # so you should append the image_mod

    rest_image_list.append(image)



image0.save(output_filename,
            "PDF" ,
            resolution=100.0,
            save_all=True,
            append_images=rest_image_list)