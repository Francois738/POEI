#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-

def compteur(letter, string):
    index_list = []
    for i in string:
      if i == letter:
         index_list.append(i)
    return len(index_list)
