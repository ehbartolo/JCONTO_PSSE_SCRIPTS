# accc_1D.py - 4 MPjobs
from __future__ import print_function
#***************************************************
#***************************************************
#** Set paths, import modules, define run vars
#{----------------------------------------------------------------------------}
#import os, sys
#import time,datetime
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mpaccc_1d.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 'savnw'
#{----------------------------------------------------------------------------}
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
def DFXmake(subfile,monfile,confile,dfxfile,dxoption):
    import psspy
    ier = psspy.dfax(dxoption,subfile,monfile,confile,dfxfile)
    return ier
    
def ACCArun(tolerance,lfoption,DFXfile,ACCfile):
    import psspy
    #psspy.accc(0.5,[1, 0, 1, 1, 1, 0, 0],MyDFX,MyACC,"")
    ier = psspy.accc(tolerance,lfoption,DFXfile,ACCfile,"")
    return ier
##################################################################
# main:
#savfile = My['SAVFILE']
subfile = My['SUBFILE']
monfile = My['MONFILE']
confile = My['CONFILE']
#dfxfile = My['DFXFILE']
#accfile = My['ACCFILE']
dxoption  = My['DXOPTION']  
tolerance = My['TOLERANCE'] 
lfoption  = My['LFOPTION']  
iterations= My['ITERATIONS']
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #XYZ vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi   = zyxvars[0][0] 
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
#***************************************************
#** Set file names:
savfile  = '%s%s'%(xvarpath,My['XVAR'])
dfxfile  = '%s%s.dfx'%(My['ACCCPATH'],studyi)
accfile  = '%s%s.acc'%(My['ACCCPATH'],studyi)
logfile  = '%s%s.log'%(My['LOGSPATH'],studyi)
print ('case=',savfile)

#***************************************************
sys.stdout = open(logfile,'w') # redirect all prints to this log file
#___________________________________________________________
print ('****************************************************')
print ('   Scenario <%s>'%studyi)
print ('   %s - %s'%(My['TITLE1'], My['TITLE2']))
print ('')
print ('   {:%Y-%b-%d   %H:%M:%S}'.format(datetime.datetime.now()))
print ('****************************************************')
print ('')
#___________________________________________________________
# run a simulation:
print (zyxmsg)
ier =psspy.case(savfile)       # basecase name
if ier:
   print ('ERROR %s when loading '%ier,savfile)
#psspy.solv()
#prepare a DFX file
#if not os.path.isfile(dfxfile):
ier = DFXmake(subfile,monfile,confile,dfxfile,dxoption)
#update solution parameters
psspy.solution_parameters_2([_i,iterations,_i],
                            [_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f,_f]) # change iteration number to 40
#execute a ACCA run
ier = ACCArun(tolerance,lfoption,dfxfile,accfile)
if ier: print ('ERROR %s - in ACCArun'%ier)

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
