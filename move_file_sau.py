# -*- coding:UTF-8 -*-
import os
import stat
import os
import shutil
import psutil

# def handle_remove_read_only(func, path, exc):
#     excvalue = exc[1]
#     if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
#       os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
#       func(path)
#     else:
#       raise

def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        try:
            if psutil.Process(pid).name() == processname:
                return pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

def updateAndCopyfile(srcPath, detPath):
    if not os.path.exists(srcPath):
        print "%s not exist!" % (srcPath)
    else:
        os.chdir('C:/Program Files/TortoiseSVN/bin')
        cmd = 'TortoiseProc.exe /command:revert /path ' + srcPath + ' /notempfile /closeonend:1'
        result = os.system(cmd)
        if result == 0:
            print('svn update succes')
        elif not os.path.exists(detPath):
            print "%s not exist!" % (srcPath)
        else:
            shutil.rmtree(detPath)
            shutil.copytree(srcPath, detPath)  
            print "copy %s -> %s" % (srcPath, detPath)

    
srcPath = 'E:/art22/gui'
detPath = 'D:/code_xj/res/gui'
if isinstance(checkprocess("Engine317.exe"), int):
    os.system('%s%s' % ("taskkill /F /IM ", 'Engine317.exe'))

updateAndCopyfile(srcPath, detPath)


