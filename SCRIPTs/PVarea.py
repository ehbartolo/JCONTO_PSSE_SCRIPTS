# run_PVarea.py
from __future__ import print_function
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
#ierr, My = JCtools.readIni('mppv.ini',My,1)
#My['PYVER']= 37
#My['PSSEVERSION'] = 34
#My['XVAR'] = 'LIGHTCO'
#{----------------------------------------------------------------------------}
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
    
#--PV run for a single area------------------------------
# main:
savfile   = My['SAVFILE']
subfile   = My['SUBFILE']
monfile   = My['MONFILE']
confile   = My['CONFILE']
if 'DFXFILE' in My:
   dfxfile = My['DFXFILE']
else:
   dfxfile = '%s_%s.dfx'%(savfile,My['XVAR'])
thrfile = My['THRFILE']  
ecdfile = My['ECDFILE']  
inlfile = My['INLFILE']  
sublabel= My['SUBLABEL'] 
zipfile = My['ZIPFILE']  
dxoption  = My['DXOPTION']  
pvoption_6= My['PVOPTION_6'] 
pvstudy_6 = My['PVSTUDY_6']
Redispatchsys= My['REDISPATCHSYS']
#__________________________________________________________________
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()
zyxvars  = JCtools.ZYXvars(My)    #XYZ vars= [studyi,[xvarpath,xvarkey],[yvarpath,yvarkey],[zvarpath,zvarkey],zyxmsg]
studyi   = zyxvars[0][0]
zyxmsg   = zyxvars[0][1]
xvarpath = zyxvars[1][0]
xvarkey  = zyxvars[1][1]
#***************************************************
#** Set file names & vars that depend on XYZ vars:
Sink  = My['XVAR']
Source= 'SRC_%s'%Sink
pvfile  = '%s%s.pv'%(My['OUTSPATH'],studyi)    #PV output file
rptfile = '%s%s_pv.dat'%(My['OUTSPATH'],studyi)    #PV report file
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
sublabel_6 = [Source,Sink,Redispatchsys]
#print 'sublabel_6'
#print sublabel_6
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

#loading case
psspy.case(savfile)

#prepare a DFX file
#if not os.path.isfile(dfxfile):
DFXmake(subfile,monfile,confile,dfxfile,dxoption)

major = My['PSSEVERSION']
if   major <= 32:
     #psspy.pv_engine_2(pvoption_2,
     #                  pvstudy_2,
     #                  sublabel_2,
     #                  dfxfile,thrfile,ecdfile,pvfile)
     ierr = psspy.pv_engine_3(pvoption_3,
                       pvstudy_3,
                       sublabel_3,
                       dfxfile,thrfile,ecdfile,pvfile)
else:       # major >= 33:
     #psspy.pv_engine_4(pvoption_4,
     #                  pvstudy_4,
     #                  sublabel_4,
     #                  dfxfile,thrfile,ecdfile,pvfile)
     #psspy.pv_engine_5(pvoption_5,
     #                  pvstudy_5,
     #                  sublabel_5,
     #                  dfxfile,thrfile,ecdfile,inlfile,pvfile)
     ierr = psspy.pv_engine_6(pvoption_6,
                       pvstudy_6,
                       sublabel_6,
                       dfxfile,thrfile,ecdfile,inlfile,pvfile,zipfile)
if ierr:
   print ('pv_engine_6 return error %s'%ierr)
