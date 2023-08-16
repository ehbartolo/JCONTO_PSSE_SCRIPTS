# QV2D.py - 4 mpjobs
from __future__ import print_function
#***************************************************
#** Set paths, import modules, define run vars
#import os, sys
#import time
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mpQV_2d.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 154
#***************************************************
debug = My['DEBUG']
if My['PYVER']>= 37:
   timeb = time.perf_counter()
else:
   timeb = time.clock()
exec('import psse{}'.format(My['PSSEVERSION']))
import psspy
import pssarrays
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
    ierr = psspy.dfax(dxoption,subfile,monfile,confile,dfxfile)
    return ierr
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #ZYX vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi   = zyxvars[0][0] 
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
yvarpath = zyxvars[2][0]
yvarkey  = zyxvars[2][1]

#***************************************************
#** Set file names:
busid = My['XVAR']
savfile = '%s\\%s.sav'%(yvarpath,yvarkey)
dfxfile = '%s\\%s.dfx'%(yvarpath,yvarkey)
qvfile  = '%s%s.qv'%(My['OUTSPATH'],studyi)
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
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
#------------------------------------------------------------------------------------------------
subfile = My['SUBFILE']    
monfile = My['MONFILE']    
confile = My['CONFILE']
if 'QVFILE' in My:   
    qvfile = My['QVFILE']
thrfile = My['THRFILE']        # Load Throwover Data file; blank for none
inlfile = My['INLFILE']        # Inertia and Governor Response Data file; blank for none
sublabel= My['SUBLABEL']       #label of the dispatch subsystem; used if OPTIONS(12) is 1 through 4 (blank by default).
zipfile = My['ZIPFILE']        #ZIP Archive Output File (input; blank by default)
dfxoptions = My['DFXOPTIONS']

lfoption4  = My['LFOPTION4']
#lfoption4 = [0,0,0,0,0,1,1,0,1,0,busid,0,0]
lfoption4[-3] = busid
qvoption  = My['QVOPTION']
#----------------------------------------------------------------------------------------------------
#main:
for k in range(1):
    with JCtools.redirect_stdout():     #to suppress PSSe message when loading
    ier = psspy.case(savfile)
    if ier:
       print ('ERROR - when loading base case ',savfile)
       break
    if not os.path.isfile(dfxfile):
       DFXmake(subfile, monfile, confile, dfxfile, dfxoptions)
       if ier:
          print ('ERROR - in DFXmake')
          break
       
    major = My['PSSEVERSION']
    if   major <= 32:
         ierr = psspy.qv_engine(lfoption, qvoption, dfxfile, thrfile, qvfile)
    else:       #major >= 33:
         #ierr = psspy.qv_engine_2(lfoption2, qvoption, dfxfile, thrfile, qvfile)
         #ierr = psspy.qv_engine_3(lfoption3, qvoption, sublabel, dfxfile, thrfile, inlfile, qvfile)
         ierr = psspy.qv_engine_4(lfoption4, qvoption, sublabel, dfxfile, thrfile, inlfile, qvfile, zipfile)
    if ier:
       print ('ERROR - in making QV file')
       break
    # ====================================================================================================
    if 'DORPT_SUMMARY' in My:
        rptfile = '%sqv_%s_summary.dat'%(My['OUTSPATH'],studyi)
        ierr = pssarrays.qv_summary_report(qvfile,rptfile)                     #works!
        if ierr>0: 
           print ('qv_summary_report error ',ierr)
    ##
    if 'DORPT_SOLUTION' in My:
        colabels = My['COLABELS']           #''           #<- all ctgs
        rptfile = '%sqv_%s.dat'%(My['OUTSPATH'],studyi)
        ierr = pssarrays.qv_solution_report(qvfile,colabels,rptfile)           #works!
        if ierr>0: 
           print ('qv_solution_report error ',ierr)

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

