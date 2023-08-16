# Grun_pre.py - 4 mpjobs
from __future__ import print_function
#***************************************************
#** Set paths, import modules, define run vars
#import os, sys
#import time,datetime
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mperun.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 211
#***************************************************
debug = My['DEBUG']
if My['PYVER']>= 37:
   timeb = time.perf_counter()
else:
   timeb = time.clock()
exec('import psse{}'.format(My['PSSEVERSION']))
import psspy

if debug:
   print('Python ver %s'%sys.version) #parentheses necessary in python 3.
   print(psspy.psseversion())
   print(sys.executable)
   
with JCtools.redirect_stdout():     #to suppress PSSe message when loading
     if 'BUSDIM' in My:
         psspy.psseinit(My['BUSDIM'])
     else:
         psspy.psseinit()
#import redirect
#redirect.psse2py()
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
#__________________________________________________________________
if 'DEBUG' in My:
   zyxvars = JCtools.ZYXvars(My)    #ZYX vars=[[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
   studyi  = zyxvars[0][0] 
   logfile = '%s%s.log'%(My['LOGSPATH'],'grun_pre')
   sys.stdout = open(logfile,'w') # redirect all prints to this log file
   #___________________________________________________________
   print ('****************************************************')
   print ('   Scenario <%s>'%studyi)
   print ('   erun_pre.py logs')
   print ('')
   print ('   {:%Y-%b-%d   %H:%M:%S}'.format(datetime.datetime.now()))
   print ('****************************************************')
   print ('')
   #___________________________________________________________
for k in range(1):
    # Get the Gen buses:
    ier = psspy.case(My['SAVFILE'])
    if ier: 
       print ('ERROR %s loading savfile '%ier,My['SAVFILE'])
       break
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
    gendata = JCtools.subsystem_data(sid,'mach', ['NUMBER','ID'])
    genslst = []
    for gbus, id in gendata:
        if 'W' in id.upper(): continue
        genslst.append(gbus) 
    My['XVEC'] = genslst
