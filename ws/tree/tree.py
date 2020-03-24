from math import log


def create_data_set():
    data_set = [[1, 1, 0, 'yes'],
                [1, 0, 1, 'yes'],
                [1, 0, 0, 'no'],
                [0, 1, 1, 'no'],
                [1, 1, 1, 'no']]
    labels = ['noSurfacing', 'flippers', 'fish']
    return data_set, labels


def split_data_set(data_set, index, value):
    ret_data_set = []
    for data in data_set:
        if data[index] == value:
            reduced_data = data[:index]
            reduced_data.extend(data[index + 1:])
            ret_data_set.append(reduced_data)
    return ret_data_set


def calc_shannon_ent(data_set):
    num = len(data_set)
    label_count = {}
    for data in data_set:
        label = data[-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    shannon_ent = 0.0
    for key in label_count:
        percent = float(label_count[key]) / num
        shannon_ent -= percent * log(percent, 2)
    return shannon_ent


def find_best_feature_to_split(data_set):
    feature_num = len(data_set[0]) - 1
    old_ent = calc_shannon_ent(data_set)
    best_feature = 0
    max_gain = 0.0
    for i in range(feature_num):
        feature_gain = old_ent - calc_ent_by_split(data_set, i)
        if feature_gain > max_gain:
            max_gain = feature_gain
            best_feature = i
    return best_feature


def calc_ent_by_split(data_set, i):
    feature_values = [data[i] for data in data_set]
    destinct_fvs = set(feature_values)
    new_ent = 0
    for feature_value in destinct_fvs:
        sub_data_set = split_data_set(data_set, i, feature_value)
        new_ent += calc_shannon_ent(sub_data_set) * len(sub_data_set) / len(data_set)
    return new_ent


def find_most(label_list):
    label_count = {}
    for label in label_list:
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    sorted_label_count = sorted(label_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_label_count[0][0]


def create_tree(data_set, lables):
    class_list = [data[-1] for data in data_set]
    if class_list.count(class_list[0]) == len(class_list):
        return class_list[0]
    if len(data_set[0]) == 1:
        return find_most(class_list)

    best_feature = find_best_feature_to_split(data_set)
    best_feature_label = lables[best_feature]
    tree = {best_feature_label: {}}
    feature_list = [data[best_feature] for data in data_set]
    feature_set = set(feature_list)
    sub_labels = lables[:best_feature]
    sub_labels.extend(lables[best_feature + 1:])
    for feature_value in feature_set:
        sub_data_set = split_data_set(data_set, best_feature, feature_value)
        tree[best_feature_label][feature_value] = create_tree(sub_data_set, sub_labels)
    return tree


def apply(tree, data, labels):
    if type(tree) is str:
        return tree
    label = list(tree.keys())[0]
    sub_branches = list(tree.values())[0]
    feature = labels.index(label)
    feature_value = data[feature]
    sub_tree = sub_branches[feature_value]
    sub_data = data[:feature]
    sub_data.extend(data[feature + 1:])
    sub_label = labels[:feature]
    sub_label.extend(labels[feature + 1:])
    return apply(sub_tree, sub_data, sub_label)


if __name__ == '__main__':
    d, ll = create_data_set()
    my_tree = create_tree(d, ll)
    print(my_tree)
