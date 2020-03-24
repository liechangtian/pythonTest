import matplotlib
from numpy import array
import matplotlib.pyplot as plt


def runn(mat, label):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(mat[:, 0], mat[:, 1], 15.0 * array(label), 15.0 * array(label))
    plt.show()