# ====================================================================================================
#get QV run data output using pssarrays
#     qv_solution(qvfile=None, colabel=None)
#         rlst = qv_solution(qvfile,colabel)
#         QV analysis monitored flows and bus voltages for one contingency.
#         Inputs:
#             qvfile  = QV output file name (.qv)
#             colabel = contingency label (to get QV solution for)
#                       only one contingency label allowed
#         Returned object 'rlst' contains the following attributes:
#             rlst.ierr       = error code(0=no error)
#             rlst.island     = number of islands, integer
#             rlst.vsetpoint  = voltage setpoints, float of length [nvstp]
#             rlst.cnvflag    = convergence flag (True when converged), logical of length [nvstp]
#             rlst.cnvcond    = convergence condition
#             rlst.mvaworst   = larget bus MVA mismatch, float of length [nvstp]
#             rlst.mvatotal   = total system MVA mismatch, float of length [nvstp]
#             rlst.volts      = monitored bus voltage (pu), float of length [nmvbus][nvstp]
#             rlst.mgenmvar   = monitored plant Mvar, float of length [nmgnbus][nvstp]
# 
#             where
#             ntrans  = number of voltage setpoint changes
#             nmvbus  = number of voltage monitored buses
#             nmgnbus = number of monitored plant (generator) buses
# 
#     qv_summary(qvfile=None)
#         rlst = qv_summary(qvfile)
#         Returns QV analysis summary.
#         Inputs:
#             qvfile = QV output file name (.qv)
#         Returned object 'rlst' contains the following attributes:
#             rlst.ierr             = error code (0=no error)
#             rlst.qvbus            = QV analysis bus name
#             rlst.qvsize.ncase     = number of contingencies + 1 (for base case)
#             rlst.qvsize.nmvbus    = number of voltage monitored buses
#             rlst.qvsize.nmvrec    = number of voltage monitored records
#             rlst.qvsize.nmgnbus   = number of monitored plant (generator) buses
#             rlst.qvsize.nmxvstp   = maximum number of voltage setpoint changes
#             rlst.options          = QV solution options (same as in API manual)
#             rlst.values           = QV solution values (same as in API manual)
#             rlst.casetitle.line1  = short title line 1
#             rlst.casetitle.line2  = short title line 2
#             rlst.file.qv          = contingency output (.acc) file name
#             rlst.file.sav         = saved case (.sav) file name
#             rlst.file.thr         = load throwover data (.thr) file name
#             rlst.file.dfx         = distribution factor data (.dfx) file name
#             rlst.file.sub         = subsystem definition data (.sub) file name
#             rlst.file.mon         = monitored element data (.mon) file name
#             rlst.file.con         = contingency description data (.con) file name
#             rlst.mgenbus          = monitored plant (generator) bus label
#             rlst.mvbuslabel       = monitored voltage bus label
#             rlst.mvreclabel       = monitored voltage record label
#             rlst.mvrecmax         = monitored voltage bus maximum
#             rlst.mvrecmin         = monitored voltage bus minimum
#             rlst.mvrectype        = monitored voltage record type (range/deviation)
#             rlst.colabel          = contingency labels
#             rlst.codesc           = contingency description
#             rlst.minvstp          = minimum voltage setpoint
#             rlst.maxvstp          = maximum voltage setpoint
#             rlst.minmvar          = minimum MVAR change
#             rlst.maxmvar          = maximum MVAR change
#             rlst.maxmsm           = maximum MVAR mismatch
# 
#     qv_solution_report(qvfile=None, colabels=None, rptfile=None)
#         ierr = qv_solution_report(qvfile,colabels,rptfile)
#         QV analysis solution text report.
#         Inputs:
#             qvfile   = QV output file name (.qv)
#             colabels = contingency labels (to get QV solution)
#                        default "all contingencies"
#                        for more than one contingency, provide as a list or tuple
#             rptfile  = report text file name (to write solution report)
#                        default "PSS(R)E Report"
#         Returns ierr.
#             ierr     = 0, no error
# 
#     qv_summary_report(qvfile=None, rptfile=None)
#         ierr = qv_summary_report(qvfile,rptfile)
#         QV analysis summary text report.
#         Inputs:
#             qvfile  = QV output file name (.qv)
#             rptfile = report text file name (to write summary report)
#                       default "PSS(R)E Report"
#         Returns ierr.
#             ierr    = 0, no error
