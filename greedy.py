#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-09
################################################################

# 给定一个非负整数数组，你最初位于数组的第一个位置
# 数组中的每个元素代表你在该位置可以跳跃的最大长度
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置
# num_list = [2, 3, 1, 1, 4]


class Greedy(object):
    def __init__(self, num_list):
        self.__num_list = num_list
        self.__num_length = len(num_list)

    def solve(self):
        current, previous, step = 0, -1, 0
        while current < self.__num_length - 1:
            step += 1
            farthest = current
            for i in range(previous + 1, current + 1):
                farthest = max(farthest, i + self.__num_list[i])
            previous, current = current, farthest

        return step


def main():
    num_list = [2, 3, 1, 1, 4]
    greedy = Greedy(num_list)
    print(greedy.solve())


if __name__ == '__main__':
    main()