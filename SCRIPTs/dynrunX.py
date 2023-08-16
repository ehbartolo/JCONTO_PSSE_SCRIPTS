# dynrunX.py - 4 mpjobs
from __future__ import print_function
#*************************************begin of test single-run block**
# for single-run test: uncomment following code
#** Set paths, import modules, define run vars (set for PSSe 34 with python 3.7
try:
    My['MPTYPE']
    pass
except: 
    import os, sys
    import time,datetime
    pythoncode = 'SCRIPTs\\'
    if os.environ['PYTHONCODE']:
       pythoncode = os.environ['PYTHONCODE']
    sys.path.append(pythoncode)
    import JCtools
    My  = {}
    ierr, My = JCtools.readIni('cmld.ini',My,1)
    My['PYVER']= 37
    My['PSSEVERSION'] = 34
    My['XVAR'] = 'SB1_b152.idv'
#************************************** end of test single-run block**
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
#__________________________________________________________________
def runscript(myscript):
    import psspy
    if os.path.isfile(myscript):
       root,ext = os.path.splitext(myscript)
       if   ext.upper()=='.PY':
            exec(open(myscript).read())
       elif ext.upper()=='.IDV':  
            psspy.runrspnsfile(myscript)
       elif ext.upper()=='.IRF':  
            psspy.runiplanfile(myscript)

def varlstsort(varlst):
    outlst = []
    if JCtools.WhatType(varlst)=='LIST':
       outlst = varlst       
    elif '*' in os.path.basename(varlst):
       # addding all the varlst inside the LIBs folder
       vbname = os.path.basename(varlst)
       vpath  = os.path.dirname(varlst)
       outlst = JCtools.find_files(vbname,vpath)
    elif os.path.isfile(varlst):     #single file name
         outlst.append(varlst)
    return outlst

def systot():
    import psspy
    ierr, gen_tot = psspy.systot('GEN')
    ierr, load_tot= psspy.systot('LOAD')
    ierr, loss_tot= psspy.systot('LOSS')
    return [gen_tot,load_tot,loss_tot]
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #ZYX vars= [[studyi,study],[xvarpath,xvarkey],
                                  #                          [yvarpath,yvarkey],
                                  #                          [zvarpath,zvarkey],zyxmsg]
studyi   = zyxvars[0][0]          #= studyname_studytype_Zvar_Yvar_Xvar
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]          #= events\
xvarkey  = zyxvars[1][1]          #= SB1_b152
#print (zyxvars)
#***************************************************
# vars: passed in My
GenRelAng  = My['GENRELANG']              #=101
GenIDRelAng= My['GENIDRELANG']            #=1

Accelerationf  = My['ACCELERATIONF']      #=1.0
Integrationstep= My['INTEGRATIONSTEP']    #=0.0041667
Freqfactor     = My['FREQFACTOR']         #=0.01667
Iteration      = My['ITERATION']          #=99

prt2log = My['PRT2LOG']                   #=99
prt2out = My['PRT2OUT']                   #=9
prt2plt = My['PRT2PLT']                   #=0

event   = '%s%s'%(xvarpath,My['XVAR'])

savkey  = My['SAVKEY']

simtime = My['SIMTIME']
title1  = My['TITLE1'] 
title2  = My['TITLE2']
channels= My['CHANNELS']
if 'DYRADD' in My:
   dyradd = My['DYRADD']
else:
   dyradd = '' 
if 'DLLS' in My:
   dlls = My['DLLS']
else:
   dlls = ''
#_file names definition_______________________________
cnvfile = r"""%s_cnv.sav"""%savkey
snpfile = r"""%s.snp"""%savkey
outfile = '%s%s.out'%(My['OUTSPATH'],studyi)
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
logopen = 'w'
if 'LOGOPEN' in My:
    logopen = My['LOGOPEN'].lower()
