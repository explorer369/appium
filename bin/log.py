# -*- encoding:GBK
import logging,os,sys
import ctypes
reload(sys)
sys.setdefaultencoding('GBK')
localpath = os.getcwd()
sys.path.append(localpath)
 
FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
 
STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool
 
 
class Logger:

    def __init__(self, path,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.logger = logging.getLogger(path)
        #  这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)
            fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
            #输出到cmd
            sh = logging.StreamHandler()
            sh.setFormatter(fmt)
            sh.setLevel(clevel)

            #输出到文件
            fh = logging.FileHandler(path)
            fh.setFormatter(fmt)
            fh.setLevel(Flevel)


            self.logger.addHandler(sh)
            self.logger.addHandler(fh)
            #self.logger.removeHandler(fh)
            #self.sh = sh
            #self.fh = fh

    def debug(self,message):
        self.logger.debug(message)

 
    def info(self,message):
        self.logger.info(message)
    def war(self,message,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(message)
        set_color(FOREGROUND_WHITE)
 
    def error(self,message,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(message)
        set_color(FOREGROUND_WHITE)
 
    def cri(self,message):
        self.logger.critical(message)



if __name__ =='__main__':
    logyyx = Logger('yyx.log',logging.WARNING,logging.DEBUG)
    logyyx.debug('???debug???')
    logyyx.info('???info???')
    logyyx.war('???warning???')
    logyyx.error('???error???')
    logyyx.cri('???????critical???')