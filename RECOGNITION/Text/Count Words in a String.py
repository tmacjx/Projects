#!/usr/bin/python
# coding=utf-8
"""
Counts the number of individual
words in a string. For added complexity read these strings in from a text file and generate a summary.
"""
# 单词计数
import os
import sys
import re

__author__ = 'tmackan'


# 统计string中的word
def word_count_string(string):
    return len(string.split(' '))


# 统计file中的word
def word_count_file(path):
    word_list = []
    count = 0
    with open(path, 'r') as text:
        for line in text.readlines():
            for word in line.split(' '):
                if word not in word_list:
                    word_list.append(word)
                    count += 1
                else:
                    continue
    return count


def handle(line):
    # 如果是空行
    if line == "" or is_passline(line):
        return 0
    count = 0
    is_word = False
    for i in range(len(line)):
        # 如果如果遇到单词第一个字母则＋＋，如果遇到非字母，则跳过
        if not line[i].isalpha():
            is_word = False
            continue
        elif is_word is False:
            count += 1
            is_word = True
            continue
        else:
            continue
    return count


_default_config = ('__author__', '__all__')
# 是否全局的无关变量, 比如 __author__, __all__


def is_global_config(line):
    global _default_config
    for config in _default_config:
        if line.startswith(config):
            return True
    return False


# 是否是对模块的引入
# def is_import(line):
#     if line.startswith('import') or line.startswith("from import"):
#         return True
#     return False


_skip_status = False
# 是否是多行注释


def is_note(line):
    global _skip_status

    # #开头的注释
    if line.startswith("#"):
        return True
    # 判断是否是多行注释的开始部分 比如 """, """abc
    if line.startswith('"""'):
        if len(line) > 3 and line.endswith('"""'):
            return True
        _skip_status = True if not _skip_status else False
        return True
    # 处于多行注释之间
    if _skip_status is True:
        return True

    return False


def is_import(line):
    regular_expressions = (['import .*', 'from .* import.*'])
    for pattern in regular_expressions:
        temp = re.compile(pattern)
        if re.search(temp, line) is None:
            continue
        else:
            return True
    return False


def is_passline(line):
    if is_global_config(line) or is_note(line) or is_import(line):
        return True
    return False


class PyContent(object):
    def __init__(self, path):
        # TODO 如何在初始化时, 对path是否以.py结尾做一个判断?
        self.path = path
        self.name = os.path.split(self.path)[1]
        self.__count = 0
        self.__code_line = 0

    def total(self):
        count = 0
        with open(self.path) as text:
            for line in text.readlines():
                # strip 默认删除空白符（包括'\n', '\r',  '\t',  ' ')
                content = line.strip()
                num = handle(content)
                if num != 0:
                    count += num
                    self.__code_line += 1
        self.__count = count
        return self.__count

    def __repr__(self):
        # if not hasattr(self, '__count'):
        self.__count = self.total()
        fmt = '{0} total: {1}>line {2}>words'
        return fmt.format(self.name, self.__code_line, self.__count)

if __name__ == '__main__':

    file_path = sys.argv[1]

    print word_count_string(' abcd dog car apple')
    print word_count_file(file_path)

    py_content = PyContent(file_path)
    print py_content

