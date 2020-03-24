from numpy import *


def file2mat(filename):
    fr = open(filename)
    array_of_lines = fr.readlines()
    num_of_lines = len(array_of_lines)
    returnmat = zeros((num_of_lines, 3))
    class_label_vector = []
    index = 0
    for line in array_of_lines:
        line = line.strip()
        print(line)
        items = line.split('\t')
        print(items)
        returnmat[index, :] = items[0:3]
        class_label_vector.append(int(items[-1]))
        index += 1
    return returnmat, class_label_vector
