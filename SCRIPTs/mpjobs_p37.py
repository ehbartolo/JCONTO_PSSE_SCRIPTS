# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: mpjobs.py
# Compiled at: 2021-06-28 18:54:55
# Size of source mod 2**32: 10428 bytes
from __future__ import print_function
import os, sys, time, datetime, multiprocessing as mp
if sys.argv[(-1)] == '-d':
    debug = 1
    sys.argv.pop()
else:
    debug = 0
prgversion = '20201103'
pythoncode = 'scripts\\\\'
if os.path.isdir(pythoncode):
    pythoncode = os.path.abspath(pythoncode)
    if pythoncode not in sys.path:
        sys.path.insert(0, pythoncode)
import JCtools
resulst = []
My = {}
INIfile = JCtools.argINI()
ier, My = JCtools.readIni(INIfile, My, debug)
if ier:
    quit()
else:
    if 'DEBUG' in My:
        debug = My['DEBUG']
    else:
        My['DEBUG'] = debug
    if 'PSSEPATH' in My or 'PSSPYPATH' in My:
        if 'PSSPYPATH' not in My:
            My['PSSPYPATH'] = My['PSSEPATH']
        My['PSSEVERSION'] = JCtools.psseversion(My['PSSPYPATH'])
        My['PYVER'] = JCtools.psspyver(My['PSSPYPATH'])
    else:
        My['PSSEVERSION'] = int(os.environ['PSSEVERSION'])
    My['PYVER'] = int(os.environ['PYVER'])
My['STUDY'] = JCtools.getStudy(My)

def title(version):
    print(chr(223) * 60)
    print('                       MPjobs                  v.%s' % version)
    print('           python parallel processing engine')
    print('  Copyright - Jos%s Conto, Jan. 2015 - All rights reserved' % chr(130))
    print(chr(220) * 60)
    print('')


def title37(version):
    print(chr(223) * 60)
    print('                       MPjobs                  v.%s' % version)
    print('           python parallel processing engine')
    print('  Copyright - Jos%s Conto, Jan. 2015 - All rights reserved' % chr(233))
    print(chr(220) * 60)
    print('')


def run_mpaa(My):
    exec(open(My['SCRIPT']).read())
    sys.stdout.flush()
    return My['RETURN']


def call_back(result):
    global resulst
    resulst.append(result)


def run_mpp(My, lock, out_q):
    vectorlst = My['MPPVEC'][My['PI']]
    My['RUNI'] = 0
    tmpdict = {}
    for xvar in vectorlst:
        if My['PYVER'] >= 37:
            timei = time.perf_counter()
        else:
            timei = time.clock()
        My['XVAR'] = xvar
        My['XVARROOT'] = xvar
        if 'XFILE' in My:
            filenameDic = JCtools.fnameDic(xvar)
            My['XVARROOT'] = filenameDic['ROOT']
        else:
            My['RUNI'] += 1
            lock.acquire()
            exec(open(My['SCRIPT']).read())
            lock.release()
            if 'POOLDELAY' in My:
                time.sleep(My['POOLDELAY'])
            if My['PYVER'] >= 37:
                timef = time.perf_counter()
            else:
                timef = time.clock()
        timedeltastr = '%10.2f' % (timef - timei)
        result = My['RETURN']
        tmpdict[xvar] = (My['PI'], My['RUNI'], float(timedeltastr), result)

    out_q.put(tmpdict)


