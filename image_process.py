"""
@author: phil
"""


import os
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import time
from pytesseract import *


# segment captcha image
def segment(img):
    start = 10
    width = 40
    height = 70
    t = 20
    ret = []

    for i in range(4):
        sub = img.crop((start+width*i, t, start+width*(i+1), height))
        ret.append(sub)
    return ret


# batch operation cut images
def cut_images(img_name, to_path):
    img = image_pre_process(img_name)
    pics = segment(img)
    for pic in pics:
        pic.save(to_path % int(time.time() * 1000000), "jpeg")


#加载需要识别的图片，参数为路径
def load_images(img):
    img = image_pre_process(img)
    pics = segment(img)
    ret = []
    for pic in pics:
        pixels = get_binary_represent_from_img(pic)
        ret.append(pixels)
    return ret


# binary process image
def image_pre_process(img_name):
    img = Image.open(img_name)
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(1)
    img = img.convert('L')
    return img


#获取图片二值化的数学值
def get_binary_represent_from_img(im):
    img = np.array(im)
    rows, cols = img.shape
    for row in range(rows):
        for col in range(cols):
            if img[row, col] <= 128:
                img[row, col] = 0
            else:
                img[row, col] = 1
    return np.ravel(img)  # img.reshape(1, rows * cols)


#获取图片二值化的数学值
def get_binary_represent_from_path(path_):
    img = Image.open(path_)
    return get_binary_represent_from_img(img)


# get all files in path
def get_files(path_):
    ret = []
    files = os.listdir(path_)
    for file in files:
        full_path = path_ + file
        if full_path.rfind(u'.DS_Store') == -1 and full_path.rfind(u'.idea') == -1:
            ret.append(full_path)
    return ret


# load image segment's binary
def load_image_segment_binary(path_):

    im = image_pre_process(path_)

    pics = segment(im)
    rs = []
    for pic in pics:
        pixels = get_binary_represent_from_img(pic)
        rs.append(pixels)
    return rs


# write content into file
def write_content(content_, full_path):
    with open(full_path, "a+") as f_:
        f_.write(content_)
        f_.write('\n')
        f_.close()


# recognize image
def ocr(image_path):
    try:
        img = Image.open(image_path)
        ret = image_to_string(img, config="-psm 10")
    except:
        return "none"
    return ret
