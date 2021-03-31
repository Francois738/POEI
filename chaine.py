#!/usr/bin/env python3.9
# -*- coding:utf-8 -*-

string = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3.Gandh1"
for i in string:
    if i == '1':
        string.replace(i, 'i')
    elif i == '3':
        string.replace(i, 'e')
