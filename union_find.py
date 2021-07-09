#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-09
################################################################

# 班上有N名学生。其中有些人是朋友，有些则不是。
# 他们的友谊具有是传递性。如果已知A是B的朋友，B是C的朋友，那么我们可以认为A也是C的朋友。
# 所谓朋友圈，是指所有朋友的集合。
# 给定一个N*N的矩阵M，表示班级中学生之间的朋友关系。如果M[i][j]=1，表示已知第i个和第j个学生互为朋友关系，否则为不知道
# 你必须输出所有学生中的已知的朋友圈总数


class UnionFind(object):
    def __init__(self, student_list):
        self.__student_list = student_list
        self.__student_length = len(student_list)
        self.__father_list = [i for i in range(self.__student_length)]
        self.__count = 0

    def find_loop_count(self):
        for i in range(self.__student_length):
            for j in range(self.__student_length):
                if self.__student_list[i][j]:
                    self.__union(i,j)
        
        for i in range(self.__student_length):
            if self.__find(i) == i:
            # if self.__father_list[i] == i:
                self.__count += 1
        
        return self.__count

    def __union(self, item_1, item_2):
        self.__father_list[self.__find(item_1)] = self.__find(item_2)

    def __find(self, item):
        if self.__father_list[item] == item:
            return item
        else:
            self.__father_list[item] = self.__find(self.__father_list[item])
            return self.__father_list[item]

    def __connected(self, item_1, item_2):
        return self.__find(item_1) == self.__find(item_2)


def main():
    student_list = [[True, True, False], [True, True, True],
                    [False, True, True]]
    # student_list = [[True, True, False], [True, True, False],
    #                 [False, False, True]]
    union_find = UnionFind(student_list)
    print(union_find.find_loop_count())


if __name__ == '__main__':
    main()