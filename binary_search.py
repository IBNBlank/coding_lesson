#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-08
################################################################

# 给定一个非负整数数组和一个整数m
# 你需要将这个数组分成m个非空的连续子数组
# 设计一个算法是的这m个子数组各自和的最大值最小
# divide = 2
# num_list = [7, 2, 5, 10, 8]


class BinarySearch(object):
    def __init__(self, divide, num_list):
        self.__divide = divide
        self.__num_list = num_list
        self.__left = max(num_list) - 1
        self.__right = sum(num_list)

    def solve(self):
        while self.__right - self.__left > 1:
            mid = (self.__right + self.__left) // 2
            if self.__is_in_right(mid):
                self.__right = mid
            else:
                self.__left = mid

        # self.__right = self.__left + 1
        return self.__right

    def __is_in_right(self, mid):
        cnt = 1
        cur = 0
        for num in self.__num_list:
            cur += num
            if cur > mid:
                cnt += 1
                cur = num
        return cnt <= self.__divide


def main():
    divide = 2
    num_list = [7, 2, 5, 10, 8]
    binary_search = BinarySearch(divide, num_list)
    print(binary_search.solve())


if __name__ == '__main__':
    main()