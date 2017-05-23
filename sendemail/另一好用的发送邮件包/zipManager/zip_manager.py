 #coding=utf-8

'''
压缩文件夹，生成zip文件
'''

import os,zipfile
from os.path import join
from datetime import date
from time import time
import traceback

# 解决乱码问题
import sys
reload(sys)
SYS_ENCODING = 'cp936'  # 定义系统编码
sys.setdefaultencoding(SYS_ENCODING)  # 设置默认编码

class ZipManager:
    '''
    zip the given folder automatically
    '''

    def __init__(self):
        ' 构造函数 '
        pass

    @staticmethod
    def zip_dir(dirname,zipfilename):
        ' 压缩指定文件夹 '
        filelist = []
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else :
            for root, dirs, files in os.walk(dirname):
                for name in files:
                    # hard code，原有压缩文件跳过
                    if name.endswith('.zip'):
                        continue
                    # hard code end
                    filelist.append(os.path.join(root, name))

        zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname = tar[len(dirname):]
            #print arcname
            zf.write(tar,arcname)
        zf.close()

    @staticmethod
    def unzip_file(zipfilename, unziptodir):
        ' 解压缩指定文件夹 '
        if not os.path.exists(unziptodir): os.mkdir(unziptodir, 0777)
        zfobj = zipfile.ZipFile(zipfilename)
        for name in zfobj.namelist():
            name = name.replace('\\','/')

            if name.endswith('/'):
                os.mkdir(os.path.join(unziptodir, name))
            else:
                ext_filename = os.path.join(unziptodir, name)
                ext_dir= os.path.dirname(ext_filename)
                if not os.path.exists(ext_dir) : os.mkdir(ext_dir,0777)
                outfile = open(ext_filename, 'wb')
                outfile.write(zfobj.read(name))
                outfile.close()


# 测试函数
if __name__ == "__main__":
    folder = r'D:\ruansz\code\python\codeManager\zipManager\test'
    filename = 'test.zip'
    dirbase = r'test'
    targetbase = 'D:'+'/'

    ZipManager.zip_folder( folder, filename, dirbase=dirbase)