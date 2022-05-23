import os
import re
import sys

def text_create(name, msg):
    desktop_path = "D:\\22SS\\kal\\Argumentation\\"                       # the path for new .txt
    full_path = desktop_path + name + '.txt'                              # file search
    file = open(full_path, 'w')
    file.writelines(msg)                                                  # 
    # file.close()
 



def renameall():
	fileList = os.listdir(r"D:\22SS\kal\Argumentation\dataset")		                   #list - return all the filename into the list 
	print("before change ："+str(fileList))	                     	                   #return the original Name
	
	text_create('before change', fileList)                                             #修改内容
	
	currentpath = os.getcwd()		                                                   #得到进程当前工作目录
	os.chdir(r"D:\22SS\kal\Argumentation\dataset")		                  			   #将当前工作目录修改为待修改文件夹的位置
	num=1		                                               					       #名称变量
	for fileName in fileList:		                            				       #遍历文件夹中所有文件
		pat=".+\.(jpg|png|gif|py|txt)"		                      					   #匹配文件名正则表达式
		pattern = re.findall(pat,fileName)		                 					   #进行匹配
		os.rename(fileName,(str(num)+'.'+pattern[0]))		      					   #文件重新命名
		num = num+1		                                         					   #改变编号，继续下一项
	print("---------------------------------------------------")
	os.chdir(currentpath)		                                  					   #改回程序运行前的工作目录
	sys.stdin.flush()		                                                           #刷新
	Listdir = os.listdir(r"D:\22SS\kal\Argumentation\dataset")    					   #返回指定路径下的文件和文件夹列表名字（就是名字赋值给Listdir）
	print("修改后："+str(os.listdir(r"D:\22SS\kal\Argumentation\dataset")))		       #return the filename after changing
	text_create('修改后', Listdir) 
renameall()