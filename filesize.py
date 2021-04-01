#!/usr/bin/env python
# coding=utf-8

def file_size(fname):
    import os
    statinfo = os.stat(fname)
    return statinfo.st_size

print("taille du fichier: ",file_size("time.py"))

