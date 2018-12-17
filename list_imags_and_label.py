#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 12/17/2018 3:11 PM 
# @Author : Xiang Chen (Richard)
# @File : list_imags_and_label.py 
# @Software: PyCharm
from random import shuffle
import glob
shuffle_data = True # shuffle the addresses befor saving
hdf5_path = 'Cat vs Dog/dataset.hdf5' # address to where you want to save the hdf5 file
cat_dog_train_path = 'Cat vs Dog/train/*.jpg'

# read addresses and labels from the 'train' folder
addrs = glob.glob(cat_dog_train_path)
labels = [0 if 'cat' in addrs else 1 for addr in addrs] # 0 = Cat, 1 = Dog

# to shuffle data
if shuffle_data:
    C = list(zip(addrs,labels))
    shuffle(C)
    addrs, labels = zip(*c)
# divide the data into 60% train, 20% validation, and 20% test
train_addrs = addrs[0:int(0.6*len(addrs))]
train_labels = labels[0:int(0.6*len(labels))]

val_addrs = addrs[int(0.6*len(addrs)):int(0.8*len(addrs))]
val_labels = labels[int(0.6*len(addrs)):int(0.8*len(addrs))]

test_addrs = addrs[int(0.8*len(addrs)):]
test_labels = labels[int(0.8*len(labels)):]

# open a hdf5 file and create earrays
hdf5_file = h5py.File(hdf5_path,mode='w')

hdf5_file.create_dataset("training_img",train_shape,np.int8)
hdf5_file.create_dataset("val_img",val_shape,np.int8)
hdf5_file.create_dataset("test_img",test_shape,np.int8)

hdf5_file.create_dataset("train_mean",train_shape[1:],np.float32)
hdf5_file.create_dataset("train_labels", (len(train_addrs),), np.int8)
hdf5_file["train_labels"][...] = train_labels
hdf5_file.create_dataset("val_labels", (len(val_addrs),), np.int8)
hdf5_file["val_labels"][...] = val_labels
hdf5_file.create_dataset("test_labels", (len(test_addrs),), np.int8)
hdf5_file["test_labels"][...] = test_labels





