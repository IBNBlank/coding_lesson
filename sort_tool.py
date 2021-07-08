#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-08
################################################################


class SortTool(object):
    def __init__(self, num_list):
        self.__num_list = num_list
        self.__num_length = len(num_list)

    def show_list(self):
        print(self.__num_list)

    def sort_list(self):
        self.__bubble_sort()
        self.__quick_sort()
        self.__merge_sort()

    def __bubble_sort(self):
        for i in range(self.__num_length):
            for j in range(self.__num_length - i - 1):
                if self.__num_list[j] > self.__num_list[j + 1]:
                    self.__num_list[j], self.__num_list[
                        j + 1] = self.__num_list[j + 1], self.__num_list[j]

    def __quick_sort(self):
        pass

    def __merge_sort(self):
        pass


def main():
    num_list = [64, 34, 25, 12, 22, 90, 11]
    sort_tool = SortTool(num_list)
    sort_tool.show_list()
    sort_tool.sort_list()
    sort_tool.show_list()


if __name__ == '__main__':
    main()