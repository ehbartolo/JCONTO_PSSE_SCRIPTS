# grun.py - 4 mpjobs + grun.ini
from __future__ import print_function
#** Set paths, import modules, define run vars
#{----------------------------------------------------------------------------}
# in single run mode, no error.  In parallel mode, matplotlib issue an error with pop-up message!!
#import os, sys
#import time,datetime
#pythoncode = 'SCRIPTs\\'
#if os.environ['PYTHONCODE']:
#   pythoncode = os.environ['PYTHONCODE']
#sys.path.append(pythoncode)
#import JCtools
#My  = {}
#ierr, My = JCtools.readIni('mpGrun_govtuning.ini',My,1)
#My['PYVER']= 27
#My['PSSEVERSION'] = 34
#My['XVAR'] = 0.5
# =============================================================================================
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
# =============================================================================================
import dyntools
# =============================================================================================
# 1. Data extraction/information
def test_data_extraction(chnfobj):   
    print ('\n Testing call to get_data')
    sh_ttl, ch_id, ch_data = chnfobj.get_data()
    print (sh_ttl)
    print (ch_id)

    print ('\n Testing call to get_id')
    sh_ttl, ch_id = chnfobj.get_id()
    print (sh_ttl)
    print (ch_id)
    
    print ('\n Testing call to get_range')
    ch_range = chnfobj.get_range()
    print (ch_range)

    print ('\n Testing call to get_scale')
    ch_scale = chnfobj.get_scale()
    print (ch_scale)

    print ('\n Testing call to print_scale')
    chnfobj.print_scale()

    print ('\n Testing call to txtout')
    chnfobj.txtout(channels=[1,4])

    print ('\n Testing call to xlsout')
    chnfobj.xlsout(channels=[2,3,4,7,8,10])

# =============================================================================================
# 2. Multiple subplots in a figure, but one trace in each subplot
def test_subplots_one_trace(chnfobj,pltfile):
    #optnppg  = {'size':'Letter', 'orientation':'Portrait'}
    optnfmt  = {'rows':3,'columns':2,'dpi':300,
                'showttl'    : False,
                'showoutfnam': False,
                'showlogo'   : True}

    optnchn1 = {1:{'chns':1},2:{'chns':2},} #Pmec
    figfiles1 = chnfobj.xyplots(optnchn1,optnfmt,pltfile)

    #optnchn2 = {1:{'chns':{outfile2:1}},
    #            2:{'chns':{outfile2:3}},
    #            3:{'chns':{outfile2:2}},
    #            4:{'chns':{outfile2:4}},
    #            } #angles, speed
    #pn,x     = os.path.splitext(outfile2)
    #pltfile2 = pn+'.eps'
    #figfiles2 = chnfobj.xyplots(optnchn2,optnfmt,pltfile2)
      
# =============================================================================================
# 3. Multiple subplots in a figure and more than one trace in each subplot
def test_subplots_mult_trace(chnfobj):
    optnppg  = {'size':'Letter', 'orientation':'Portrait'}
    optnfmt  = {'rows':2,'columns':2,'dpi':300,'showttl':True}
    
    optnchn1 = {1:{'chns':[1]},2:{'chns':[2]},3:{'chns':[3]},4:{'chns':[4]},5:{'chns':[5]}}
    pn,x     = os.path.splitext(outfile1)
    pltfile1 = pn+'.png'

    optnchn2 = {1:{'chns':{outfile2:1}},
                2:{'chns':{'v82_test1_bus_fault.out':3}},
                3:{'chns':4},
                4:{'chns':[5]}
               }
    pn,x     = os.path.splitext(outfile2)
    pltfile2 = pn+'.pdf'

    optnchn3 = {1:{'chns':{'v80_test1_bus_fault.out':1}},
                2:{'chns':{'v80_test2_complex_wind.out':[1,5]}},
                3:{'chns':{'v82_test1_bus_fault.out':3}},
                5:{'chns':[4,5]},
               }
    pn,x     = os.path.splitext(outfile3)
    pltfile3 = pn+'.eps'

    chnfobj.xyplots(optnchn1,optnppg,optnfmt,pltfile1)
    chnfobj.xyplots(optnchn2,optnppg,optnfmt,pltfile2)
    chnfobj.xyplots(optnchn3,optnppg,optnfmt,pltfile3)
    
# =============================================================================================
# 4. Do XY plots and insert them into word file
def test_plots2word(chnfobj):
    p,nx       = os.path.split(outfile1)
    docfile    = os.path.join(p,'savnw_response.doc')
    show       = True
    overwrite  = True
    caption    = True
    align      = 'center'
    captionpos = 'below'
    height     = 0.0
    width      = 0.0
    rotate     = 0.0
    
    optnppg  = {'size':'Letter', 'orientation':'Portrait'}
    optnfmt  = {'rows':3,'columns':1,'dpi':300,'showttl':True}
    
    optnchn  = {1:{'chns':{outfile1:13,  outfile2:13} },
                2:{'chns':{outfile1:15,  outfile2:15} },
               }
    chnfobj.xyplots2doc(optnchn,optnppg,optnfmt,docfile,show,overwrite,caption,align,
                        captionpos,height,width,rotate)
    return
#__________________________________________________________________
title1     = My['TITLE1']   
title2     = My['TITLE2']   
studyname  = My['STUDYNAME']
StudyType  = My['STUDYTYPE']
cnvfile    = My['CNVFILE']      
snpfile    = My['SNPFILE']      
Genbus     = My['GENBUS']     
initloading= My['INITLOADING']
Pdelta     = My['PDELTA']     
simtime    = My['SIMTIME']    
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
#** Set file names:
logfile = '%s%s.log'%(My['LOGSPATH'],studyi)
outfile = '%s%s.out'%(My['OUTSPATH'],studyi)
plotfile= '%s%s.pdf'%(My['PLOTSPATH'],studyi)
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
psspy.case(cnvfile)
psspy.rstr(snpfile)
#
model    = My['MODEL']   
modelCON = My['MODELCON']
Genbus   = My['GENBUS']  
Genid    = str(My['GENID'])
psspy.change_plmod_con(Genbus,Genid,model,modelCON,My['XVAR'])  # droop sensitivity

psspy.dynamics_solution_params([99,_i,_i,_i,_i,_i,_i,_i],
                               [0.8,_f, 0.001, 0.004,_f,_f,_f,_f],'')
psspy.gstr(Genbus,initloading,Pdelta,outfile)
psspy.grun(simtime,99,99,0)

#plotting
#outlst = [My['OUTFILE'],]
#chnf = dyntools.CHNF(outlst)
#test_subplots_one_trace(chnf,My['PLOTFILE'])

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
