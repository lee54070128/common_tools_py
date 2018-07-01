#!/usr/bin python
#encoding:utf-8

import urllib
#import urllib2
#import requests 
import os

'''
#本文件提供了一系列下载的方法
'''

def Schedule(a,b,c):
    '''''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
   '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print ('%.2f%%' % per)

#显示进度的下载方法，使用urllib
def download_with_urllib(url_path,local_path):
    print ("downloading with urllib...")
    urllib.urlretrieve(url_path,local_path,Schedule)

#小文件下载，第二种下载方法，使用urllib2
def download_tinyfile_with_urllib2(url_path,local_path):
    print ("downloading with urllib2...")
    f = urllib2.urlopen(url_path) 
    data = f.read() #如果是下载大文件，可以限定一次读取的数据长度，使用循环读取
    with open(local_path, "wb") as code:     
        code.write(data)

#小文件下载，第三种下载方法,使用requests库
def download_tinyfile_with_requests(url_path,local_path):
    print ("downloading with requests...")
    r = requests.get(url_path) 
    with open(local_path, "wb") as code:
         code.write(r.content)

##大文件下载，第三种下载方法,使用requests库
def download_largefile_with_requests(url_path,local_path):
    print ("downloading with requests...")
    r = requests.get(url_pat,stream=True) 
    with open(local_path, "wb") as code:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                code.write(chunk)

#批量下载网页中的文件，可以先解析网页，提取出要下载的文件路径，然后再一次下载
#或者可以把要下载的文件列表存入文件，然后下载

         
#同时下载文件最大个数
MAX_NUM = 3
        
if __name__ == '__main__':
    pwd = os.getcwd()
    with open('filelist.txt') as f:
        for file in f.readlines():
            filename=file.split('?')[0].split('/')[-1]
            print ('开始下载文件%s...' %filename)
            download_with_urllib(file,filename)
            
