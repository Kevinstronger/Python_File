#coding=UTF-8
import os
#listdir(),返回当前目录的文件名
files = os.listdir(r'.')

#循环列表，获取每一个文件名
for filename in files:
    #查找文件名中‘.’的位置，并记录下来
    pos = filename.find('.')
    #判断文件名是否为html
    if filename[pos+1:] == 'html':
        #print filename[:pos+1]
        #重新组合新的文件名
        newname = filename[:pos+1]+'htm'
        #给文件更名
        os.rename(filename, newname)
for filelist in os.listdir('.'):
    #对中文文件名重新编码，显示为UTF-8格式
    print filelist.decode('GBK').encode('UTF-8')
    
#也可以使用splitext()，返回的是一个元组
for filename in os.listdir('.'):
    names = os.path.splitext(filename)
    
    if names[1] == '.html':
        names[0]+'.htm'
print os.listdir('.')
 
