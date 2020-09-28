# -*- coding:UTF-8 -*-
import os
import stat
import shutil
import psutil
import sys

# def handle_remove_read_only(func, path, exc):
#     excvalue = exc[1]
#     if func in (os.rmdir, os.remove, os.unlink) and excvalue.errno == errno.EACCES:
#       os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  # 0777
#       func(path)
#     else:
#       raise
files = [
    '/Animation',
    '/badam_ui',
    '/fonts',
]

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
        os.chdir(srcPath)
        cmd = 'svn update'
        result = os.system(cmd)

        if result == 0:
            print('svn update succes')
            if os.path.exists(detPath):
                shutil.rmtree(detPath)
            shutil.copytree(srcPath, detPath)  
            print "copy %s -> %s" % (srcPath, detPath)

    
    

def main():
    srcPath = sys.argv[1]
    detPath = sys.argv[2]

    if isinstance(checkprocess("Engine317.exe"), int):
        os.system('%s%s' % ("taskkill /F /IM ", 'Engine317.exe'))

    for pathName in files:
        updateAndCopyfile(srcPath + pathName, detPath + pathName)

if __name__ == "__main__":
    main()
