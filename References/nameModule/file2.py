#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:43:13 2020

@author: manohar
"""
import file1
print ('file2 __name__',__name__)


if __name__ == '__main__':
    print('file2 is being run directly')
else:
    print('file2 is being imported')

