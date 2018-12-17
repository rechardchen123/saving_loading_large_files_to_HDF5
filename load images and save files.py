#!/usr/bin/env python3
# -*- coding: utf-8 -*- 
# @Time : 12/17/2018 3:33 PM 
# @Author : Xiang Chen (Richard)
# @File : load images and save files.py 
# @Software: PyCharm
import list_imags_and_label
import creating_HDF5_files

# a numpy array to save the mean of the images
mean = np.zeros(train_shape[1:],np.float32)
# loop over train addresses
for i in range(len(train_addrs)):
    # print how many images are saved every 1000 images
    if i % 1000 == 0 and i >1:
        print('Train data:{}/{}'.format(i,len(train_addrs)))
        # read an image and resize to (224,224)
        # cv2 load images as BGR, conver it to RGB
    addr = train_addrs[i]
    img = cv2.imread(addr)
    img = cv2.resize(img,(224,224),interpolation = cv2.INTER_CUBIC)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    # add any image pre_porcessing here
    if data_order =='th':
        img = np.rollaxis(img,2)
        # save the image and calculate the mean so far
    hdf5_file["train_img"][i, ...] = img[None]
    mean += img / float(len(train_labels))
    # loop over validation addresses
    for i in range(len(val_addrs)):
    # print how many images are saved every 1000 images
        if i % 1000 == 0 and i > 1:
            print('Validation data: {}/{}'.format(i, len(val_addrs)))
        # read an image and resize to (224, 224)
        # cv2 load images as BGR, convert it to RGB
        addr = val_addrs[i]
        img = cv2.imread(addr)
        img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)







