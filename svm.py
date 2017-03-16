"""
@author: phil
recognize captcha
"""


from sklearn.externals import joblib
from image_process import load_images
import time


PKL = "/Users/PhilChia/Desktop/downloads/svm/captcha.pkl"


def predict(pic_path):
    clf = joblib.load(PKL)
    time1 = time.time()

    res = load_images(pic_path)
    predict_value = []
    for data in res:
        predict_value.append(clf.predict(data)[0])
    predict_value = [str(int(i)) for i in predict_value]
    print("captcha is %s" % "".join(predict_value))
    time2 = time.time()
    print('function took %0.3f ms' % ((time2 - time1) * 1000.0))

if __name__ == '__main__':
    predict("/Users/PhilChia/Desktop/downloads/1489558114478046.jpg")
