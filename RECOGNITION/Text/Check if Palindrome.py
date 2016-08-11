#!/usr/bin/python
# coding=utf-8
"""
Checks if the string entered by the user is a palindrome.
That is that it reads the same forwards as backwards like “racecar”
"""
__author__ = 'tmackan'


def is_palindrome(string):
    return True if string == string[::-1] else False

if __name__ == '__main__':
    print is_palindrome('pop')
    print is_palindrome('abcba')
    print is_palindrome('a')