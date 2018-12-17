#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 12/17/2018 3:25 PM 
# @Author : Xiang Chen (Richard)
# @File : creating_HDF5_files.py 
# @Software: PyCharm
import numpy as np
import h5py
import list_imags_and_label

data_order = 'tf' # 'tf' for tensorflow

# check the order of data and chose proper data shape to save images
train_shape = (len(train_addrs),224,224,3)
val_shape = (len(val_addrs),224,224,3)
test_shape = (len(test_addrs),224,224,3)
