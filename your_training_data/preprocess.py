# -*- coding: utf-8 -*-
#########################################################################
# Author: mao
# Created Time: 04,28,Apr,2018
# File Name: generate_train_validation.py
# Description:
# 	1. read label_old.txt and delete useless label and pic
# 	2. reorder pic and generate new label.txt
#########################################################################

import os
import shutil
from os import getcwd

classes = ['Traffic_Light_go', 'Traffic_Light_stop', 'Traffic_Light_ambiguous', 'Traffic_Light_warning']

width = 640
hight = 480
size = [width,hight]

def process(file_path, out_path, image_in_path, image_out_path):
    #generate labels
    with open(file_path) as f:
        i = 0
        pic_indexs = []
        if os.path.exists(out_path):
            shutil.rmtree(out_path)
        os.mkdir(out_path)
        for line in f.readlines():
            strs = str.split(line)
            pic_index = strs[2]
            pic_indexs.append(pic_index)
            x1 = float(strs[3])
            y1 = float(strs[4])
            x2 = float(strs[5])
            y2 = float(strs[6])
            box = [x1, x2, y1, y2]
            x,y,w,h = convert(size, box)
            label = strs[-3][1:]+'_'+strs[-2][:-1]+'_'+strs[-1][1:-1]
            class_ = classes.index(label)
            with open(out_path+'/%s.txt'%(str(i).zfill(6)), 'w') as out:
                out.write('%s %s %s %s %s\n'%(class_, x, y, w, h))
            i = i+1
    
    #reorder pictures
    i = 0
    if os.path.exists(image_out_path):        
        shutil.rmtree(image_out_path)
    os.mkdir(image_out_path)
    for index in pic_indexs:
        pic_name = 'frame_'+index.zfill(6)+'.jpg'  #fill left null with zeros
        new_pic = str(i).zfill(6)+'.jpg'
        new_pic_path = image_out_path + '/' + new_pic
        old_pic_path = image_in_path + '/' + pic_name
        print(old_pic_path+' -> '+new_pic_path)
        shutil.copyfile(old_pic_path, new_pic_path)
        i = i+1
            

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

wd = getcwd()
file_path = wd + '/label_old.txt' #这个路径是下载下来的label所存储动位置
out_path = wd +'/labels'
image_in_path = wd + '/Image_old' #这个路径是下载下来的图片存储动位置
image_out_path = wd + '/Images'
process(file_path, out_path, image_in_path, image_out_path)

