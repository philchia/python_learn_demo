"""
@author phil
train ml from train data
"""


from sklearn import svm
from sklearn import grid_search
import numpy as np
from sklearn import cross_validation as cs
from sklearn.externals import joblib


PKL = "/Users/PhilChia/Desktop/downloads/svm/captcha.pkl"


def load_data():
    return np.loadtxt("/Users/PhilChia/Desktop/downloads/train/train_data.txt", delimiter=",")


def cross_validation():
    data_set = load_data()
    row, col = data_set.shape
    x = data_set[:, :col - 1]
    y = data_set[:, -1]
    clf = svm.SVC(kernel='rbf', C=1000)

    scores = cs.cross_val_score(clf, x, y, cv=5)
    print("Accuracy: %2.0f (+/- %2.0f)" % (scores.mean(), scores.std() * 2))


def train():
    data_set = load_data()
    row, col = data_set.shape
    x = data_set[:, :col - 1]
    y = data_set[:, -1]
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(x, y)
    joblib.dump(clf, PKL)


def search_best_parameter():
    parameters = {"kernel": ("linear", "poly", "rbf", "sigmoid"), "C": [1, 100]}
    dataset = load_data()
    row, col = dataset.shape
    x = dataset[:, :col-1]
    y = dataset[:, -1]
    svr = svm.SVC()
    clf = grid_search.GridSearchCV(svr, parameters)
    clf.fit(x, y)
    print(clf.best_params_)


if __name__ == '__main__':
    train()
