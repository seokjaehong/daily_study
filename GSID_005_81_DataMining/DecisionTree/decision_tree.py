import csv
from collections import OrderedDict
from math import log
import operator
import pandas as pd


class MyDecisionClassifierTree():
    def __init__(self, data_file='heart_2020_cleaned_3.csv'):
        self.filename = data_file
        self.dataset, self.label = self.get_dataset()
        self.base_entropy = self.get_entropy(self.dataset)
        self.all_label = self.label.copy()


    def get_entropy(self, dataset):
        """
        엔트로피를 도출하는 함수
        :param dataset:
        :return:
        """

        label_count_dict = {}
        for feature in dataset:
            # print(feature)
            curr_label = feature[0]  # 데이터셋의 첫항은 질병유무를 의미함
            if curr_label not in label_count_dict.keys():  # 처음 데이터
                label_count_dict[curr_label] = 0
            # Yes/No에 를 개수별로 집계
            label_count_dict[curr_label] += 1
        entropy = 0.0
        for key in label_count_dict:
            prob = float(label_count_dict[key]) / len(dataset)  # 각 항목의 Probability계산
            entropy -= prob * log(prob, 2)  # 엔트로피 계산
        return entropy

    def get_dataset(self):
        data, label = list(), list()
        for row in csv.reader(open(self.filename)):
            if len(label) > 0:
                data.append(row)
            else:
                label = row
        return data, label

    @staticmethod
    def split_dataset(input_dataset, axis, value):
        result = []
        for vec in input_dataset:
            if vec[axis] == value:
                feature_vec = vec[:axis]  # chop out axis used for splitting
                feature_vec.extend(vec[axis + 1:])
                result.append(feature_vec)

        return result

    def get_best_feature_to_split(self, dataset):
        """
        Gain 값을 도출, 가장항목의 커럶 Index 를 Return
        :param dataset:
        :return:
        """

        num_features = len(dataset[0]) - 1
        best_info_gain = 0.0
        best_feature = -1
        for i in range(1, num_features):
            feature_list = [data[i] for data in dataset]
            new_entropy = 0.0
            for value in set(feature_list):
                # 분할된 데이터셋 별 엔트로피 계산
                sub_dataset = self.split_dataset(dataset, i, value)
                prob = len(sub_dataset) / float(len(dataset))
                new_entropy += prob * self.get_entropy(sub_dataset)
            # Gain을 계산하여
            info_gain = self.base_entropy - new_entropy
            if info_gain > best_info_gain:
                # info_gain이 가장 작은 항목의 index를 도출
                best_info_gain = info_gain
                best_feature = i
        return best_feature

    def get_tree(self, dataset=None, labels=None):
        if not dataset:
            dataset = self.dataset
        if not labels:
            labels = self.label
        target_list = [data[0] for data in dataset]

        if len(set(target_list)) == 1:
            # if target_list.count(target_list[0]) == len(target_list):
            # 더이상 분할할 데이터가없을때 , ex) 해당 노드의 데이터가 모두 False일때]

            return target_list[0]
        best_feature = self.get_best_feature_to_split(dataset)
        best_feature_label = self.label[best_feature]

        my_tree = {best_feature_label: {}}

        del (labels[best_feature])
        feature_values = [data[best_feature] for data in dataset]

        # 순서를 지켜줘야함
        unique_values = list(OrderedDict.fromkeys(feature_values))

        for value in unique_values: # 각 값들을 순회하면서 트리를 채워나감
            # 복사
            sub_labels = self.label[:]
            sub_dataset = self.split_dataset(dataset, best_feature, value)
            my_tree[best_feature_label][value] = self.get_tree(dataset=sub_dataset, labels=sub_labels)
        return my_tree

    def classify(self, tree, label, test_data):
        first_key = list(tree.keys())[0]

        next_dict = tree[first_key]
        # print('next_dict',next_dict)
        f_index = label.index(first_key)
        # print('f_index',f_index)
        # print(test_data)
        key = test_data[f_index]
        # print('key',key)
        child_tree = next_dict[str(key)]
        # print(child_tree)

        if isinstance(child_tree, dict):
            return self.classify(tree=child_tree, label=label, test_data=test_data)
        return child_tree

    # def draw_tree(self,tree,feature_names, class_names):
    #     # import graphviz
    #     # from sklearn.tree import export_graphviz
    #
    #     tree = export_graphviz(tree,feature_names=feature_names,class_names=class_names)
    #
    #     graphviz.Source(tree)


if __name__ == '__main__':
    m = MyDecisionClassifierTree()
    # m.preprocessing()
    tree = m.get_tree()
    # m.draw_tree(tree,m.all_label,['MentalHealth','SleepTime'])
    print("TREE", tree)

    answer = m.classify(tree=tree, label=m.all_label,
                        test_data=['?', 1, 1, 0, 0, 3, 30, 0, 0, 1, 0, 1, 1, 4, 5, 1, 0, 1])
    print(answer)
