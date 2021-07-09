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

    def get_list(self):
        return self.__num_list

    def sort_list(self):
        # self.__bubble_sort()
        self.__quick_sort(0, self.__num_length - 1)
        # self.__num_list = self.__merge_sort(self.__num_list)

    def __bubble_sort(self):
        for i in range(self.__num_length):
            for j in range(self.__num_length - i - 1):
                if self.__num_list[j] > self.__num_list[j + 1]:
                    self.__num_list[j], self.__num_list[
                        j + 1] = self.__num_list[j + 1], self.__num_list[j]

    def __quick_sort(self, begin, end):
        if begin < end:
            pivot_index = self.__partition(begin, end)
            self.__quick_sort(begin, pivot_index - 1)
            self.__quick_sort(pivot_index + 1, end)

    def __partition(self, begin, end):
        pivot = self.__num_list[end]
        slow = begin - 1

        for quick in range(begin, end):
            if self.__num_list[quick] < pivot:
                slow += 1
                self.__num_list[slow], self.__num_list[
                    quick] = self.__num_list[quick], self.__num_list[slow]
        self.__num_list[slow + 1], self.__num_list[end] = self.__num_list[
            end], self.__num_list[slow + 1]

        return slow + 1

    def __merge_sort(self, num_list):
        if len(num_list) <= 1:
            return num_list
        mid = len(num_list) // 2
        left = self.__merge_sort(num_list[:mid])
        right = self.__merge_sort(num_list[mid:])
        return self.__merge(left, right)

    def __merge(self, left, right):
        result = []
        left_index, right_index = 0, 0
        left_length, right_length = len(left), len(right)

        while left_index < left_length and right_index < right_length:
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result += left[left_index:]
        result += right[right_index:]

        return result


def main():
    num_list = [64, 34, 25, 12, 22, 90, 11]
    sort_tool = SortTool(num_list)
    sort_tool.sort_list()
    print(sort_tool.get_list())


if __name__ == '__main__':
    main()