else:
  colabels = ''                 #<- all ctgs
  ierr = pssarrays.pv_solution_report(pvfile,colabels,rptfile)
  if ierr>0: 
     print ('pssarrays.pv_solution_report error %s'%ierr)
  #
  # runcompleted, now process output data
  #
  #rlst = pssarrays.pv_summary(pvfile)
  #print 'dfxfile=',rlst.file.dfx
  #
  #rptfile = 'pv_summary.dat'
  #ierr = pssarrays.pv_summary_report(pvfile,rptfile)
  #if ierr>0: 
  #   print 'ERROR on pssarrays.pv_summary_report:',ierr
  #
  #colabel = 'TRIP1NUCLEAR'
  #rlst = pssarrays.pv_solution(pvfile,colabel)
  #print 'mwtransfer=',rlst.mwtransfer
  #
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
# subsystems for source & sink shall be totally independent.
# accessing a dummy bus (insile a MSLine) causes a crush. Delete MSL in case.
#     pv_solution(pvfile=None, colabel=None)
#         rlst = pv_solution(pvfile,colabel)
#         PV analysis monitored flows and bus voltages for one contingency.
#         Inputs:
#             pvfile  = PV output file name (.pv)
#             colabel = contingency label (to get PV solution for)
#                       only one contingency label allowed
#         Returned object 'rlst' contains the following attributes:
#             rlst.ierr       = error code(0=no error)
#             rlst.island     = number of islands, integer
#             rlst.mwtransfer = MW transactions, float of length [ntrns]
#             rlst.cnvflag    = convergence flag (True when converged), logical of length [ntrns]
#             rlst.cnvcond    = convergence condition
#             rlst.mvaworst   = larget bus MVA mismatch, float of length [ntrns]
#             rlst.mvatotal   = total system MVA mismatch, float of length [ntrns]
#             rlst.volts      = monitored bus voltage (pu), float of length [nmvbus][ntrns]
#             rlst.mgenmw     = monitored plant MW, float of length [nmgnbus][ntrns]
#             rlst.mgenmvar   = monitored plant MVAR, float of length [nmgnbus][ntrns]
#             rlst.mloadmw    = monitored load MW, float of length [nmldbus][ntrns]
#             rlst.mloadmvar  = monitored load MVAR, float of length [nmldbus][ntrns]
#             rlst.mbrnmva    = monitored branch MVA flow (MVA), float of length [nmline][ntrns]
#             rlst.mbrnamp    = monitored branch flow, AMPS expressed in MVA or MVA, float of length [nmline][ntrns]
#                               The "brnflowunits" variable in pv_summary determine the units.
#                               Use this value to calculate branch loadings.
#              rlst.mitfmw   = monitored interface MW flow (MW), float of length [ninter][ntrns]
# 
#             where
#             ntrans  = number of MW transfer changes
#             nmvbus  = number of voltage monitored buses
#             nmgnbus = number of monitored plant (generator) buses
#             nmldbus = number of monitored load buses
#             nmline  = number of monitored branches
#             ninter  = number of monitored interfaces
# 
#     pv_solution_report(pvfile=None, colabels=None, rptfile=None)
#         ierr = pv_solution_report(pvfile,colabels,rptfile)
#         PV analysis solution text report.
#         Inputs:
#             pvfile   = PV output file name (.pv)
#             colabels = contingency labels (to get PV solution)
#                        default "all contingencies"
#                        for more than one contingency, provide as a list or tuple
#             rptfile  = report text file name (to write solution report)
#                        default "PSS(R)E Report"
#         Returns ierr.
#             ierr     = 0, no error
# 
#     pv_summary(pvfile=None)
#         rlst = pv_summary(pvfile)
#         Returns PV analysis summary.
#         Inputs:
#             pvfile = PV output file name (.pv)
#         Returned object 'rlst' contains the following attributes:
#             rlst.ierr                = error code (0=no error)
#             rlst.pvsize.ncase        = number of contingencies + 1 (for base case)
#             rlst.pvsize.nmline       = number of monitored branches
#             rlst.pvsize.ninter       = number of monitored interfaces
#             rlst.pvsize.nmvbus       = number of voltage monitored buses
#             rlst.pvsize.nmvrec       = number of voltage monitored records
#             rlst.pvsize.nmgnbus      = number of monitored plant (generator) buses
#             rlst.pvsize.nmldbus      = number of monitored load buses
#             rlst.pvsize.nmxtrns      = maximum number of MW transfer changes
#             rlst.options             = PV solution options (same as in API manual)
#             rlst.values              = PV solution values (same as in API manual)
#             rlst.brnflowunits.xfrcur = PV solution transformer branch flow units ('mbrnamp' in pv_solution return list)
#             rlst.brnflowunits.nxfrcr = PV solution non-transformer branch flow units ('mbrnamp' in pv_solution return list)
#             rlst.casetitle.line1     = short title line 1
#             rlst.casetitle.line2     = short title line 2
#             rlst.file.pv             = contingency output (.acc) file name
#             rlst.file.sav            = saved case (.sav) file name
#             rlst.file.ecd            = economic dispatch data (.ecd) file name
#             rlst.file.thr            = load throwover data (.thr) file name
#             rlst.file.dfx            = distribution factor data (.dfx) file name
#             rlst.file.sub            = subsystem definition data (.sub) file name
#             rlst.file.mon            = monitored element data (.mon) file name
#             rlst.file.con            = contingency description data (.con) file name
#             rlst.srcsink             = source and sink subsystem names
#             rlst.mbranch             = monitored branch names
#             rlst.mbrnrating.a        = rating A
#             rlst.mbrnrating.b        = rating B
#             rlst.mbrnrating.c        = rating C
#             rlst.minterface          = monitored interface names
#             rlst.mitfrating          = selected rating of monitored interface
#             rlst.mgenbus             = monitored plant (generator) bus label
#             rlst.mloadbus            = monitored load bus label
#             rlst.mvbuslabel          = monitored voltage bus label
#             rlst.mvreclabel          = monitored voltage record label
#             rlst.mvrecmax            = monitored voltage bus maximum
#             rlst.mvrecmin            = monitored voltage bus minimum
#             rlst.mvrectype           = monitored voltage record type (range/deviation)
#             rlst.colabel             = contingency labels
#             rlst.codesc              = contingency description
#             rlst.maxmw               = maximum MW transfer
#             rlst.minmw                                 = minimum MW transfer
# 
#     pv_summary_report(pvfile=None, rptfile=None)
#         ierr = pv_summary_report(pvfile,rptfile)
#         PV analysis summary text report.
#         Inputs:
#             pvfile  = PV output file name (.pv)
#             rptfile = report text file name (to write summary report)
#                       default "PSS(R)E Report"
#         Returns ierr.
#            ierr    = 0, no error
#
#run PV engine
#pvoption_2 = [1,0,1,1,1,  0,2,0,0,2,3,3,1,0,0,0,1,0,1,1,1]
#pvoption_3 = [1,0,1,1,1,  0,2,0,0,2,3,3,1,0,0,0,1,0,1,1,1]
#   pvoption_4(6) base case induction motor treatment flag; applied
#                 when an induction motor fails to solve due to low
#                 terminal voltage (0 by default).
#   pvoption_4(6) = 0 stall.
#   pvoption_4(6) = 1 trip.
#   pvoption_4(23) contingency case induction motor treatment flag;
#                  applied when an induction motor fails to solve due
#                  to low terminal voltage (0 by default).
#   pvoption_4(23) = 0 stall.
#   pvoption_4(23) = 1 trip.
#pvoption_4 = [1,0,1,1,1,0,0,2,0,0,2,3,3,1,0,0,0,1,0,1,1,1,0]
#     pvoption_5(18) dispatch mode for power unbalances resulting from
#                    the application of contingencies (0 by default).
#     pvoption_5(18) = 0 disable.
#     pvoption_5(18) = 1 in-service subsystem machines using reserve.
#     pvoption_5(18) = 2 in-service subsystem machines using Pmax.
#     pvoption_5(18) = 3 in-service subsystem machines using inertia.
#     pvoption_5(18) = 4 in-service subsystem machines using governor droop.
#pvoption_5 = [1,0,1,1,1,0,0,2,0,0,2,3,3,1,0,0,0,0,1,0,1,1,1,0]
#     pvoption_6(19) ZIP Archive flag (0 by default).
#     pvoption_6(19) = 0 No ZIP Archive file.
#     pvoption_6(19) = 1 Write ZIP Archive file ZIPFILE; preserve each
#                      system condition at its largest solved incremental transfer level.
#     pvoption_6(19) = 2 Write ZIP Archive file ZIPFILE; preserve each
#                      system condition at all of its solved incremental transfer levels.
#pvoption_6 = [1,0,1,1,1,0,0,2,0,0,2,3,3,1,0,0,0,0,0,1,0,1,1,1,0]
#
#pvstudy_2  = [ 0.5, 100.0, 10.0, 5000.0, 0.8, 100.0]
#     pvstudy_3(7) minimum incremental transfer in MW (< 0.0) (0.0 by default).
#pvstudy_3  = [ 0.5, 100.0, 10.0, 5000.0, 0.8, 100.0,0.0]
#pvstudy_4  = [ 0.5, 100.0, 10.0, 5000.0, 0.8, 100.0,0.0]
#     pvstudy_5(8) power factor for load increases in dispatch methods 2, 3 and 4 (0.0 by default).
#                  Specify as < 0.0 to retain the original p.f. at each load that is changed.
#pvstudy_5  = [ 0.5, 100.0, 10.0, 5000.0, 0.8, 100.0,0.0,0.0]
#pvstudy_6  = [ 0.5, 100.0, 10.0, 5000.0, 0.8, 100.0,0.0,0.0]
#sublabel_2 = [r"""STUDY""",r"""EAST"""]
#sublabel_3 = [r"""STUDY""",r"""EAST"""]
#sublabel_4 = [r"""STUDY""",r"""EAST"""]
#     sublabel_5(3)= label of the dispatch subsystem; used if pvoption_5(18) is 1 through 4 (blank by default).
#sublabel_5 = [r"""STUDY""",r"""EAST""",'']
#sublabel_6 = [r"""STUDY""",r"""EAST""",'']
#
#dfxoptions[0] # 1-calculate distribution factors
#dfxoptions[1] # 1-sort monitored elements
