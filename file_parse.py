import os
from PIL import Image

path = "img"
filename_hr = "marina_stojakovic.jpeg" # File must be colored JPEG image


def reduce_resolution(img):
    split_filename = img.split(sep='.')
    filename_lr = split_filename[0] + '_lr.' + split_filename[1]
    image_file = Image.open(path + "/" + filename_hr, 'r')
    image_file.save(path + "/" + filename_lr, quality=1)
    return filename_lr


def single_file(file):
    im = Image.open(path + "/" + file, 'r')
    pix_val = list(im.getdata())
    return pix_val


def multi_file(path_to_file):
    for file in os.listdir(path_to_file):
        im = Image.open(path_to_file + "/" + file, 'r')
        pix_val = list(im.getdata())
    return pix_val