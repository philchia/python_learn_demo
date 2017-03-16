"""
@author: phil
cut images
"""


from image_process import *


if __name__ == '__main__':
    import os
    d = "/Users/PhilChia/Desktop/downloads/"
    for name in os.listdir(d):
        name = d + name
        if name.rfind(u'.DS_Store') == -1:
            cut_images(name, "/Users/PhilChia/Desktop/downloads/tests/%s.%s")
