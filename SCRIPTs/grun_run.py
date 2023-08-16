# run_grun.py - 4 mpjobs
from __future__ import print_function
# Grun activity does not works well if:
#		- machine does not have a governor model
#		- machine has status off
#		- machine has Pgen = 0.0
#   - non-gen modeled as gens (statcom,..)
#		
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
#ierr, My = JCtools.readIni('mpgrun.ini',My,1)
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
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #ZYX vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi   = zyxvars[0][0] 
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
#***************************************************
#** Set vars & file names:
Genx       = My['XVAR']
initloading= My['INITLOADING'] 
Pdelta     = My['PDELTA']      
outfile  = '%s%s.out'%(My['OUTSPATH'],studyi)
logfile  = '%s%s.log'%(My['LOGSPATH'],studyi)
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
# run a dynamic simulation:
print (zyxmsg)
psspy.case(My['CNVFILE'])
psspy.rstr(My['SNPFILE'])
psspy.dynamics_solution_params([My['ITERATION'],_i,_i,_i,_i,_i,_i,_i],
       [My['ACCELERATIONF'],_f, My['INTEGRATIONSTEP'],My['FREQFACTOR'] ,_f,_f, _f,_f],'')
if 'GENRELANG' in My:
   psspy.set_relang(1,My['GENRELANG'],str(My['GENIDRELANG']))
psspy.gstr(Genx,initloading,Pdelta,outfile)
psspy.grun(My['SIMTIME'],99,9,0)

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