status= ''
systot_start = ''
systot_end   = ''
#***************************************************
# run a dynamic simulation:
print (zyxmsg)
for k in range(1):
    if os.path.isfile(logfile) and logopen=='e':		#e= bypass run if log exist, w= overwrite, a= append
       status = 'Scenario <%s> was done or being processed!. Bypass now!'%studyi
       break
    if logopen=='e': logopen= 'w'
    sys.stdout = open(logfile, logopen) # redirect all prints to this log file
    print ('***************************************')
    print (' *  Scenario <%s>'%studyi)
    print (' *  %s - %s'%(title1, title2))
    print (' *')
    print (' *  event=%s'%event)
    print (' *  {:%Y-%b-%d   %H:%M:%S}'.format(datetime.datetime.now()))
    print ('***************************************')
    print ('')
  
    try:
        psspy.case(cnvfile)
    except:
        status = 'error while opening file:%s'%cnvfile
        break
    try:
        psspy.rstr(snpfile)
    except:
        status = 'error while opening file:%s'%snpfile
        break
    
    #=====================================================================================    
    # load DLLs'
    DLLlst = varlstsort(dlls)
    if DLLlst:
       for dllfile in DLLlst:
           dllerr = psspy.addmodellibrary('%s'%dllfile)
           if dllerr:
              status = " ERROR: %s Library NOT loaded\n"%dllfile
              break        
    #=====================================================================================    
    #add standard psse model not requiring compiling
    DYRlst = varlstsort(dyradd)
    if DYRlst:
       for dyr in DYRlst:
           err = psspy.dyre_add([_i,_i,_i,_i],dyr,"","")
           if err:
              status = " ERROR: %s dyr file NOT loaded\n"%dyr
              break                   
    #=====================================================================================    
    #add channels to run
    CHANlst = varlstsort(channels)
    if CHANlst:
       for CHANfile in CHANlst:
           err = runscript(CHANfile)
           if err:
              status = " ERROR: %s channel file NOT loaded\n"%CHANfile
              break
    #=====================================================================================    
    #apply default parameters to run
    psspy.dynamics_solution_params([Iteration,_i,_i,_i,_i,_i,_i,_i],
           [Accelerationf,_f,Integrationstep,Freqfactor,_f,_f, _f,_f],'')
    psspy.set_relang(1,GenRelAng,str(GenIDRelAng))
    #update basecase titles
    otitle1, otitle2 = psspy.titldt()
    psspy.case_title_data(otitle1,'%s - %s'%(otitle2,studyi))

    systot_start = systot()
    # initialize
    try:
        psspy.strt(1,outfile)
        psspy.run(0,0,99,9,0)
    except:
        status = ' error while initializing file: ',outfile
        break
    runscript(event)        #path included
    psspy.run(0,simtime,prt2log,prt2out,prt2plt)
    systot_end = systot()
if systot_end:
   systot_delta = [systot_end[0]-systot_start[0],systot_end[1]-systot_start[1],systot_end[2]-systot_start[2]]
   print ('\n              systot_start [P, Q]    systot_end [P, Q]    systot_delta [P, Q]')
   print (' gen_tot  = {0:>20.2f} {1:>20.2f}   {2:>20.2f}'.format(systot_start[0],systot_end[0],systot_delta[0]))
   print (' load_tot = {0:>20.2f} {1:>20.2f}   {2:>20.2f}'.format(systot_start[1],systot_end[1],systot_delta[1]))
   print (' loss_tot = {0:>20.2f} {1:>20.2f}   {2:>20.2f}'.format(systot_start[2],systot_end[2],systot_delta[2]))
print (status)

if My['PYVER']>=37:
   timee = time.perf_counter()
else:
   timee = time.clock()  
deltasecstr = '%10.2f'%(timee-timeb)
deltasec = float(deltasecstr)
My['RETURN'] = [deltasec,studyi]
byebye = '    Scenario %s completed in %10.2f sec.'%(studyi,timee-timeb)
print (byebye)
sys.stdout.close()                # ordinary file object
sys.stdout = sys.__stdout__
print (byebye)

