import numpy as np


def calcGini(dataset):
    y_labels = np.unique(dataset[:, -1])
    y_counts = len(dataset)
    y_p = {}
    gini = 1.0
    for y_label in y_labels:
        y_p[y_label] = len(dataset[dataset[:, -1] == y_label]) / y_counts
        gini -= y_p[y_label] ** 2
    return gini
