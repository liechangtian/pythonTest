from numpy import *


def file2mat(filename):
    fr = open(filename)
    lines = fr.readlines()
    ord_mat = zeros((len(lines), 3))
    index = 0
    for line in lines:
        items = line.split("\t")
        ord_mat[index, :] = items[:]
        index += 1
    return ord_mat
