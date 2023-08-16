# run_QV1D_pre.py - 4 mpjobs
from __future__ import print_function
#***************************************************
#** Set paths, import modules, define run vars
#import os, sys
#sys.path.append('SCRIPTs\\')
#import JCtools_p27 as JCtools
#My = {}
#ier, My = JCtools.readIni('mpQV.ini',My,1)
# for PSSe v>= 33
#***************************************************
import JCtools
debug = My['DEBUG']
if My['PYVER']>= 37:
   timeb = time.perf_counter()
else:
   timeb = time.clock()
exec('import psse{}'.format(My['PSSEVERSION']))
import psspy
#import redirect
#redirect.psse2py()
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
#for key,val in My.items():
#    print ('%s = %s'%(key,val))
if debug:
    print('Python ver %s'%sys.version) #parentheses necessary in python 3.
    print (psspy.psseversion())
    print(sys.executable)

with JCtools.redirect_stdout():     #to suppress PSSe message when loading
     if 'BUSDIM' in My:
         psspy.psseinit(My['BUSDIM'])
     else:
         psspy.psseinit()
#__________________________________________________________________
def loadbustotal(loadlst):
    '''
    input loadlst: [['1',100,1,2,3],['1',102,1,2,3],['2',102,1,2,3]]
                     id,lbus,A, Z, O
    return: case is modified with load aggregated
    '''
    import psspy
    _i = psspy.getdefaultint()
    aloadlst = []
    busprev = 0
    multiple = False
    for lid,lbus,ai,zi,oi in loadlst:
        if not aloadlst:
           aloadlst.append([lbus,lid])
           busprev = lbus
           continue
        elif lbus == busprev:
             aloadlst.append([lbus,lid])
             multiple = True
             continue
        else:
           if multiple:
              # aggregate the loads
              Pt = 0.0
              Qt = 0.0
              Ip = 0.0
              Iq = 0.0
              Yp = 0.0
              Yq = 0.0
              for lbusx,lidx in aloadlst:
                  ierr, cmpval = psspy.loddt2(lbusx,lidx,'MVA','NOM')
                  Pt += cmpval.real
                  Qt += cmpval.imag
                  ierr, cmpval = psspy.loddt2(lbusx,lidx,'IL','NOM')
                  Ip += cmpval.real
                  Iq += cmpval.imag
                  ierr, cmpval = psspy.loddt2(lbusx,lidx,'YL','NOM')
                  Yp += cmpval.real
                  Yq += cmpval.imag
              with JCtools.redirect_stdout():     #to suppress PSSe message when loading
                   ierr = psspy.purgloads(lbusx)
              #add new aggregated load
              idx = 'a%s'%len(aloadlst)
              intgar = [_i,ai,zi,oi,_i,_i]
              realar = [Pt,Qt,Ip,Iq,Yp,Yq]
              with JCtools.redirect_stdout():     #to suppress PSSe message when loading
                   ierr = psspy.load_data_4(lbusx,idx,intgar,realar)
              multiple = False
           #clear list and add lbus
           aloadlst= []
           aloadlst.append([lbus,lid])
           busprev = lbus
    return
#__________________________________________________________________
#** Set file names:
#if 'DEBUG' in My:
#    logfile  = '%s%s.log'%(My['LOGSPATH'],'QV1D_pre')
#    psspy.progress_output(2,logfile,[0,0])
#    psspy.prompt_output(2,logfile,[0,0])
#***************************************************
for k in range(1):
    #with JCtools.redirect_stdout():     #to suppress PSSe message when loading
    ier = psspy.case(My['SAVFILE'])
    if ier: 
       print ('ERROR %s loading savfile '%ier,My['SAVFILE'])
       break
    # get a list of gen's remote control buses
    controlbus = []
    gendata = JCtools.subsystem_data(-1,'genbus', ['NUMBER','IREG'])
    for bus,ireg in gendata:
       if ireg not in controlbus:
           controlbus.append(ireg)

    swshdata = JCtools.subsystem_data(-1,'swsh', ['NUMBER','STATUS','IREG'])
    for bus,status,ireg in swshdata:
        if ireg not in controlbus:
           controlbus.append(ireg)

    # Get the load buses for a QV simulation:
    sid    = int(My['SID'])
    basekv = My['BASEKV']
    areas  = My['AREAS']
    buses  = My['BUSES']
    owners = My['OWNERS']
    zones  = My['ZONES']
    inservice = My['INSERVICE']
    ier = JCtools.bsyset(sid=sid,basekv=basekv,areas=areas,buses=buses,owners=owners,zones=zones)
    if ier:
       print ('ERROR in bsyset, subsystem sid %s NOT creted.'%sid)
       break
    loadata = JCtools.subsystem_data(sid,'load', ['ID','NUMBER','AREA','ZONE','OWNER'])
    loadbustotal(loadata)   #update case with aggregated loads
    loadbus = JCtools.subsystem_data(sid,'load', ['NUMBER'])
    My['XVEC'] = []
    for bus in loadbus:
        if controlbus:
           if bus in controlbus: continue       #by-pass it - QV cannot be done at controlled buses
        My['XVEC'].append(bus)

