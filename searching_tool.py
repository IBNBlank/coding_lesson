#!/usr/bin/env python3
################################################################
# Copyright 2021 HUST Control Science Innovation Base.
# All rights reserved.
# Author: Dong Zhaorui 847235539@qq.com
# Date  : 2021-07-08
################################################################

# 班上有N名学生。其中有些人是朋友，有些则不是。
# 他们的友谊具有是传递性。如果已知A是B的朋友，B是C的朋友，那么我们可以认为A也是C的朋友。
# 所谓朋友圈，是指所有朋友的集合。
# 给定一个N*N的矩阵M，表示班级中学生之间的朋友关系。如果M[i][j]=1，表示已知第i个和第j个学生互为朋友关系，否则为不知道
# 你必须输出所有学生中的已知的朋友圈总数


class SearchingTool():
    def __init__(self, student_list):
        self.__student_list = student_list
        self.__student_length = len(student_list)
        self.__loop_count = 0
        self.__visited = [False for _ in range(self.__student_length)]
        # BFS
        self.__search_queue = []

    def find_loop_count(self):
        for i in range(self.__student_length):
            if not self.__visited[i]:
                self.__breadth_first_search(i)
                # self.__depth_first_search(i)

                self.__loop_count += 1

        return self.__loop_count

    def __breadth_first_search(self, i):
        self.__search_queue.append(i)
        # 队列不为空，继续层次搜索
        while self.__search_queue:
            start = self.__search_queue.pop(index=0)
            self.__visited[start] = True
            for j in range(self.__student_length):
                # 如果start和j是朋友且j未被标记过
                if self.__student_list[start][j] and not self.__visited[j]:
                    self.__search_queue.append(j)

    def __depth_first_search(self, i):
        for j in range(self.__student_length):
            if self.__student_list[i][j] and not self.__visited[j]:
                self.__depth_first_search(j)


def main():
    student_list = []
    searching_tool = SearchingTool(student_list)
    print(searching_tool.find_loop_count())


if __name__ == '__main__':
    main()