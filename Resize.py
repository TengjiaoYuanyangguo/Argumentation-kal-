

import os
import cv2 

base_path='D:\\22SS\\kal\\Argumentation\\dataset'              ##This is path for Windows,without \\ at the end
for fileList in os.listdir(base_path):
    print(fileList)
    image_path = base_path+'\\'+fileList                       ##path combination 
    image=cv2.imread(image_path) 
    res=cv2.resize(image,(300,300),interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(image_path, res)                                       #don't hold and resize the original Image 
