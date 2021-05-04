#!usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import imageio
import matplotlib.pyplot as plt
from matplotlib import rcParams
from PIL import Image

path = '/home/vyacheslav/Projects/active_projects/CryptoStorage/dr/1.tif'
path2 = '/home/vyacheslav/Projects/active_projects/PH_CNN_Model/data'


def dir_read(folder):
    img_lst = list()
    for i in os.listdir(folder):
        img_lst.append(folder+'/'+i)
    #print(img_lst)
    return img_lst


def img_iter(source, di):
    im_l = source
    for i in source:
        pass
        #img_show(i, di, im_l)
        break

#Image.open(path+'/'+'1.tif')
#dir_read(path2)