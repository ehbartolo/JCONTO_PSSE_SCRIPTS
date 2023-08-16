# run_QV1D.py - 4 mpjobs
from __future__ import print_function
#***************************************************
#** Set paths, import modules, define run vars
#import os, sys
#import time
#sys.path.append('SCRIPTs\\')
#import JCtools_p27 as JCtools
#My = {}
#ier, My = JCtools.readIni('mpQV.ini',My,1)
#My['XVAR'] = 203
#My['RETURN']=[]
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
import pssarrays

#psspy.throwPsseExceptions = True
#__________________________________________________________________
def DFXmake(subfile,monfile,confile,dfxfile,dxoption):
    import psspy
    ierr = psspy.dfax(dxoption,subfile,monfile,confile,dfxfile)
    return ierr
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars = JCtools.ZYXvars(My)    #ZYX vars= [[studyi,zyxmsg],[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey]]
studyi  = zyxvars[0][0]
zyxmsg  = zyxvars[0][1]
xvarpath= zyxvars[1][0]
xvarkey = zyxvars[1][1]
#***************************************************
#** Set file names:
logopen = My['LOGOPEN'].lower()
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
if os.path.isfile(logfile) and logopen=='e':		#e= bypass run if log exist, w= overwrite, a= append
   status = 'Scenario <%s> was done or being processed!. Bypass now!'%studyi
if logopen=='e': logopen= 'w'
sys.stdout = open(logfile, logopen) # redirect all prints to this log file
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
savfile = My['SAVFILE']
subfile = My['SUBFILE']    
monfile = My['MONFILE']    
confile = My['CONFILE']    
dfxfile = My['DFXFILE']    
thrfile = My['THRFILE']        # Load Throwover Data file; blank for none
qvfile  = My['QVFILE']     
inlfile = My['INLFILE']        # Inertia and Governor Response Data file; blank for none
sublabel= My['SUBLABEL']       #label of dispatch subsystem; used if OPTIONS(12) is 1 through 4 (blank by default).
zipfile = My['ZIPFILE']        #ZIP Archive Output File (input; blank by default)
dfxoptions = My['DFXOPTIONS']

busid = My['XVAR']
root,ext = os.path.splitext(qvfile)
qvfile = My['OUTSPATH']+root+'_'+str(busid)+ext

lfoption4  = My['LFOPTION4']
#lfoption4 = [0,0,0,0,0,1,1,0,1,0,busid,0,0]
lfoption4[-3] = busid
qvoption  = My['QVOPTION']

#main:
for k in range(1):
    with JCtools.redirect_stdout():     #to suppress PSSe message when loading
    ier = psspy.case(savfile)
    if ier:
       print ('ERROR - when loading base case ',savfile)
       break
    if not os.path.isfile(dfxfile):
       ier = DFXmake(subfile, monfile, confile, dfxfile, dfxoptions)
       if ier:
          print ('ERROR - in DFXmake')
          break
    major = My['PSSEVERSION']
    if   major <= 32:
         ier = psspy.qv_engine(lfoption, qvoption, dfxfile, thrfile, qvfile)
    else:       #major >= 33:
         #ierr = psspy.qv_engine_2(lfoption2, qvoption, dfxfile, thrfile, qvfile)
         #ierr = psspy.qv_engine_3(lfoption3, qvoption, sublabel, dfxfile, thrfile, inlfile, qvfile)
         ier = psspy.qv_engine_4(lfoption4, qvoption, sublabel, dfxfile, thrfile, inlfile, qvfile, zipfile)
    if ier:
       print ('ERROR - in making QV file')
       break
    # ====================================================================================================
    rptfile = '%sqv_%s_summary.dat'%(My['OUTSPATH'],busid)
    ier = pssarrays.qv_summary_report(qvfile,rptfile)                     #works!
    if ier>0: 
       print ('qv_summary_report error ',ierr)
       break
    ##
    #colabels = 'TRIP1NUCLEAR'
    colabels = ''           #<- all ctgs
    rptfile = '%sqv_%s.dat'%(My['OUTSPATH'],busid)
    ier = pssarrays.qv_solution_report(qvfile,colabels,rptfile)           #works!
    if ier>0: 
       print ('qv_solution_report error ',ierr)

if My['PYVER']>=37:
   deltat = time.process_time() - time0
else:
   deltat = time.clock() - time0  
deltasecstr = '%12.3f'%(deltat)
deltasec = float(deltasecstr)
sys.stdout.close()                # ordinary file object
sys.stdout = stdoutreset          # restore print commands to interactive prompt
My['RETURN'].append([studyi,deltasec])
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