def main():
    global debug
    resultdict = {}
    My['RETURN'] = []
    if My['PYVER'] >= 37:
        time1 = time.perf_counter()
        title37(prgversion)
    else:
        time1 = time.clock()
        title(prgversion)
    if 'MPTYPE' in My:
        mptype = My['MPTYPE'].upper()
    else:
        mptype = 'MPP'
        My['MPTYPE'] = mptype
        out_q = mp.Queue()
    CPUmax = mp.cpu_count()
    if 'CPU' not in My:
        My['CPU'] = CPUmax
    else:
        if My['CPU'] == 0:
            My['CPU'] = 1
        else:
            if My['CPU'] < 0:
                My['CPU'] += CPUmax
                if My['CPU'] < 0:
                    My['CPU'] = CPUmax - 1
                else:
                    if My['CPU'] > CPUmax:
                        My['CPU'] = CPUmax
                    else:
                        My['ZVEC'], My['YVEC'], My['XVEC'] = JCtools.ZYXvecs(My)
                        if debug:
                            if My['ZVEC']:
                                print("My['ZVEC']=", My['ZVEC'])
                            if My['YVEC']:
                                print("My['YVEC']=", My['YVEC'])
                            if My['XVEC']:
                                print("My['XVEC']=", My['XVEC'])
                njob = JCtools.ZYXcount(My)[0]
                if njob > 0:
                    if njob < My['CPU']:
                        My['CPU'] = njob
            else:
                if mptype == 'MPAA':
                    pool = mp.Pool(processes=(My['CPU']))
                else:
                    My['RUNI'] = 0
                    if 'PRESCRIPTZ' in My:
                        exec(open(My['PRESCRIPTZ']).read())
                        sys.stdout.flush()
                    for zvar in My['ZVEC']:
                        if zvar:
                            My['ZVAR'] = zvar
                        else:
                            if isinstance(zvar, int) or isinstance(zvar, float):
                                My['ZVAR'] = zvar
                            if 'PRESCRIPTY' in My:
                                exec(open(My['PRESCRIPTY']).read())
                                sys.stdout.flush()
                            for yvar in My['YVEC']:
                                if yvar:
                                    My['YVAR'] = yvar
                                else:
                                    if not isinstance(yvar, int):
                                        if isinstance(yvar, float):
                                            My['YVAR'] = yvar
                                        if 'PRESCRIPT' in My:
                                            My['PRESCRIPTX'] = My['PRESCRIPT']
                                        if 'PRESCRIPTX' in My:
                                            exec(open(My['PRESCRIPTX']).read())
                                            sys.stdout.flush()
                                        if mptype == 'MPP':
                                            lock = mp.Lock()
                                            My['MPPVEC'] = JCtools.vectorpx(My['XVEC'], My['CPU'])
                                            pp = []
                                            for pi in range(My['CPU']):
                                                My['PI'] = pi
                                                print('\nProcessing MPP group %s' % My['PI'])
                                                pp.append(None)
                                                pp[pi] = mp.Process(target=run_mpp, args=(My, lock, out_q))
                                                pp[pi].start()

                                            for i in range(My['CPU']):
                                                resultdict.update(out_q.get())

                                            for pi in range(My['CPU']):
                                                pp[pi].join()

                                    else:
                                        for xvar in My['XVEC']:
                                            if xvar:
                                                My['XVAR'] = xvar
                                            else:
                                                if isinstance(xvar, int) or isinstance(xvar, float):
                                                    My['XVAR'] = xvar
                                                My['RUNI'] += 1
                                                zyxvars = JCtools.ZYXvars(My)
                                                studyi = zyxvars[0][0]
                                                print('processing MPAA run %s, %s' % (My['RUNI'], studyi))
                                                pool.apply_async(run_mpaa, args=(
                                                 My,),
                                                  callback=call_back)
                                            if 'POOLDELAY' in My:
                                                time.sleep(My['POOLDELAY'])

                                    sys.stdout.flush()

                    if mptype == 'MPAA':
                        pool.close()
                        pool.join()
                        sys.stdout.flush()
                        k = -1
                        for x in resulst:
                            if not x:
                                continue
                            k += 1
                            if JCtools.WhatType(x) != 'LIST':
                                resultdict[k] = x
                            else:
                                if len(x) < 2:
                                    x.insert(0, k)
                                resultdict[x[0]] = x[1]

                    if 'POSTSCRIPT' in My:
                        exec(open(My['POSTSCRIPT']).read())
                        sys.stdout.flush()
                    if My['PYVER'] >= 37:
                        time2 = time.perf_counter()
                    else:
                        time2 = time.clock()
                print('\n--- mpjobs [%s] finished in %10.2f seconds ---' % (mptype, time2 - time1))
                if debug:
                    if mptype == 'MPP':
                        print('XVAR, Pi, runi, time, [Return]')
                    else:
                        print('[Return]')
            if resultdict:
                for key, val in resultdict.items():
                    print('%s, %s' % (key, val))

            return resultdict


if __name__ == '__main__':
    main()