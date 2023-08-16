# run_faults2D.py - 4 mpjobs
from __future__ import print_function
#*************************************begin of single-run block**
# for single-run test: uncomment following code
#** Set paths, import modules, define run vars
#import os, sys
#import time
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mp2d.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 'SB1_b152.idv'
#My['YVAR'] = 'jc_flat33'
#************************************** end of single-run block**debug = My['DEBUG']
if My['PYVER']>= 37:
     timeb = time.perf_counter()
else:
     timeb = time.clock()
exec('import psse{}'.format(My['PSSEVERSION']))
import psspy
if debug:
    print('Python ver %s'%sys.version) #parentheses necessary in python 3.
    print (psspy.psseversion())
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
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
#** Set file names:
zyxvars  = JCtools.ZYXvars(My)		#XYZ vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi   = zyxvars[0][0]
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
yvarpath = zyxvars[2][0]
yvarkey  = zyxvars[2][1]
#***************************************************
cnvfile  = '%s%s_cnv.sav'%(yvarpath,yvarkey)
snpfile  = '%s%s.snp'%(yvarpath,yvarkey)
eventfile= '%s%s.idv'%(xvarpath,xvarkey)
outfile  = '%s%s.out'%(My['OUTSPATH'],studyi)
logfile  = '%s%s.log'%(My['LOGSPATH'],studyi)
#***************************************************
sys.stdout = open(logfile,'w') # redirect all prints to this log file
#___________________________________________________________
print ('****************************************************')
print ('   Scenario <%s>'%studyi)
print ('   %s - %s'%(My['TITLE1'], My['TITLE2']))
print ('')
if eventfile:
   print ('   event=%s'%eventfile)
print ('   {:%Y-%b-%d   %H:%M:%S}'.format(datetime.datetime.now()))
print ('****************************************************')
print ('')
#___________________________________________________________
# run a dynamic simulation:
print (zyxmsg)
psspy.case(cnvfile)
psspy.rstr(snpfile)

runscript(My['CHANNELS'])
psspy.dynamics_solution_param_2([My['ITERATION'],_i,_i,_i,_i,_i,_i,_i],
                                [My['ACCELERATIONF'],_f, My['INTEGRATIONSTEP'],My['FREQFACTOR'] ,_f,_f, _f,_f])
psspy.set_relang(1,My['GENRELANG'],str(My['GENIDRELANG']))
psspy.strt(0,outfile)
runscript(eventfile)
psspy.run(0,My['SIMTIME'],99,9,0)

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
