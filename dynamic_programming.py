#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-08
################################################################

# 找到整数数组num_list能被3整除的元素最大和
# num_list = [3, 6, 5, 1, 8]


class DynamicProgramming(object):
    def __init__(self, num_list):
        self.__num_list = num_list
        self.__num_length = len(num_list)
        self.__dp = [[0 for _ in range(3)]
                     for _ in range(self.__num_length + 1)]
        self.__dp[0] = [0, -1_000, -1_000]

    def solve(self):
        for i in range(1, self.__num_length + 1):
            delta_index = (-self.__num_list[i - 1]) % 3
            for j in range(3):
                self.__dp[i][j] = max(
                    self.__dp[i - 1][j],
                    self.__dp[i - 1][(j + delta_index) % 3] +
                    self.__num_list[i - 1])

        return self.__dp[self.__num_length][0]


def main():
    num_list = [3, 6, 5, 1, 8]
    dynamic_programming = DynamicProgramming(num_list)
    print(dynamic_programming.solve())


if __name__ == '__main__':
    main()