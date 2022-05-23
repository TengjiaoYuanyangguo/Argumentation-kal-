import numpy as np
from PIL import Image
import os
from numpy import *
import cv2  #导入openCV
input_dir = r'D:\\22SS\\kal\\dataset\\benchmark_images\\benchmark_images\\Yield\\VehicleRight\\'  #文件夹名字后一定要加/，才能识别为打开文件夹中的内容
out_dir1 = r'D:\\22SS\\kal\\dataset\\benchmark_images\\1benchmark\\Yield\\VR\\Gray\\'             #进行灰度化后的图片保存在该文件夹下
out_dir2 = r'D:\\22SS\\kal\\dataset\\benchmark_images\\1benchmark\\Yield\\VR\\Nor\\'              #进行灰度化和归一化后的图片保存在该文件夹下

#3.1灰度化
a = os.listdir(input_dir)
for i in a:    
    print(i)
    Img = Image.open(input_dir + i)                                                               #用PIL的库来逐个读取图片
    Img_gray = Img.convert('L')                                                                   #灰度化L
    Img_gray.save( out_dir1 + i)                                                                  #用PIL的库来逐个保存图片到指定路径下
    print('~~~~~~~~~~~~~This is a picture after graying~~~~~~~~~~')
    print(Img_gray)

#3.2对上述灰度化后的Img_gray进行归一化
b = os.listdir(out_dir1)
for j in b:
    print(j)
    photo = cv2.imread(out_dir1  + j)
 #cv2.imread()接口读图像，读进来直接是BGR 格式数据格式在 0~255，通道格式为(W,H,C)
    result = np.zeros(photo.shape, dtype=np.float32) 
    cv2.normalize(photo, result, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F, mask=None)
    print('~~~~~~~~~~This is data of BGR after normalizing : ~~~~~~~~~~~~~~~~~~')
    print(result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    Img_output = Image.fromarray(np.uint8(result))  # 将array恢复成图片 Img_output，不能直接把result保存在文件夹里。
    Img_output.save(out_dir2 + j)  #将归一化后的图片保存在指定路径下
    
    #3.3下面将以上每张图归一化后的数据保存下项目文件夹下的 txtfile.txt 中
    #fname = open(r"D:\\22SS\\kal\\dataset\\benchmark_images\\1benchmark\\NoSign\\Vleft\\DataVl.txt", 'a') #a是向txt中追加写入
    #fname.write("Name of the Picture:" + str(j) + '\n')
    #fname.write("图像的形状,返回一个图像的(行数,列数,通道数):" + str(result.shape) + '\n')
    #fname.write("图像的像素数目:"+str(result.size)+'\n')
    #fname.write("图像的数据类型:"+str(result.dtype)+'\n')
    #Xlenth = result.shape[1]  #图片列数
    #Ylenth = result.shape[0]  #图片行数
    
    #m = 1
    #for p in range(Ylenth):  #外循环是行
    #    fname.write(str(m) + ':'+'\n')
    #    for q in range(Xlenth):   #内循环是列
    #        fname.write(str(result[p][q])+' ')
    #    m += 1
    #    fname.write('\n')
    #fname.close()
#————————————————
#版权声明：本文为CSDN博主「米开朗km」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
#原文链接：https://blog.csdn.net/qq_35328403/article/details/105352525