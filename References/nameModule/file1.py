#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:32:51 2020

@author: manohar
"""

print ('file1 __name__',__name__)


if __name__ == '__main__':
    print('file1 is being run directly')
else:
    print('file1 is being imported')

