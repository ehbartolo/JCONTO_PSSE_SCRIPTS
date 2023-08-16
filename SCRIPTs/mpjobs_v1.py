# -*- coding: utf-8 -*-
# mpjobs.py - v.20150415
# Copyrighted by José Conto, 2015
import os, sys
import multiprocessing
import logging
import time
#{----------------------------------------------------------------------------}
sys.path.append('SCRIPTs\\')
import JCtools
#{----------------------------------------------------------------------------}
def run_py(My):
    #call py code to exec a single process run
    execfile(My['SCRIPT'],globals(),locals())
    sys.stdout.flush()
    return My['RETURN']
    
resulst = []
def call_back(result):
    # This is called whenever run_py returns a result.
    # resulst is modified only by the main process, not by the pool workers.
    resulst.append(result)

def main():
    time0 = time.clock()
    INIfile = JCtools.arg1()
    My = JCtools.readIni(INIfile)
    if My.has_key('CPU'):
       pool= multiprocessing.Pool(processes=My['CPU'])
    else:
       pool= multiprocessing.Pool()
    #multiprocessing.log_to_stderr(logging.DEBUG)
    #multiprocessing.log_to_stderr()
    #logger = multiprocessing.get_logger()
    #logger.setLevel(logging.INFO)
    
    My['ZVEC'],My['YVEC'],My['XVEC']= JCtools.ZYXvecs(My)
          
    if My.has_key('PRESCRIPT'):
       #call py code to exec a single process run
       execfile(My['PRESCRIPT'],globals(),locals())
       sys.stdout.flush()
    if not My['XVEC']:
       print 'ERROR: main variable file %s does not exist.'%My['XFILE']
       return
    #__________________________________________________________
    for zvar in My['ZVEC']:
        if zvar: My['ZVAR'] = zvar
        for yvar in My['YVEC']:
            if yvar: My['YVAR'] = yvar
            for xvar in My['XVEC']:
                My['XVAR'] = xvar
                pool.apply_async(run_py, args = (My, ), callback = call_back)
                if My.has_key('POOLDELAY'):
                   time.sleep(My['POOLDELAY'])
                else:
                   time.sleep(1)
    pool.close()
    pool.join()
    sys.stdout.flush()
    print("--- MPjobs completed - %.3f seconds ---" % (time.clock() - time0))
    My['TRUNS'] = len(resulst)
    if My['DEBUG']: 
       for x in resulst: print x
    #__________________________________________________________
    # main parallel computation are done. Run final py script
    if My.has_key('POSTSCRIPT'):
       #call py code to exec a single process run
       execfile(My['POSTSCRIPT'],globals(),locals())
       sys.stdout.flush()

if __name__ == '__main__':
   main()
