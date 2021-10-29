import os
from PIL import Image

path = "img"
filename = "test_g.jpg"


def single_file(file):
    im = Image.open(path + "/" + file, 'r')
    pix_val = list(im.getdata())
    return pix_val


def multi_file(path_to_file):
    for file in os.listdir(path_to_file):
        im = Image.open(path_to_file + "/" + file, 'r')
        pix_val = list(im.getdata())
    return pix_val


def mode(file):
    im = Image.open(path + "/" + file, 'r')
    return im.mode
