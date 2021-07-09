#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-09
################################################################

# 给定一个字符串，请你找出其中不含有重复字符的最长子串的长度
# question_string = "abcabcbb"


class SlidingWindow(object):
    def __init__(self, question_string):
        self.__question_string = question_string
        self.__question_length = len(question_string)
        self.__count = 0

    def solve(self):
        cnt_dict = {}
        end = 0
        
        for start in range(self.__question_length):
            if start > 0:
                cnt_dict[self.__question_string[start - 1]] += -1

            while end < self.__question_length:
                try:
                    if cnt_dict[self.__question_string[end]] == 1:
                        break
                    else:
                        cnt_dict[self.__question_string[end]] += 1
                        end += 1
                except KeyError:
                    cnt_dict[self.__question_string[end]] = 1
                    end += 1
                

            self.__count = max(self.__count, end - start)

        return self.__count


def main():
    question_string = "abcabcbb"
    sliding_window = SlidingWindow(question_string)
    print(sliding_window.solve())


if __name__ == '__main__':
    main()
