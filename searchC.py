#!/usr/bin/python3
# -*- coding :utf-8 -*-

def searchC(word, string):
    if word not in string:
        return False
    else:
        index_list = []
        for i, j in enumerate(string):
            if j == word:
                index_list.append(i)
        return index_list
