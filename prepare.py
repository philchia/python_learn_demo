"""
@author phil
prepare data for train
"""


from image_process import *


if __name__ == '__main__':
    path = "/Users/PhilChia/Desktop/downloads/category/%s/"
    for i in range(10):
        print(i)
        for f in get_files(path % i):
            pixels = get_binary_represent_from_path(f).tolist()
            pixels.append(i)
            pixels = [str(i) for i in pixels]
            content = ",".join(pixels)
            write_content(content, "/Users/PhilChia/Desktop/downloads/train/train_data.txt")
