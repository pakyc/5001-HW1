#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 21:02:08 2020

@author: pakyuchan
"""

from xml.dom.minidom import parse
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("/Users/pakyuchan/Desktop/blocklist.xml")
collection=DOMTree.documentElement
A=collection.getElementsByTagName("emItem")
for i in range(len(A)):
    a=A[i].getAttribute('blockID')
    if a[0] == 'i' or a[0] == 'g':
        print(a)
for j in range(len(A)):
    b=A[j].getAttribute('id')
    if b.count('.com') == 1:
        if b[0] != '/':
            print(b)
        