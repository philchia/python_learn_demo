"""
@author: phil
"""


import shutil
from image_process import *


# category ocr result
def category(origin, path, filename):
    if not os.path.exists(path):
        os.makedirs(path)
    shutil.copy(origin, path+filename)


if __name__ == '__main__':
    target_path = "/Users/PhilChia/Desktop/downloads/tests/"
    for file in os.listdir(target_path):
        full_path = target_path+file
        if full_path.rfind(u'.DS_Store') == -1 and full_path.rfind(u'.idea') == -1:
            cate = ocr(full_path)
            category(full_path, "/Users/PhilChia/Desktop/downloads/category/%s/" % cate, file)
