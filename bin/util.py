# -*- encoding: utf-8 -*-
import logging,os,threading
import log
logger = log.Logger('TestResult/log_util.log', clevel = logging.DEBUG, Flevel = logging.INFO)   # 在rst下创建一个log文件 用logger调用时全部所写的日志全记录到此LOG文件
def exccmd(cmd):
    try:
        return os.popen(cmd).read()    # 读取CMD命令结果的值返回
    except Exception:                  # 捕获异常，返回None
        return None
     
#遍历目录内的文件列表
def listFile(path, isDeep=True):
    _list = []
    if isDeep:
        try:
            for root, dirs, files in os.walk(path):
                for fl in files:
                    _list.append('%s\%s' % (root, fl))
        except:
            pass
    else:
        for fn in glob.glob( path + os.sep + '*' ):
            if not os.path.isdir(fn):
                _list.append('%s' % path + os.sep + fn[fn.rfind('\\')+1:])
    return _list
     
#线程函数
class FuncThread(threading.Thread):
    def __init__(self, func, *params, **paramMap):
        threading.Thread.__init__(self)
        self.func = func
        self.params = params
        self.paramMap = paramMap
        self.rst = None
        self.finished = False
 
    def run(self):
        self.rst = self.func(*self.params, **self.paramMap)
        self.finished = True
 
    def getResult(self):
        return self.rst
 
    def isFinished(self):
        return self.finished
 
def doInThread(func, *params, **paramMap):
    t_setDaemon = None
    if 't_setDaemon' in paramMap:
        t_setDaemon = paramMap['t_setDaemon']
        del paramMap['t_setDaemon']
    ft = FuncThread(func, *params, **paramMap)
    if t_setDaemon != None:
        ft.setDaemon(t_setDaemon)
    ft.start()
    return ft