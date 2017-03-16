"""
@author: phil
download images
"""


import requests
import time


# download images
def download(image_name):
    url = 'http://smart.gzeis.edu.cn:8081/Content/AuthCode.aspx'
    res = requests.get(url, stream=True)
    with open("/Users/PhilChia/Desktop/downloads/%s.jpg" % image_name, 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    for _ in range(1000):
        imageName = int(time.time()*1000000)
        download(imageName)
